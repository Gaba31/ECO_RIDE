class Hub:
    def __init__(self,hub_name):
        self.hub_name = hub_name
        self.vehicle_list = []

    def add_vehicle(self,vehicle):
        # Used for duplicate checking
        if vehicle in self.vehicle_list:
            print(f"Vehicle with ID {vehicle.vehicle_id} already exists in hub {self.hub_name}")
            return
        self.vehicle_list.append(vehicle)
        print("Vehicle added successfully")