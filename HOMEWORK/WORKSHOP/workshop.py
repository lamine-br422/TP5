from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

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

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        shape_type = shape_type.lower().strip()
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        if shape_type == "triangle":
            return Triangle()
        if shape_type == "rectangle":
            return Rectangle()
        raise ValueError(f"Unknown shape type: {shape_type!r}")

def factory_demo() -> None:
    print("=== Factory pattern ===")
    shape_names = ["Circle", "Square", "Triangle", "Rectangle"]
    for name in shape_names:
        shape = ShapeFactory.create_shape(name)
        print(f"\nCreated {name} ->", type(shape).__name__)
        shape.draw()
        shape.erase()
    print("=" * 50, "\n")

@dataclass
class Car:
    brand: str
    model: str
    engine: str
    has_gps: bool = False
    has_air_conditioning: bool = False
    has_sunroof: bool = False
    has_leather_seats: bool = False

    def __str__(self) -> str:
        options = []
        if self.has_gps:
            options.append("GPS")
        if self.has_air_conditioning:
            options.append("AC")
        if self.has_sunroof:
            options.append("Sunroof")
        if self.has_leather_seats:
            options.append("Leather seats")
        options_str = ", ".join(options) if options else "no extra options"
        return f"{self.brand} {self.model} ({self.engine}) with {options_str}"

class CarBuilder(ABC):
    def __init__(self) -> None:
        self._brand: str = ""
        self._model: str = ""
        self._engine: str = ""
        self._has_gps: bool = False
        self._has_air_conditioning: bool = False
        self._has_sunroof: bool = False
        self._has_leather_seats: bool = False

    def reset(self) -> None:
        self.__init__()

    def set_brand(self, brand: str) -> None:
        self._brand = brand

    def set_model(self, model: str) -> None:
        self._model = model

    def set_engine(self, engine: str) -> None:
        self._engine = engine

    def enable_gps(self) -> None:
        self._has_gps = True

    def enable_air_conditioning(self) -> None:
        self._has_air_conditioning = True

    def enable_sunroof(self) -> None:
        self._has_sunroof = True

    def enable_leather_seats(self) -> None:
        self._has_leather_seats = True

    @abstractmethod
    def build(self) -> Car:
        ...

class BasicCarBuilder(CarBuilder):
    def build(self) -> Car:
        car = Car(
            brand=self._brand,
            model=self._model,
            engine=self._engine,
            has_gps=self._has_gps,
            has_air_conditioning=self._has_air_conditioning,
            has_sunroof=self._has_sunroof,
            has_leather_seats=self._has_leather_seats,
        )
        self.reset()
        return car

class FullOptionCarBuilder(CarBuilder):
    def build_full_options(self) -> None:
        self.enable_gps()
        self.enable_air_conditioning()
        self.enable_sunroof()
        self.enable_leather_seats()

    def build(self) -> Car:
        self.build_full_options()
        car = Car(
            brand=self._brand,
            model=self._model,
            engine=self._engine,
            has_gps=self._has_gps,
            has_air_conditioning=self._has_air_conditioning,
            has_sunroof=self._has_sunroof,
            has_leather_seats=self._has_leather_seats,
        )
        self.reset()
        return car

class CarOrderDirector:
    def __init__(self, builder: CarBuilder) -> None:
        self._builder = builder

    def build_basic_order(self, brand: str, model: str) -> Car:
        self._builder.reset()
        self._builder.set_brand(brand)
        self._builder.set_model(model)
        self._builder.set_engine("1.4L petrol")
        return self._builder.build()

    def build_full_order(self, brand: str, model: str) -> Car:
        self._builder.reset()
        self._builder.set_brand(brand)
        self._builder.set_model(model)
        self._builder.set_engine("2.0L turbo")
        return self._builder.build()

    def build_custom_order(
        self,
        brand: str,
        model: str,
        engine: str,
        gps: bool = False,
        ac: bool = False,
        sunroof: bool = False,
        leather: bool = False,
    ) -> Car:
        self._builder.reset()
        self._builder.set_brand(brand)
        self._builder.set_model(model)
        self._builder.set_engine(engine)
        if gps:
            self._builder.enable_gps()
        if ac:
            self._builder.enable_air_conditioning()
        if sunroof:
            self._builder.enable_sunroof()
        if leather:
            self._builder.enable_leather_seats()
        return self._builder.build()

def builder_demo() -> None:
    print("=== Builder pattern ===")
    basic_builder = BasicCarBuilder()
    director = CarOrderDirector(basic_builder)
    car1 = director.build_basic_order("Toyota", "Corolla")
    print("Basic order ->", car1)
    full_builder = FullOptionCarBuilder()
    director = CarOrderDirector(full_builder)
    car2 = director.build_full_order("BMW", "X5")
    print("Full options order ->", car2)
    custom_builder = BasicCarBuilder()
    director = CarOrderDirector(custom_builder)
    car3 = director.build_custom_order(
        brand="Renault",
        model="Clio",
        engine="1.5L diesel",
        gps=True,
        ac=True,
        sunroof=False,
        leather=True,
    )
    print("Custom order ->", car3)
    print("=" * 50, "\n")

def main() -> None:
    factory_demo()
    builder_demo()

if __name__ == "__main__":
    main()
