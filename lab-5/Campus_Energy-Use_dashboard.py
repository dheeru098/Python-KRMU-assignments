import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

# ==========================================================
# PROJECT PATH SETUP
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR / "data"   # <-- uses small letters (correct folder)


# ==========================================================
# TASK 1 – INGEST & VALIDATE MULTIPLE CSV FILES
# ==========================================================

def load_energy_data():
    """Reads all CSV files from /data, validates them,
       and returns a single combined DataFrame + logs."""

    logs = []
    frames = []

    if not DATA_FOLDER.exists():
        raise FileNotFoundError(f"Data folder not found: {DATA_FOLDER}")

    csv_files = list(DATA_FOLDER.glob("*.csv"))

    if len(csv_files) == 0:
        raise FileNotFoundError("No CSV files found in data folder.")

    for file in csv_files:
        try:
            df = pd.read_csv(file, on_bad_lines="skip")

            # file example: home_block_2024-01.csv
            parts = file.stem.split("_")
            building = parts[0] if len(parts) > 0 else "unknown"
            month = parts[-1] if len(parts) > 1 else "unknown"

            # add metadata if missing
            if "building" not in df.columns:
                df["building"] = building

            if "month" not in df.columns:
                df["month"] = month

            # validate structure
            if "timestamp" not in df.columns or "kwh" not in df.columns:
                logs.append(f"Skipped {file.name} → missing timestamp/kwh")
                continue

            df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
            df = df.dropna(subset=["timestamp", "kwh"])

            frames.append(df)

        except Exception as e:
            logs.append(f"Failed to read {file.name}: {e}")

    combined = pd.concat(frames, ignore_index=True)
    return combined, logs


# ==========================================================
# TASK 2 – DAILY & WEEKLY AGGREGATES
# ==========================================================

def get_daily_usage(df):
    df = df.set_index("timestamp")
    return df.resample("D")["kwh"].sum()

def get_weekly_usage(df):
    df = df.set_index("timestamp")
    return df.resample("W")["kwh"].sum()

def get_building_summary(df):
    return df.groupby("building")["kwh"].agg(["mean", "min", "max", "sum"])


# ==========================================================
# TASK 3 – OBJECT-ORIENTED DESIGN
# ==========================================================

class MeterEntry:
    def __init__(self, ts, value):
        self.ts = ts
        self.value = value

class Building:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add_reading(self, entry: MeterEntry):
        self.records.append(entry)

    def total_kwh(self):
        return sum(x.value for x in self.records)

    def generate_report(self):
        return f"{self.name}: {self.total_kwh():.2f} kWh"

class BuildingManager:
    def __init__(self):
        self.buildings = {}

    def load_from_df(self, df):
        for _, row in df.iterrows():
            name = row["building"]
            if name not in self.buildings:
                self.buildings[name] = Building(name)

            self.buildings[name].add_reading(
                MeterEntry(row["timestamp"], row["kwh"])
            )

    def reports(self):
        return [b.generate_report() for b in self.buildings.values()]


# ==========================================================
# TASK 4 – VISUAL DASHBOARD
# ==========================================================

def generate_dashboard(df, daily, weekly, summary):
    fig, ax = plt.subplots(3, 1, figsize=(12, 14))

    # Daily line
    ax[0].plot(daily.index, daily.values)
    ax[0].set_title("Daily Energy Consumption")
    ax[0].set_ylabel("kWh")

    # Building bar chart
    ax[1].bar(summary.index, summary["sum"])
    ax[1].set_title("Total Usage Per Building")
    ax[1].set_ylabel("kWh")
    ax[1].set_xticklabels(summary.index, rotation=45)

    # Scatter of all readings
    ax[2].scatter(df["timestamp"], df["kwh"], s=12)
    ax[2].set_title("All Meter Readings")
    ax[2].set_xlabel("Timestamp")
    ax[2].set_ylabel("kWh")

    plt.tight_layout()
    plt.savefig(BASE_DIR / "dashboard.png")
    plt.close()


# ==========================================================
# TASK 5 – EXPORT CLEANED FILES + SUMMARY REPORT
# ==========================================================

def export_results(df, summary, daily, weekly):

    df.to_csv(BASE_DIR / "cleaned_energy_data.csv", index=False)
    summary.to_csv(BASE_DIR / "building_summary.csv")

    # peak load
    peak = df.loc[df["kwh"].idxmax()]
    peak_time = peak["timestamp"]
    peak_value = peak["kwh"]

    total = df["kwh"].sum()
    top_building = summary["sum"].idxmax()

    with open(BASE_DIR / "summary.txt", "w", encoding="utf-8") as f:
        f.write("CAMPUS ENERGY SUMMARY REPORT\n")
        f.write("-------------------------------------\n")
        f.write(f"Total Energy Consumption: {total:.2f} kWh\n")
        f.write(f"Highest Usage Building: {top_building}\n")
        f.write(f"Peak Load: {peak_value:.2f} kWh at {peak_time}\n")
        f.write("\nDaily Trend:\n")
        f.write(str(daily.head()))
        f.write("\n\nWeekly Trend:\n")
        f.write(str(weekly.head()))
        f.write("\n")


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def main():
    print("=== Running Campus Energy Dashboard ===")

    df, logs = load_energy_data()

    if logs:
        print("\nLOGS:")
        for msg in logs:
            print(" -", msg)

    daily = get_daily_usage(df)
    weekly = get_weekly_usage(df)
    summary = get_building_summary(df)

    manager = BuildingManager()
    manager.load_from_df(df)

    print("\nBuilding Reports:")
    for line in manager.reports():
        print(" ", line)

    generate_dashboard(df, daily, weekly, summary)
    export_results(df, summary, daily, weekly)

    print("\n✓ All files generated successfully!")


if __name__ == "__main__":
    main()
