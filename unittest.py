import unittest
import rectangle
import circle
import triangle
import square

class GeometryTestCase(unittest.TestCase):
    '''Тестирование функциональности прямоугольника'''

    def test_rectangle_area_with_zero_height(self):
        # Проверка площади прямоугольника с нулевой высотой
        self.assertEqual(rectangle.area(8, 0), 0)

    def test_rectangle_area_with_equal_sides(self):
        # Проверка площади квадрата (прямоугольника с равными сторонами)
        self.assertEqual(rectangle.area(7, 7), 49)

    def test_rectangle_perimeter_with_zero_height(self):
        # Проверка периметра прямоугольника с нулевой высотой
        self.assertEqual(rectangle.perimeter(8, 0), 16)

    def test_rectangle_perimeter_with_valid_dimensions(self):
        # Проверка периметра прямоугольника с положительными сторонами
        self.assertEqual(rectangle.perimeter(6, 12), 36)

    '''Негативные тесты для прямоугольника'''

    def test_rectangle_area_with_negative_width(self):
        # Проверка на ошибку при использовании отрицательной ширины
        with self.assertRaises(ValueError):
            rectangle.area(-2, 5)

    def test_rectangle_area_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения
        with self.assertRaises(TypeError):
            rectangle.area("b", 5)

    def test_rectangle_perimeter_with_negative_width(self):
        # Проверка на ошибку при использовании отрицательной ширины для периметра
        with self.assertRaises(ValueError):
            rectangle.perimeter(-2, 5)

    def test_rectangle_perimeter_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для периметра
        with self.assertRaises(TypeError):
            rectangle.perimeter("b", 5)

    '''Тестирование функциональности круга'''

    def test_circle_area_with_zero_radius(self):
        # Проверка площади круга с нулевым радиусом
        self.assertEqual(circle.area(0), 0)

    def test_circle_area_with_positive_radius(self):
        # Проверка площади круга с положительным радиусом
        self.assertAlmostEqual(circle.area(4), 50.24, places=2)

    def test_circle_perimeter_with_zero_radius(self):
        # Проверка периметра круга с нулевым радиусом
        self.assertEqual(circle.perimeter(0), 0)

    def test_circle_perimeter_with_positive_radius(self):
        # Проверка периметра круга с положительным радиусом
        self.assertAlmostEqual(circle.perimeter(4), 25.12, places=2)

    '''Негативные тесты для круга'''

    def test_circle_area_with_negative_radius(self):
        # Проверка на ошибку при использовании отрицательного радиуса
        with self.assertRaises(ValueError):
            circle.area(-3)

    def test_circle_perimeter_with_negative_radius(self):
        # Проверка на ошибку при использовании отрицательного радиуса для периметра
        with self.assertRaises(ValueError):
            circle.perimeter(-3)

    def test_circle_area_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для площади
        with self.assertRaises(TypeError):
            circle.area("b")

    def test_circle_perimeter_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для периметра
        with self.assertRaises(TypeError):
            circle.perimeter("b")

    '''Тестирование функциональности треугольника'''

    def test_triangle_area_with_base_and_height(self):
        # Проверка площади треугольника с заданными основанием и высотой
        self.assertAlmostEqual(triangle.area(5, 6), 15.0)

    def test_triangle_perimeter_with_valid_sides(self):
        # Проверка периметра треугольника с корректными длинами сторон
        self.assertEqual(triangle.perimeter(5, 12, 13), 30)

    '''Негативные тесты для треугольника'''

    def test_triangle_area_with_negative_height(self):
        # Проверка на ошибку при использовании отрицательной высоты
        with self.assertRaises(ValueError):
            triangle.area(-2, 6)

    def test_triangle_perimeter_with_invalid_sides(self):
        # Проверка на ошибку при использовании сторон, не образующих треугольник
        with self.assertRaises(ValueError):
            triangle.perimeter(5, 12, 20)

    def test_triangle_area_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для площади
        with self.assertRaises(TypeError):
            triangle.area("b", 6)

    def test_triangle_perimeter_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для периметра
        with self.assertRaises(TypeError):
            triangle.perimeter(5, 12, "d")

    '''Тестирование функциональности квадрата'''

    def test_square_area_with_side_length(self):
        # Проверка площади квадрата с заданной длиной стороны
        self.assertEqual(square.area(6), 36)

    def test_square_perimeter_with_side_length(self):
        # Проверка периметра квадрата с заданной длиной стороны
        self.assertEqual(square.perimeter(5), 20)

    '''Негативные тесты для квадрата'''

    def test_square_area_with_negative_side(self):
        # Проверка на ошибку при использовании отрицательной длины стороны
        with self.assertRaises(ValueError):
            square.area(-2)

    def test_square_perimeter_with_negative_side(self):
        # Проверка на ошибку при использовании отрицательной длины стороны для периметра
        with self.assertRaises(ValueError):
            square.perimeter(-10)

    def test_square_area_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для площади
        with self.assertRaises(TypeError):
            square.area("a")

    def test_square_perimeter_with_string_input(self):
        # Проверка на ошибку при передаче строкового значения для периметра
        with self.assertRaises(TypeError):
            square.perimeter("b")
