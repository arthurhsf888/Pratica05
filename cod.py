import unittest

def is_first_semester(month):
    if month >= 1 and month <= 6:
        return True
    else:
        return False

class TestFirstSemester(unittest.TestCase):
    def test_january(self):
        self.assertTrue(is_first_semester(1))

    def test_february(self):
        self.assertTrue(is_first_semester(2))

    def test_march(self):
        self.assertTrue(is_first_semester(3))

    def test_april(self):
        self.assertTrue(is_first_semester(4))

    def test_may(self):
        self.assertTrue(is_first_semester(5))

    def test_june(self):
        self.assertTrue(is_first_semester(6))

    def test_july(self):
        self.assertFalse(is_first_semester(7))

    def test_august(self):
        self.assertFalse(is_first_semester(8))

    def test_september(self):
        self.assertFalse(is_first_semester(9))

    def test_october(self):
        self.assertFalse(is_first_semester(10))

    def test_november(self):
        self.assertFalse(is_first_semester(11))

    def test_december(self):
        self.assertFalse(is_first_semester(12))

if __name__ == '__main__':
    unittest.main()
