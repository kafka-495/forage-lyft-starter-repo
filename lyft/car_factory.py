from lyft.battery.models.Batteries import SpindlerBattery, NubbinBattery
from lyft.engine.models.Engines import *
from lyft.tire.models.Tires import *
from lyft.car.car import Car
class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_array) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_array))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_array) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_array))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on: bool, tire_array) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_array) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_array))

    def needs_service(self):
        pass

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage: int, last_service_mileage: int, tire_array) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), CarriganTire(tire_array))
