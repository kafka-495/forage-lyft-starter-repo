from lyft.tire.tires import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array=tire_array
    def needs_service(self)->bool:
        condition=[a>=0.9 for a in self.tire_array]
        return (sum(condition)>=1)


class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.tire_array=tire_array
        #print("OctoprimeTire")
    def needs_service(self)->bool:
        return (sum(self.tire_array)>=3)
