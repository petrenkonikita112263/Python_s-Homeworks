import unittest
from square_preceding import square_preceding


class TestSquarePreceding(unittest.TestCase):
    def test_positive_numbers_in_list(self):
        self.assertEqual(square_preceding([1, 2, 3]), [0, 1, 4])

    def test_negative_numbers_in_list(self):
        self.assertEqual(square_preceding([-1, -2, -3]), [0, 1, 4])


if __name__ == "__main__":
    unittest.main()
