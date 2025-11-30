#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add(self, item):
        self.ingredients.append(item)

    def show(self):
        print("Sandwich:", ", ".join(self.ingredients))


class SandwichBuilder:
    def __init__(self):
        self.sandwich = Sandwich()

    def add_bread(self):
        self.sandwich.add("Bread")

    def add_meat(self):
        self.sandwich.add("Meat")

    def add_ground_meat(self):
        self.sandwich.add("Ground meat")

    def add_omelet(self):
        self.sandwich.add("Omelet")

    def add_fries(self):
        self.sandwich.add("Fries")

    def add_salad(self):
        self.sandwich.add("Salad")

    def add_sauce(self):
        self.sandwich.add("Sauce")


class SandwichDirector:
    def construct(self, builder):
        self.builder = builder

    def shawarma_sandwich(self):
        self.builder.sandwich = Sandwich()
        self.builder.add_bread()
        self.builder.add_meat()
        self.builder.add_salad()
        self.builder.add_fries()
        self.builder.add_sauce()

    def ground_meat_sandwich(self):
        self.builder.sandwich = Sandwich()
        self.builder.add_bread()
        self.builder.add_ground_meat()
        self.builder.add_salad()
        self.builder.add_sauce()

    def fried_with_omelet_sandwich(self):
        self.builder.sandwich = Sandwich()
        self.builder.add_bread()
        self.builder.add_omelet()
        self.builder.add_fries()
        self.builder.add_sauce()


class Car:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Car:", ", ".join(self.parts))


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def add_chassis(self):
        self.car.add("Chassis")

    def add_engine(self):
        self.car.add("Engine")

    def add_wheels(self):
        self.car.add("Wheels")

    def add_air_conditioning(self):
        self.car.add("Air conditioning")

    def add_gps(self):
        self.car.add("GPS")

    def add_sunroof(self):
        self.car.add("Sunroof")


class CarDirector:
    def construct(self, builder):
        self.builder = builder

    def basic_car(self):
        self.builder.car = Car()
        self.builder.add_chassis()
        self.builder.add_engine()
        self.builder.add_wheels()

    def full_car(self):
        self.builder.car = Car()
        self.builder.add_chassis()
        self.builder.add_engine()
        self.builder.add_wheels()
        self.builder.add_air_conditioning()
        self.builder.add_gps()
        self.builder.add_sunroof()

    def car_with_some_options(self):
        self.builder.car = Car()
        self.builder.add_chassis()
        self.builder.add_engine()
        self.builder.add_wheels()
        self.builder.add_air_conditioning()
        self.builder.add_gps()


def main():
    s_builder = SandwichBuilder()
    s_director = SandwichDirector()
    s_director.construct(s_builder)

    s_director.shawarma_sandwich()
    sandwich = s_builder.sandwich
    sandwich.show()

    s_director.ground_meat_sandwich()
    sandwich = s_builder.sandwich
    sandwich.show()

    s_director.fried_with_omelet_sandwich()
    sandwich = s_builder.sandwich
    sandwich.show()

    c_builder = CarBuilder()
    c_director = CarDirector()
    c_director.construct(c_builder)

    c_director.basic_car()
    car = c_builder.car
    car.show()

    c_director.full_car()
    car = c_builder.car
    car.show()

    c_director.car_with_some_options()
    car = c_builder.car
    car.show()


if __name__ == "__main__":
    main()
