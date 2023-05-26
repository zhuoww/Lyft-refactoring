from abc import ABC
from engine.capulet_engine import CapuletEngine
from car import Car


class Engine(Car, ABC):
    def needs_service(self):
        pass