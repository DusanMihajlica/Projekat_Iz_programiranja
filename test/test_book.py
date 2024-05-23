import unittest
from klasa import Book
class Test_Book(unittest.TestCase):
    def test_dodavanje_naslova(self):
    Book = book("Na Drini cuprija")
    self.assertEqual(book.naziv, "Na Drini cuprija")
        
if __name__ == '__main__':
   unittest.main()