from datetime import datetime, timedelta, time

import package


class Truck:

    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.unused_capacity = 16
        self.contents = []
        self.current_location = "HUB"
        self.distance_traveled = 0
        self.min_distance_to_nearest_location = 0
        self.time = time(hour=8)

    def add_package(self, package):
        """checks truck for unused capacity, adds package, and updates truck's unused capacity"""
        if self.unused_capacity > 0:
            self.contents.append(package)
            self.unused_capacity -= 1

    def list_contents(self):
        """for testing, prints all packages on a truck"""
        for package in self.contents:
            print(package)

    def return_to_hub(self, distance_to_hub, time_spent, manifest):
        self.current_location = "HUB"
        self.distance_traveled += distance_to_hub
        delta = timedelta(minutes=time_spent)
        self.time = (datetime.combine(datetime.today(), self.time) + delta).time()
        self.contents.append(manifest.lookup(6))


    def log_delivery(self,time_delivered,distance,new_location):
        """update current time, distance_traveled, unused capacity(returns how much capacity remains in truck), and current location
        https://docs.python.org/3/library/datetime.html#time-objects
        use datetime.combine to convert self.time to a datetime obj
        add delta
        convert back to time obj
        """
        delta = timedelta(minutes=time_delivered)
        self.time = (datetime.combine(datetime.today(),self.time) + delta).time()
        self.distance_traveled += distance
        self.unused_capacity += 1
        self.current_location = new_location



    def __repr__(self):
        return ("truck_number: {}, \n"
                "unused_capacity: {}, \n"
                "contents={}, \n" 
                "current_location={}, \n"
                "distance_traveled={}, \n" 
                "min_distance_to_nearest_location={}, \n"
                " time={}".format(self.truck_number, self.unused_capacity, self.contents,self.current_location,
                                        self.distance_traveled,self.min_distance_to_nearest_location,self.time))
    def __str__(self):
        return ("truck_number: {}, \n"
                "unused_capacity: {}, \n"
                "contents={}, \n" 
                "current_location={}, \n"
                "distance_traveled={}, \n" 
                "min_distance_to_nearest_location={}, \n"
                " time={}".format(self.truck_number, self.unused_capacity, self.contents,self.current_location,
                                        self.distance_traveled,self.min_distance_to_nearest_location,self.time))