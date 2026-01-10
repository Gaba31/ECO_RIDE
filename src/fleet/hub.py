class Hub:
    def __init__(self,hub_name):
        self.__hub_name = hub_name
        self.vehicle_list = []

    def add_vehicle(self,vehicle):
        self.vehicle_list.append(vehicle)