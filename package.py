from hash_table import HashTable


class Package:
    def __init__(self, package_id: int,
                 delivery_address : str,
                 delivery_city : str,
                 state : str,
                 delivery_zip: int,
                 package_weight : int,
                 notes : str,
                 delivery_status : str,
                 loading_time : str,
                 delivery_time : str):

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.state = state
        self.delivery_zip = delivery_zip
        self.package_weight = package_weight
        self.notes = notes
        self.delivery_status = delivery_status
        self.loading_time = loading_time
        self.delivery_time = delivery_time


    def __repr__(self):
        return ("package_id: {},"
                "delivery_address: {},"
                "delivery_city: {},"
                "state: {},"
                "delivery_zip: {},"
                "package_weight: {},"
                "notes: {},"
                "delivery_status: {},"
                "loading_time: {},"
                "delivery_time: {}".format(self.package_id, self.delivery_address, self.delivery_city, self.state, self.delivery_zip,
                                           self.package_weight, self.notes, self.delivery_status, self.loading_time, self.delivery_time))


    def __str__(self):
        return ("package_id: {},"
                "delivery_address: {},"
                "delivery_city: {},"
                "state: {},"
                "delivery_zip: {},"
                "package_weight: {},"
                "notes: {},"
                "delivery_status: {},"
                "loading_time: {},"
                "delivery_time: {}".format(self.package_id, self.delivery_address, self.delivery_city, self.state,
                                           self.delivery_zip,
                                           self.package_weight, self.notes, self.delivery_status, self.loading_time,
                                           self.delivery_time))

p1 = Package(1, "195 W Oakland Ave","Salt Lake City","UT",84115,
                   21 ,"", "delivered", "10:30 AM",  "2:20 PM")
p20 = Package(20, "123 Test Ave","SLC","KY",84115,
                   21 ,"", "delivered", "10:30 AM",  "2:20 PM")

my_table = HashTable()
my_table.insert(p1)
my_table.insert(p20)
print("Hash Table after insertions:")
print(my_table)
print("look-up: p1 ")
print(my_table.lookup(p1.package_id))
print("Look-up: p20 ")
print(my_table.lookup(p20.package_id))
my_table.remove(p20.package_id)

print("Hash Table after deletion(s): 20")
print(my_table)

my_table.remove(p1.package_id)
print("Hash Table after deletion(s): 1")
print(my_table)
my_table.remove(p20.package_id)

