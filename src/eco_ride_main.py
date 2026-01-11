from src.fleet.hub import Hub
from src.fleet.hub_manager import HubManager
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter
from src.utils.csv_utils import load_vehicles_from_csv, save_vehicle_to_csv



class EcoRideMain:
    @staticmethod
    def welcome():
        print("Welcome to Eco-Ride Urban Mobility System")
        print(("-"*40))

    @staticmethod
    def add_vehicle_console_comp(hub_manager):
        print("Select vehicle")
        print(("-"*40))
        print("\t 1. Add Electric Car")
        print("\t 2. Add Electric Scooter")
        print("\t 0. Return")
        ch = input()

        if ch == "0":
            return
        elif  ch == "1":
            vehicle_id = input("Enter vehicle ID:\n")
            model = input("Enter model:\n")
            battery_percentage = int(input("Enter battery percentage:\n"))
            seating_capacity = input("Enter seating capacity:\n")
            m_status = EcoRideMain.add_maintenance_status()
            rental_price = float(input("Enter rental price per trip:\n"))
            ecar_obj = ElectricCar(vehicle_id,model,battery_percentage,seating_capacity)
            ecar_obj.maintenance_status = m_status
            ecar_obj.rental_price = rental_price

            hub_name = input("Enter hub Name for the Vehicle:\n")

            if hub_manager.hub_exists(hub_name):
               hub_obj =  hub_manager.get_hub(hub_name)
               hub_obj.add_vehicle(ecar_obj)
               #print(type(hub_obj))
               hub_manager.update_hub(hub_obj)
               save_vehicle_to_csv(hub_name, ecar_obj)

            else:
                hub_obj = Hub(hub_name)
                hub_obj.add_vehicle(ecar_obj)
                #print(type(hub_obj))
                hub_manager.update_hub(hub_obj)


        elif ch == "2":
            vehicle_id = input("Enter vehicle ID:\n")
            model = input("Enter model:\n")
            battery_percentage = int(input("Enter battery percentage:\n"))
            max_speed_limit = input("Enter max_speed_limit:\n")
            m_status = EcoRideMain.add_maintenance_status()
            rental_price = float(input("Enter rental price per trip:\n"))
            escooter_obj = ElectricScooter(vehicle_id,model,battery_percentage,max_speed_limit)
            escooter_obj.maintenance_status = m_status
            escooter_obj.rental_price = rental_price

            hub_name = input("Enter hub Name for the Vehicle:\n")

            if hub_manager.hub_exists(hub_name):
                hub_obj = hub_manager.get_hub(hub_name)
                hub_obj.add_vehicle(escooter_obj)
                #print(type(hub_obj))
                hub_manager.update_hub(hub_obj)
                save_vehicle_to_csv(hub_name, escooter_obj)

            else:
                hub_obj =  Hub(hub_name)
                hub_obj.add_vehicle(escooter_obj)
                #print(type(hub_obj))
                hub_manager.update_hub(hub_obj)

    @staticmethod
    def add_maintenance_status():
        print("Select Vehicle Status")
        print("-" * 40)
        print("\t 1. Available")
        print("\t 2. On Trip")
        print("\t 3. Under Maintenance")

        choice = input("Enter choice: ")

        if choice == "1":
            return "Available"
        elif choice == "2":
            return "On Trip"
        elif choice == "3":
            return "Under Maintenance"
        else:
            print("Invalid choice, defaulting to Available")
            return "Available"

    @staticmethod
    def categorized_view(hub_manager):
        categorized = hub_manager.vehicle_category()

        if not categorized:
            print("No vehicle available")
        else:
            for v_type , vehicles in categorized.items():
                print(f"\n{v_type} Vehicles")
                print("=" * 40)
                for v in vehicles:
                    print(v)

    @staticmethod
    def console_logic(hub_manager):
        flag = True
        while flag:
            print("Select operation")
            print(("-" * 40))
            print("\t 1. Add hub")
            print("\t 2. view hubs")
            print("\t 3. Add vehicle")
            print("\t 4. Search vehicle by hub")
            print("\t 5. Search vehicle by battery percentage")
            print("\t 6. Categorize vehicle")
            print("\t 7. Vehicle by status category")
            print("\t 8. Sort vehicles in hub by model name")
            print("\t 9. Advanced sort (battery / fare)")
            print("\t 0. Exit")
            choice = input()

            if choice == "0":
                flag = False

            elif choice == "1":
                hub_name = input("Enter hub Name:\n")
                hub_obj = Hub(hub_name)
                hub_manager.add_hub(hub_obj)
            elif choice == "2":
                hub_manager.get_all_hubs()
            elif choice == "3":
              EcoRideMain.add_vehicle_console_comp(hub_manager)
            elif choice == "4":
                hub_name = input("Enter hub name:\n")
                hub_manager.search_by_hub(hub_name)
            elif choice == "5":
                battery_percentage = int(input("Enter battery percentage:\n"))
                hub_manager.search_vehicle_by_battery_percentage(battery_percentage)
            elif choice == "6":
                EcoRideMain.categorized_view(hub_manager)
            elif choice == "7":
                status_count = hub_manager.vehicle_count_by_status()

                print("\nFleet Analytics Summary")
                print("=" * 40)

                print(f"Available Vehicles        : {status_count.get('Available', 0)}")
                print(f"Vehicles On Trip          : {status_count.get('On Trip', 0)}")
                print(f"Under Maintenance Vehicles: {status_count.get('Under Maintenance', 0)}")

            elif choice == "8":
                hub_name = input("Enter hub name:\n")
                sorted_vehicles = hub_manager.get_sorted_vehicles_by_model(hub_name)
                if not sorted_vehicles:
                    print("No vehicles to display")
                else:
                    print(f"\nVehicles in '{hub_name}' sorted by model")
                    print("=" * 40)
                    for v in sorted_vehicles:
                        print(v)

            elif choice == "9":
                hub_name = input("Enter hub name:\n")

                print("Sort By:")
                print("1. Battery Level (High to Low)")
                print("2. Fare Price (High to Low)")
                sort_choice = input("Enter choice: ")

                if sort_choice == "1":
                    sorted_vehicles = hub_manager.sort_vehicles_adv(hub_name, "battery")
                elif sort_choice == "2":
                    sorted_vehicles = hub_manager.sort_vehicles_adv(hub_name, "fare")
                else:
                    print("Invalid choice")
                    continue

                if not sorted_vehicles:
                    print("No vehicles to display")
                else:
                    print("\nSorted Vehicles")
                    print("=" * 40)
                    for v in sorted_vehicles:
                        print(v)


if __name__ == "__main__":
    EcoRideMain.welcome()
    hub_manager = HubManager()
    load_vehicles_from_csv(hub_manager)
    EcoRideMain.console_logic(hub_manager)

