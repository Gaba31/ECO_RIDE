from src.fleet.hub import Hub
from src.fleet.hub_manager import HubManager
from src.models.electric_car import ElectricCar
from src.models.electric_scooter import ElectricScooter


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
            ecar_obj = ElectricCar(vehicle_id,model,battery_percentage,seating_capacity)

            hub_name = input("Enter hub Name for the Vehicle:\n")

            if hub_manager.hub_exists(hub_name):
               hub_obj =  hub_manager.get_hub(hub_name)
               hub_obj.add_vehicle(ecar_obj)
               #print(type(hub_obj))
               hub_manager.update_hub(hub_obj)
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
            escooter_obj = ElectricScooter(vehicle_id,model,battery_percentage,max_speed_limit)

            hub_name = input("Enter hub Name for the Vehicle:\n")

            if hub_manager.hub_exists(hub_name):
                hub_obj = hub_manager.get_hub(hub_name)
                hub_obj.add_vehicle(escooter_obj)
                #print(type(hub_obj))
                hub_manager.update_hub(hub_obj)
            else:
                hub_obj =  Hub(hub_name)
                hub_obj.add_vehicle(escooter_obj)
                #print(type(hub_obj))
                hub_manager.update_hub(hub_obj)

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





if __name__ == "__main__":
    EcoRideMain.welcome()
    hub_manager = HubManager()
    EcoRideMain.console_logic(hub_manager)

