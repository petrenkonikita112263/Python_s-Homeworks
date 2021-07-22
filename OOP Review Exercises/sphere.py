import math

"""
Exercise 1
Create a Sphere class that accepts a radius upon instantiation and has a volume and surface area method.
"""


class Sphere:
    # Create the methods here!
    def __init__(self, radius: int) -> None:
        self.radius = radius
        self.area_value = 0.0
        self.volume_value = 0.0

    def surface_area(self) -> None:
        self.area_value = 4 * math.pi * self.radius ** 2

    def volume(self) -> None:
        self.volume_value = (4 / 3) * math.pi * self.radius ** 3

    def __str__(self) -> str:
        return f"The sphere with radius = {self.radius} have surface area = {self.area_value}" \
               f" and volume = {self.volume_value}"
