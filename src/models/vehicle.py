from abc import ABC, abstractmethod

class Vehicle(ABC):

        def __init__(self, vehicle_id, model, b_percentage):
            self.vehicle_id = vehicle_id
            self.model = model
            self.battery_percentage = b_percentage