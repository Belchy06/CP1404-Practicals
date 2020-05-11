"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_08.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that is unreliable."""

    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable Car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only if random value is less than the reliability."""
        if random.randint(0,100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
