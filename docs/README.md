# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Rectangle
- Площадь
- Функция вычисления площади прямоугльника принмает два целых числа: длину и ширину
```
def area(a, h):
```
- Функция возвращает произведение чисел - площадь прямоугльника
```
return a*b
```
Например введы числа 5 и 6. будет выведено 30
- Периметр
- Функция принмает два целых числа - длину и ширину прямоугольника и возврщает удвоенную сумму a и b - периметр прямоугльника 
```
- def perimetr(a,b):
- return 2*(a+b)
```
Еcли будет введено 10 и 20, то будет выведено 30
- commit  * 2bb21a4 Add rectangle.py [https://github.com/KulEDmitr/geometric_lib/commit/2bb21a4a38474090eb514acc8b8afe92adf8c949]
- commit * e2bf6b5 Fix rectangle.py [https://github.com/KulEDmitr/geometric_lib/commit/e2bf6b5792a0b1121413627251867f2dd9927bb6]
## Triangle

- Функция вычисления площади треугольника принмает два целых числа: сторона прямоугльника и высота проведення к стороне
```
- def area(a, b):
```
- Функция возвращает произведение чисел - площадь прямоугльника
```
- return a*b/2
```
Если введены числв 30 и 6, то будет выведено 90
- Функция принмает три целых числа - длины сторон треугольника и возврщает сумму a, b и c - периметр треугольника
```
- def perimetr(a,b,c):
- return 2*(a+b)
```
 Пример: введены числа 3, 4 и 5 - будет выведено 12 
- commit  * 5aef15c  Add triangle.py [https://github.com/KulEDmitr/geometric_lib/commit/5aef15c0c5e49fcecdc6ddc2dfdd0c372c14f0d3]
