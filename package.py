

class Package:
    def __init__(self, package_id: int,
                 delivery_address : str,
                 delivery_city : str,
                 delivery_zip: int,
                 delivery_deadline: str,
                 package_weight : int,
                 notes : str,
                 delivery_status : str,
                 loading_time : str,
                 delivery_time : str,
                 truck_number : int):

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_deadline = delivery_deadline
        self.delivery_zip = delivery_zip
        self.package_weight = package_weight
        self.notes = notes
        self.delivery_status = delivery_status
        self.loading_time = loading_time
        self.delivery_time = delivery_time
        self.truck_number = truck_number

    def deliver_package(self,time):
        self.delivery_status = "delivered"
        self.delivery_time = time


    def __repr__(self):
        return ("package_id: {},"
                "delivery_address: {},"
                "delivery_city: {},"
                "delivery_zip: {},"
                "delivery_deadline: {},\n"
                "package_weight: {},"
                "notes: {},"
                "delivery_status: {},"
                "loading_time: {},"
                "delivery_time: {}"
                "truck_number: {}\n".format(self.package_id, self.delivery_address, self.delivery_city, self.delivery_zip,
                                           self.delivery_deadline, self.package_weight, self.notes, self.delivery_status,
                                           self.loading_time, self.delivery_time, self.truck_number))


    def __str__(self):
        return ("package_id: {},"
                "delivery_address: {},"
                "delivery_city: {},"
                "delivery_zip: {},"
                "delivery_deadline: {},\n"
                "package_weight: {},"
                "notes: {},"
                "delivery_status: {},"
                "loading_time: {},"
                "delivery_time: {}"
                "truck_number: {}\n".format(self.package_id, self.delivery_address, self.delivery_city, self.delivery_zip,
                                           self.delivery_deadline, self.package_weight, self.notes, self.delivery_status,
                                           self.loading_time, self.delivery_time, self.truck_number))