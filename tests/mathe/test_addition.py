import unittest
from lernstube.mathe.addition import Addition

class TestAddition(unittest.TestCase):

    def setUp(self):
        self.addition = Addition()

    def test_beschreibung(self):
        res = raw_input(self.addition.beschreibung())
        print self.addition.pruefung(res)
        pass

if __name__ == "__main__":
    unittest.main()
