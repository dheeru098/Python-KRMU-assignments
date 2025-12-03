Library Inventory Manager - Mini Project

This is my mini project for the subject Programming for Problem Solving Using Python.
I have made a simple library inventory manager which runs in the command line. The idea was to use Python classes, JSON file saving, basic exception handling, logging and a menu to manage books.

WHAT THE PROJECT CAN DO:
- Add a new book with title, author and isbn
- View all the books saved
- Issue a book (change its status to Issued)
- Return a book (change status back to Available)
- Save everything in a JSON file called catalog.json
- Keep a record of actions inside library.log
- Handle wrong input or missing files safely
- I also added one small unit test for bonus

COMMAND LINE PART:
When I run the project, it shows a simple menu in the terminal:

1. Add Book
2. View All Books
3. Issue Book
4. Return Book
5. Exit

If I type 1, it asks for book details.
If I type 2, it prints all books.
If I type 3, the program tries to issue the book.
If I type 4, it returns the book.
Typing 5 exits the program.

This is the menu driven CLI required in the assignment.

WHY I MADE IT THIS WAY:
The assignment wanted class-based design plus file handling. So I used:
- Book class for storing one book
- LibraryInventory class for the whole book list
- JSON instead of text file because it is easier
- try-except blocks for safe running
- logging module for tracking issue and return
I kept the whole code simple so I can understand it and explain it during viva.

PROJECT FILES IN MY FOLDER:
lab_assignment_3.py        -> Main python program
catalog.json               -> JSON file where books get saved
library.log                -> Log file for book actions
tests/test_basic.py        -> Small unit test file
README.md                  -> This explanation file
requirements.txt           -> List of modules used

HOW TO RUN THE PROJECT:
1. Open terminal inside the folder
2. Run this command:
   python lab_assignment_3.py
3. Type numbers (1 to 5) to select options
4. The JSON and log files get created automatically

MODULES I USED (all built-in):
json
pathlib
logging
unittest

HOW TO RUN THE TEST FILE (BONUS):
Run this command:
python -m unittest tests/test_basic.py
If everything is correct, the output will show OK.

NOTES:
- If the catalog.json file is deleted, the program makes a new one automatically.
- The book status (Available / Issued) is stored permanently.
- Logging is used so you can track when books were issued or returned.
- I followed everything mentioned in the assignment: OOP, JSON, CLI and error handling.
- I wrote the code in a simple and easy way so I can explain it properly.

AUTHOR:
Dheeraj Kumar Yadav
B.Tech CSE (AI & ML)

