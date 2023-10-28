from lyft.car_factory import CarFactory as cf
from datetime import datetime
from lyft.battery.models.Batteries import SpindlerBattery, NubbinBattery
from lyft.engine.models.Engines import *
from lyft.car.car import Car

def main():
    today = datetime.today().date()
    last_service_date = today.replace(year=today.year - 3)
    current_mileage = 0
    last_service_mileage = 0
    thovex = cf.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
    print( thovex.needs_service())
if __name__ == '__main__':
    main()
