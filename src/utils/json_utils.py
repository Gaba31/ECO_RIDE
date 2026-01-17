import json
import os

from src.fleet.hub import Hub
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter



BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_FILE = os.path.join(BASE_DIR, "data", "data.json")


def save_to_json(hub_manager):
    # Ensure data folder exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    data = {
        hub_name: [v.to_dict() for v in hub.vehicle_list]
        for hub_name, hub in hub_manager.hubs.items()
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Fleet saved to JSON at: {DATA_FILE}")


def load_from_json(hub_manager):
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        for hub_name, vehicles in data.items():
            hub = Hub(hub_name)

            for v in vehicles:
                if v["type"] == "ElectricCar":
                    obj = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["seating_capacity"]
                    )

                elif v["type"] == "ElectricScooter":
                    obj = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery_percentage"],
                        v["max_speed_limit"]
                    )

                else:
                    continue

                obj.maintenance_status = v["maintenance_status"]
                obj.rental_price = v["rental_price"]
                hub.add_vehicle(obj)

            hub_manager.add_hub(hub)

        print("Fleet data loaded from JSON successfully")

    except FileNotFoundError:
        print("No JSON data found. Starting fresh.")
