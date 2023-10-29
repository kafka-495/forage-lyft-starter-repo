from lyft.servicable import Servicable
from lyft.engine.Engine import Engine
from lyft.battery.battery import Battery
from lyft.tire.tires import Tire

class Car(Servicable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire=tire

    def needs_service(self) -> bool:
        print(self.tire.needs_service())
        return self.engine.needs_service() or self.battery.needs_service()
