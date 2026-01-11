from collections import defaultdict

from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter
from src.models.vehicle import Vehicle


class HubManager:
    def __init__(self):
        self.hubs = {}

    def add_hub(self,hub):
        if hub.hub_name in self.hubs:
            print("Hub Already Exists")
        else:
            self.hubs[hub.hub_name] = hub
            print("hub Added Successfully")

    def update_hub(self,hub):
        self.hubs[hub.hub_name] = hub
        print("hub Updated Successfully")

    def get_hub(self,hub_name):
        return self.hubs.get(hub_name)

    def hub_exists(self,hub_name):
        if hub_name in self.hubs:
            return True
        return False

    def get_all_hubs(self):
        for hub_name, hub_obj in self.hubs.items():
            print(f"{hub_name} : {hub_obj.vehicle_list}")

    def search_by_hub(self,hub_name):
        hub_obj = self.hubs.get(hub_name)
        if hub_obj is None:
            print("hub Not Found")
            return

        if not  hub_obj.vehicle_list:
            print("No vehicles in this list")
            return

        print(f"Vehicles in hub {hub_name}:")
        for vehicle in hub_obj.vehicle_list:
            print(vehicle)

    def search_vehicle_by_battery_percentage(self,given_battery_percentage=80):
        print(f"Vehicles with battery > {given_battery_percentage}%:")

        found = False
        for hub in self.hubs.values():
            high_battery_vehicles = list(
                filter(lambda v: v.battery_percentage > given_battery_percentage, hub.vehicle_list)
            )

            if high_battery_vehicles:
                found = True
                print(f"{hub.hub_name} : {high_battery_vehicles}")

        if found == False:
            print("No vehicles found with battery above threshold")


    def vehicle_category(self):

        category_dict = defaultdict(list)
        for hub_obj in self.hubs.values():
            for v in hub_obj.vehicle_list:
                if isinstance(v, ElectricCar):
                    category_dict["Electric Car"].append(v)

                elif isinstance(v, ElectricScooter):
                    category_dict["Electric Scooter"].append(v)

        return dict(category_dict)