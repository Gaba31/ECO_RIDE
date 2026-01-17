from src.models.vehicle import Vehicle

class ElectricCar(Vehicle):
    BASE_FARE = 5.0
    COST_PER_KM = 0.25
    def __init__(self,vehicle_id,model,battery_percentage,seating_capacity):
        super().__init__(vehicle_id,model,battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):

        if not isinstance(distance, (int, float)) or distance < 0:
            raise ValueError("Distance must be a positive number")


        return ElectricCar.BASE_FARE + (ElectricCar.COST_PER_KM * distance)

    def __str__(self):
        return (
            f"{self.__class__.__name__} | "
            f"ID: {self.vehicle_id} | "
            f"Model: {self.model} | "
            f"Battery: {self.battery_percentage}% | "
            f"Seats: {self.seating_capacity} | "
            f"Status: {self.maintenance_status} | "
            f"Fare: {self.rental_price}"
        )

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        data = super().to_dict()
        data["seating_capacity"] = self.seating_capacity
        return data
