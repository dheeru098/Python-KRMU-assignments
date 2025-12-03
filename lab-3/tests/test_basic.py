import unittest
from ..lab_assignment_3 import Book

class TestBookFunctions(unittest.TestCase):

    def test_issue_book(self):
        b = Book("Sample", "Author", "100")
        self.assertTrue(b.issue())

    def test_return_book(self):
        b = Book("Test", "Author", "200", status="Issued")
        self.assertTrue(b.return_book())

if __name__ == "__main__":
    unittest.main()
