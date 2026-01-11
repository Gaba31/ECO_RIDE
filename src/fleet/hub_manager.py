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