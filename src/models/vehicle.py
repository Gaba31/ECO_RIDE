from abc import ABC, abstractmethod

class Vehicle(ABC):

        def __init__(self, vehicle_id, model, battery_percentage):
            self.vehicle_id = vehicle_id
            self.model = model
            self.battery_percentage = battery_percentage
            self.__maintenance_status = None
            self.__rental_price = None

            @property
            def maintenance_status(self):
                """
                :return:  This will return maintenance status of the vehicle.
                """
                return self.__maintenance_status

            @maintenance_status.setter
            def maintenance_status(self,maintenance_status):
                """

                :param self:
                :param maintenance_status:
                :return: This will set maintenance status of the vehicle.
                """
                self.__maintenance_status = maintenance_status

            @property
            def rental_price(self):
                """
                    This will return rental status of the vehicle.
                """
                return self.__rental_price

            @rental_price.setter
            def rental_price(self, price):
                """
                    Sets the rental price of the vehicle

                    Parameter
                    ---------
                    price : int
                        Rental price value

                    Raises
                        ValueError
                            If the rental price is less than 0
                """
                if isinstance(price, (int, float)) and price >= 0:
                    self.__rental_price = int(price)
                else:
                    raise ValueError("Rental price cannot be negative")

            @property
            def battery_percentage(self):
                """
                :return: This will return battery percentage of the vehicle
                """
                return self.battery_percentage

            @battery_percentage.setter
            def battery_percentage(self, battery_percentage):
                """
                      Sets the battery percentage of the vehicle.

                      Parameters
                      ----------
                      battery_percentage : int
                          Battery percentage value

                      Raises
                      ------
                      ValueError
                          If battery percentage is out of range
                      """
                if isinstance(battery_percentage, (int, float)) and (
                        battery_percentage >= 0 and battery_percentage <= 100):
                    self.battery_percentage = int(battery_percentage)
                else:
                    raise ValueError("Battery Percentage must be between 0 and 100")


