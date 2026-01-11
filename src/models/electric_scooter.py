from src.models.vehicle import Vehicle

class ElectricScooter(Vehicle):
    BASE_FARE = 1.0
    COST_PER_MINUTE = 0.15
    def __init__(self,vehicle_id,model,battery_percentage,max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, minutes):

        if not isinstance(minutes, (int, float)) or minutes < 0:
            raise ValueError("Minutes must be a positive number")


        return ElectricScooter.BASE_FARE + (ElectricScooter.COST_PER_MINUTE * minutes)

    def __str__(self):
        return (
            f"{self.__class__.__name__} | "
            f"ID: {self.vehicle_id} | "
            f"Model: {self.model} | "
            f"Battery: {self.battery_percentage}% | "
            f"Max Speed: {self.max_speed_limit} | "
            f"Status: {self.maintenance_status} | "
            f"Fare: {self.rental_price}"
        )
    def __repr__(self):
        return self.__str__()

