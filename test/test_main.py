import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class Test_Main(unittest.TestCase):
   def test_citanja_fajla(self):
      with open("fajl.txt", "r") as file:
        str = file.readline()
        self.assertEqual(str, "proba")


if __name__ == '__main__':
   unittest.main()   