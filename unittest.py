import unittest
import rectangle
import circle
import triangle
import square

class GeometryTestCase(unittest.TestCase):
    '''Тесты для прямоугольника'''
    def test_rectangle_area_zero_mul(self):
        self.assertEqual(rectangle.area(10, 0), 0)
    
    def test_rectangle_area_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)
    
    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(10, 0), 20)
    
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 10), 30)

    '''Негативные тесты для прямоугольника'''
    def test_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)
            
    def test_rectangle_area_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 5)
    
    def test_rectangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-1, 5)


    def test_rectangle_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("a", 5)

    '''Тесты для круга'''
    def test_circle_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
    
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(5), 78.54, places=3)
    
    def test_circle_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.416, places=3)

    '''Негативные тесты для круга'''
    def test_circle_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_circle_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_circle_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("a")

    def test_circle_perimeter_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("a")

    '''Тесты для треугольника'''
    def test_triangle_area(self):
        self.assertAlmostEqual(triangle.area(3, 4), 6.0)
    
    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    '''Негативные тесты для треугольника'''
    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 4)

    def test_triangle_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(3, 4, 8)

    def test_triangle_area_string(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 4)

    def test_triangle_perimeter_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(3, 4, "c")

    '''Тесты для квадрата'''
    def test_square_area(self):
        self.assertEqual(square.area(5), 25)
    
    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(4), 16)

    '''Негативные тесты для квадрата'''
    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_square_area_string(self):
        with self.assertRaises(TypeError):
            square.area("a")

    def test_square_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")
