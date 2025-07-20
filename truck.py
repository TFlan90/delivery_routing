import datetime

class Truck:

    def __init__(self, truck_number):
        self.truck_number = truck_number
        self.unused_capacity = 16
        self.contents = []
        self.current_location = 0
        self.distance_traveled = 0
        self.min_distance_to_nearest_location = 0
        self.time = datetime.time(8,0,0)

    def add_package(self, package):
        if self.unused_capacity > 0:
            self.contents.append(package)
            self.unused_capacity -= 1
    def list_contents(self):
        for package in self.contents:
            print(package)


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