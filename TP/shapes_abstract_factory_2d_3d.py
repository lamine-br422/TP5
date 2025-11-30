#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
    @abstractmethod
    def erase(self):
        pass

class Circle2D(Shape):
    def draw(self):
        print("Circle.draw2D")
    def erase(self):
        print("Circle.erase2D")

class Square2D(Shape):
    def draw(self):
        print("Square.draw2D")
    def erase(self):
        print("Square.erase2D")

class Circle3D(Shape):
    def draw(self):
        print("Circle.draw3D")
    def erase(self):
        print("Circle.erase3D")

class Square3D(Shape):
    def draw(self):
        print("Square.draw3D")
    def erase(self):
        print("Square.erase3D")

class ShapeFactory(ABC):
    @staticmethod
    @abstractmethod
    def createShape(type):
        pass

class ShapeFactory2D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle":
            return Circle2D()
        elif type == "Square":
            return Square2D()
        else:
            return None

class ShapeFactory3D(ShapeFactory):
    @staticmethod
    def createShape(type):
        if type == "Circle":
            return Circle3D()
        elif type == "Square":
            return Square3D()
        else:
            return None


if __name__ == "__main__":
    for t in ("Circle", "Square", "Circle", "Square"):
        shape = ShapeFactory2D.createShape(t)
        shape.draw()
        shape.erase()

    for t in ("Circle", "Square", "Circle", "Square"):
        shape = ShapeFactory3D.createShape(t)
        shape.draw()
        shape.erase()
