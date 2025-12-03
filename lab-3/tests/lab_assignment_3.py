import json
import logging
from pathlib import Path

logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "Issued":
            return False
        self.status = "Issued"
        return True

    def return_book(self):
        if self.status == "Available":
            return False
        self.status = "Available"
        return True

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"


class LibraryInventory:
    def __init__(self):
        self.file_path = Path("catalog.json")
        self.books = []
        self.load_data()

    def load_data(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**b) for b in data]
        except Exception:
            logging.error("Error loading catalog. Resetting.")
            self.books = []
            self.save_data()

    def save_data(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
        except Exception:
            logging.error("Error saving catalog.")

    def add_book(self, title, author, isbn):
        b = Book(title, author, isbn)
        self.books.append(b)
        self.save_data()
        logging.info("New book added.")
        return b

    def find_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def get_all(self):
        return self.books


# ---------------- MAIN CLI ------------------

if __name__ == "__main__":
    inventory = LibraryInventory()

    while True:
        print("\n===== Library Inventory Manager =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            isbn = input("Enter ISBN: ")
            inventory.add_book(title, author, isbn)
            print("Book added.")

        elif choice == "2":
            for b in inventory.get_all():
                print(b)

        elif choice == "3":
            isbn = input("ISBN to issue: ")
            b = inventory.find_book(isbn)
            if b and b.issue():
                inventory.save_data()
                print("Book issued.")
            else:
                print("Cannot issue this book.")

        elif choice == "4":
            isbn = input("ISBN to return: ")
            b = inventory.find_book(isbn)
            if b and b.return_book():
                inventory.save_data()
                print("Book returned.")
            else:
                print("Cannot return this book.")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")
