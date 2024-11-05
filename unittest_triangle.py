import unittest
from triangle import calculate_area, calculate_perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_calculate_area(self):
        # 1. Площадь треугольника с известными сторонами (3, 4, 5)
        self.assertAlmostEqual(calculate_area(3, 4, 5), 6.0, places=2)

        # 2. Площадь равностороннего треугольника со стороной 5
        self.assertAlmostEqual(calculate_area(5, 5, 5), 10.83, places=2)

        # 3. Площадь равнобедренного треугольника (6, 6, 5)
        self.assertAlmostEqual(calculate_area(6, 6, 5), 13.64, places=2)

        # 4. Площадь треугольника (10, 10, 10)
        self.assertAlmostEqual(calculate_area(10, 10, 10), 43.30, places=2)

        # 5. Площадь треугольника (8, 15, 17)
        self.assertAlmostEqual(calculate_area(8, 15, 17), 60.0, places=2)

        # 6. Площадь треугольника (7, 24, 25)
        self.assertAlmostEqual(calculate_area(7, 24, 25), 84.0, places=2)

        # 7. Площадь треугольника (5, 12, 13)
        self.assertAlmostEqual(calculate_area(5, 12, 13), 30.0, places=2)

        # 8. Площадь треугольника (2, 2, 3)
        self.assertAlmostEqual(calculate_area(2, 2, 3), 1.98, places=2)

        # 9. Площадь треугольника (1, 1, 1)
        self.assertAlmostEqual(calculate_area(1, 1, 1), 0.43, places=2)

        # 10. Площадь треугольника (5, 5, 8)
        self.assertAlmostEqual(calculate_area(5, 5, 8), 12.0, places=2)

    def test_calculate_perimeter(self):
        # 1. Периметр треугольника (3, 4, 5)
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)

        # 2. Периметр равностороннего треугольника со стороной 5
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)

        # 3. Периметр равнобедренного треугольника (6, 6, 5)
        self.assertEqual(calculate_perimeter(6, 6, 5), 17)

        # 4. Периметр треугольника (10, 10, 10)
        self.assertEqual(calculate_perimeter(10, 10, 10), 30)

        # 5. Периметр треугольника (8, 15, 17)
        self.assertEqual(calculate_perimeter(8, 15, 17), 40)

        # 6. Периметр треугольника (7, 24, 25)
        self.assertEqual(calculate_perimeter(7, 24, 25), 56)

        # 7. Периметр треугольника (5, 12, 13)
        self.assertEqual(calculate_perimeter(5, 12, 13), 30)

        # 8. Периметр треугольника (2, 2, 3)
        self.assertEqual(calculate_perimeter(2, 2, 3), 7)

        # 9. Периметр треугольника (1, 1, 1)
        self.assertEqual(calculate_perimeter(1, 1 , 1), 3)

        # 10. Периметр треугольника (5, 5, 8)
        self.assertEqual(calculate_perimeter(5, 5, 8), 18)

if __name__ == '__main__':
    unittest.main()
