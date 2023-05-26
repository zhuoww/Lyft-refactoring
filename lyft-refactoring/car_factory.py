from abc import ABC
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory(ABC):
    def __init__(self, currect_date, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_date = currect_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def create_calliope(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_glissade(self):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(self):
        engine = SternmanEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(self):
        engine = SternmanEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(self):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.current_date, self.last_service_date)
        car = Car(engine, battery)
        return car