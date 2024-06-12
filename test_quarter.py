import unittest

from quarter import get_quarter

class TestGetQuarter(unittest.TestCase):

    def test_first_quarter(self):
        self.assertEqual(get_quarter(1), 1)
        self.assertEqual(get_quarter(2), 1)
        self.assertEqual(get_quarter(3), 1)

    def test_second_quarter(self):
        self.assertEqual(get_quarter(4), 2)
        self.assertEqual(get_quarter(5), 2)
        self.assertEqual(get_quarter(6), 2)

    def test_third_quarter(self):
        self.assertEqual(get_quarter(7), 3)
        self.assertEqual(get_quarter(8), 3)
        self.assertEqual(get_quarter(9), 3)

    def test_fourth_quarter(self):
        self.assertEqual(get_quarter(10), 4)
        self.assertEqual(get_quarter(11), 4)
        self.assertEqual(get_quarter(12), 4)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            get_quarter(0)
        with self.assertRaises(ValueError):
            get_quarter(13)

if __name__ == '__main__':
    unittest.main()
