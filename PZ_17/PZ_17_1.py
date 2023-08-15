# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления
# площади, длины окружности и диаметра.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
    def calculate_diameter(self):
        return 2 * self.radius

# Создаем объект класса Круг с радиусом 5
circle = Circle(5)

# Вычисляем и выводим площадь, длину окружности и диаметр
print("Площадь круга:", circle.calculate_area())
print("Длина окружности:", circle.calculate_circumference())
print("Диаметр круга:", circle.calculate_diameter())
