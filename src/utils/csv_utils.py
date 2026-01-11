import csv
import os

from src.fleet.hub import Hub
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter

# ---------------- PATH SETUP ----------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "vehicles.csv")

FIELDNAMES = [
    "hub_name",
    "vehicle_type",
    "vehicle_id",
    "model",
    "battery",
    "status",
    "rental_price",
    "extra"
]

# ---------------- SAVE VEHICLE ----------------

def save_vehicle_to_csv(hub_name, vehicle):
    file_exists = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "hub_name": hub_name,
            "vehicle_type": vehicle.__class__.__name__,
            "vehicle_id": vehicle.vehicle_id,
            "model": vehicle.model,
            "battery": vehicle.battery_percentage,
            "status": vehicle.maintenance_status,
            "rental_price": vehicle.rental_price,
            "extra": getattr(
                vehicle,
                "seating_capacity",
                getattr(vehicle, "max_speed_limit", "")
            )
        })

# ---------------- LOAD VEHICLES ----------------

def load_vehicles_from_csv(hub_manager):
    if not os.path.exists(DATA_FILE):
        return  # First run, nothing to load

    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            hub_name = row["hub_name"]

            # Create hub if missing
            if not hub_manager.hub_exists(hub_name):
                hub_manager.add_hub(Hub(hub_name))

            hub = hub_manager.get_hub(hub_name)

            # Create correct vehicle type
            if row["vehicle_type"] == "ElectricCar":
                vehicle = ElectricCar(
                    row["vehicle_id"],
                    row["model"],
                    int(row["battery"]),
                    int(row["extra"])
                )
            else:
                vehicle = ElectricScooter(
                    row["vehicle_id"],
                    row["model"],
                    int(row["battery"]),
                    int(row["extra"])
                )

            vehicle.maintenance_status = row["status"]
            vehicle.rental_price = float(row["rental_price"])

            hub.add_vehicle(vehicle)
