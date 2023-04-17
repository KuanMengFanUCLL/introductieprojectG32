from abc import ABC, abstractmethod
from math import pi
class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...
    
    @property
    @abstractmethod
    def perimeter(self):
        ...
        
class Rectangle(Shape):
    def __init__(self,width,length):
        self.width = width
        self.lengh = length
    
    @property
    def area(self):
        return self.width * self.lengh

    @property
    def perimeter(self):
        return 2 * (self.lengh + self.width)

class Square(Rectangle):
    def __init__(self,side):
        self.side = side

    @property
    def area(self):
        return self.side**2
    
    @property
    def perimeter(self):
        return self.side*4

class Circle(Shape):
    def __init__(self,radius):
         self.radius = radius

    @property
    def area(self):
        return pi * self.radius**2
    
    @property
    def perimeter(self):
        return 2*pi*self.radius
