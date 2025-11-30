from __future__ import annotations
from abc import ABC, abstractmethod

# ==========================
# 0.2.1 – Formes sans pattern
# ==========================

class Shape(ABC):
    @abstractmethod
    def draw(self) -> None:
        ...

    @abstractmethod
    def erase(self) -> None:
        ...


class Circle(Shape):
    def draw(self) -> None:
        print("Drawing a Circle")

    def erase(self) -> None:
        print("Erasing a Circle")


class Square(Shape):
    def draw(self) -> None:
        print("Drawing a Square")

    def erase(self) -> None:
        print("Erasing a Square")


class Triangle(Shape):
    def draw(self) -> None:
        print("Drawing a Triangle")

    def erase(self) -> None:
        print("Erasing a Triangle")


class Rectangle(Shape):
    def draw(self) -> None:
        print("Drawing a Rectangle")

    def erase(self) -> None:
        print("Erasing a Rectangle")


def demo_shapes_without_pattern() -> None:
    print("=== 0.2.1 – Shapes without pattern ===")
    shape_type_list = ["circle", "square", "triangle", "rectangle"]

    for shape_type in shape_type_list:
        if shape_type == "circle":
            shape: Shape = Circle()
        elif shape_type == "square":
            shape = Square()
        elif shape_type == "triangle":
            shape = Triangle()
        elif shape_type == "rectangle":
            shape = Rectangle()
        else:
            print(f"Unknown shape: {shape_type}")
            continue

        print(f"\nCreated shape -> {type(shape).__name__}")
        shape.draw()
        shape.erase()

    print("=" * 50, "\n")


# ==========================
# 0.2.2 – Simple Factory
# ==========================

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        s = shape_type.lower().strip()
        if s == "circle":
            return Circle()
        if s == "square":
            return Square()
        if s == "triangle":
            return Triangle()
        if s == "rectangle":
            return Rectangle()
        raise ValueError(f"Unknown shape type: {shape_type!r}")


def demo_shapes_simple_factory() -> None:
    print("=== 0.2.2 – Simple Shape Factory ===")
    shape_names = ["Circle", "Square", "Triangle", "Rectangle"]

    for name in shape_names:
        shape = ShapeFactory.create_shape(name)
        print(f"\nFactory created -> {type(shape).__name__}")
        shape.draw()
        shape.erase()

    print("=" * 50, "\n")

# ==========================
# Programme principal
# ==========================

def main() -> None:
    demo_shapes_without_pattern()
    demo_shapes_simple_factory()


if __name__ == "__main__":
    main()
