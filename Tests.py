import unittest
import rectangle
import circle
import triangle
import square

class GeometryTestCase(unittest.TestCase):
    '''Тесты для прямоугольника'''
    def test_rectangle_area_zero_mul(self):
        self.assertEqual(rectangle.area(15, 0), 0)
    
    def test_rectangle_area_square_mul(self):
        self.assertEqual(rectangle.area(15, 15), 225)
    
    def test_rectangle_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(15, 0), 30)
    
    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(7, 12), 38)

    '''Негативные тесты для прямоугольника'''
    def test_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-2, 6)
            
    def test_rectangle_area_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("b", 6)
    
    def test_rectangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-2, 6)

    def test_rectangle_perimeter_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("b", 6)

    '''Тесты для круга'''
    def test_circle_area_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
    
    def test_circle_area(self):
        self.assertAlmostEqual(circle.area(6), 113.097, places=3)
    
    def test_circle_perimeter_zero_radius(self):
        self.assertEqual(circle.perimeter(0), 0)
    
    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(6), 37.699, places=3)

    '''Негативные тесты для круга'''
    def test_circle_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.area(-2)

    def test_circle_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-2)

    def test_circle_area_string(self):
        with self.assertRaises(TypeError):
            circle.area("b")

    def test_circle_perimeter_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("b")

    '''Тесты для треугольника'''
    def test_triangle_area(self):
        self.assertAlmostEqual(triangle.area(5, 6), 15.0)
    
    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 6, 7), 18)

    '''Негативные тесты для треугольника'''
    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-2, 6)

    def test_triangle_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(5, 6, 12)

    def test_triangle_area_string(self):
        with self.assertRaises(TypeError):
            triangle.area("b", 6)

    def test_triangle_perimeter_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter(5, 6, "d")

    '''Тесты для квадрата'''
    def test_square_area(self):
        self.assertEqual(square.area(7), 49)
    
    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    '''Негативные тесты для квадрата'''
    def test_square_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-2)

    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-2)

    def test_square_area_string(self):
        with self.assertRaises(TypeError):
            square.area("b")

    def test_square_perimeter_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("b")
