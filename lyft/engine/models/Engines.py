from lyft.engine.Engine import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.current_mileage=current_mileage
        self.last_service_mileage=last_service_mileage
    def needs_service(self):
        return self.current_mileage-self.last_service_mileage>30000

class StrenmanEngine(Engine):
    def __init__(self, warning_light_is_on:bool):
        self.warning_light_is_on=warning_light_is_on
    def needs_service(self):
        return self.warning_light_is_on

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.current_mileage=current_mileage
        self.last_service_mileage=last_service_mileage
    def needs_service(self):
        return self.current_mileage-self.last_service_mileage>60000
