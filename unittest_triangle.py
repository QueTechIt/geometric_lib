import unittest
from triangle import calculate_area, calculate_perimeter

class TestTriangleFunctions(unittest.TestCase):

    def test_calculate_area(self):
        # Тестируем площадь треугольника с известными сторонами
        self.assertAlmostEqual(calculate_area(3, 4, 5), 6.0, places=2)  # Площадь 6
        self.assertAlmostEqual(calculate_area(5, 5, 5), 10.83, places=2)  # Площадь для равностороннего треугольника
        self.assertAlmostEqual(calculate_area(10, 10, 10), 43.30, places=2)  # Площадь для равностороннего треугольника

    def test_calculate_perimeter(self):
        # Тестируем периметр треугольника с известными сторонами
        self.assertEqual(calculate_perimeter(3, 4, 5), 12)  # Периметр 12
        self.assertEqual(calculate_perimeter(5, 5, 5), 15)  # Периметр 15
        self.assertEqual(calculate_perimeter(10, 10, 10), 30)  # Периметр 30

    def test_invalid_triangle(self):
        # Проверяем, что функция не вызывает ошибок для некорректных данных
        with self.assertRaises(ValueError):
            calculate_area(1, 2, 3)  # Стороны не мообразовать треугольник

if __name__ == '__main__':
    unittest.main()
