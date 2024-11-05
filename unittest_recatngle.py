import unittest
from rectangle import calculate_area, calculate_perimeter

class TestRectangleFunctions(unittest.TestCase):

    # Тесты для функции calculate_area
    def test_area_positive_integers(self):
        self.assertEqual(calculate_area(5, 10), 50)

    def test_area_zero_length(self):
        self.assertEqual(calculate_area(0, 10), 0)

    def test_area_zero_width(self):
        self.assertEqual(calculate_area(10, 0), 0)

    def test_area_negative_length(self):
        self.assertEqual(calculate_area(-5, 10), -50)

    def test_area_negative_width(self):
        self.assertEqual(calculate_area(5, -10), -50)

    def test_area_large_numbers(self):
        self.assertEqual(calculate_area(10000, 20000), 200000000)

    def test_area_float_values(self):
        self.assertAlmostEqual(calculate_area(5.5, 2), 11)

    def test_area_negative_values(self):
        self.assertEqual(calculate_area(-5, -10), 50)

    def test_area_one_side_zero(self):
        self.assertEqual(calculate_area(0, 0), 0)

    def test_area_identity(self):
        self.assertEqual(calculate_area(1, 1), 1)

    # Тесты для функции calculate_perimeter
    def test_perimeter_positive_integers(self):
        self.assertEqual(calculate_perimeter(5, 10), 30)

    def test_perimeter_zero_length(self):
        self.assertEqual(calculate_perimeter(0, 10), 20)

    def test_perimeter_zero_width(self):
        self.assertEqual(calculate_perimeter(10, 0), 20)

    def test_perimeter_negative_length(self):
        self.assertEqual(calculate_perimeter(-5, 10), 10)

    def test_perimeter_large_numbers(self):
        self.assertEqual(calculate_perimeter(10000, 20000), 60000)

    def test_perimeter_float_values(self):
        self.assertAlmostEqual(calculate_perimeter(5.5, 2), 15)

    def test_perimeter_one_side_zero(self):
        self.assertEqual(calculate_perimeter(0, 0), 0)

    def test_perimeter_identity(self):
        self.assertEqual(calculate_perimeter(1, 1), 4)

if __name__ == "__main__":
    unittest.main()
