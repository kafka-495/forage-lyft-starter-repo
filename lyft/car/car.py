from lyft.servicable import Servicable
from lyft.engine.Engine import Engine
from lyft.battery.battery import Battery

class Car(Servicable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
