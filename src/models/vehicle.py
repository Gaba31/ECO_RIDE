from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = None
        self.__rental_price = None

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, price):
        if isinstance(price, (int, float)) and price >= 0:
            self.__rental_price = int(price)
        else:
            raise ValueError("Rental price cannot be negative")

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, battery_percentage):
        if isinstance(battery_percentage, (int, float)) and 0 <= battery_percentage <= 100:
            self.__battery_percentage = int(battery_percentage)
        else:
            raise ValueError("Battery Percentage must be between 0 and 100")

    @abstractmethod
    def calculate_trip_cost(self,usage):
        pass

    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.vehicle_id == other.vehicle_id
        return False
