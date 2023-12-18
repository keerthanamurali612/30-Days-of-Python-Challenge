# Write a Python program to create a class representing a Circle.
# The class should have two private variables: radius and area.
# The class should also have a constructor that takes the radius as an argument,
# a getter method for the area, and a setter method for the radius.
import math


class Circle:
    def __init__(self,radius,area):
        self.__radius=radius
        self.__area=None

    def get_area(self):
        if self.__area is None:
            self.__area_of_circle()
        return self.__area

    def set_radius(self,radius):
        self.__radius=radius
        self.__area=None
    def area_of_circle(self):
        self.__area =math.pi *(self.__radius ** 2)
        print(f"area of circle {self.__area}")

circle1=Circle(6)
circle1.area_of_circle()