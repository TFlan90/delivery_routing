from hash_table import HashTable
from package import Package
import csv
from truck import Truck
import datetime
def build_delivery_manifest(filename):
    """
    build manifest(hash_table) from csv file of packages
    input: csv file of packages
    output: manifest(hash_table) of packages that uses package ID as key
    """
    manifest = HashTable()
    # https://stackoverflow.com/questions/52400408/import-csv-file-into-python
    with open(filename, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            package = Package(int(row[0]), row[1], row[2], int(row[4]), row[5], int(row[6]), row[7], "At the hub",
                              None, "TBD", None)
            manifest.insert(package)
    return manifest


def load_distance_data(filename):
    """"
    parses an adjacency matrix of address distances from a csv file
    input: csv file of distances
    output: 2d list of address distances, dictionary containing address:index pairs that are used as access points for the 2d list
    """
    adjacency_matrix = []
    address_key = {}

    with open(filename, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for i,row in enumerate(reader):
            address = row.pop(0)
            address_key[address] = i
            adjacency_matrix.append(row)
    return adjacency_matrix,address_key

def load_truck(manifest, truck1 : Truck, truck2 : Truck, truck3 : Truck):
    """
    Load truck with packages using the manifest
    input: manifest : Custom hash table of packages
    out: 3 truck objs loaded with <= 16 packages

    Algorithm logic: sort packages into candidate lists using notes for trucks 2 and 3
    everything else goes into candidate list 1
    package 6 is skipped and loaded after it arrives to the hub
    when a package is loaded on a truck, it's considered "in transit"
    truck2_candidates -> truck2 -> overflow goes to truck1_candidates
    everything in truck3_candidates -> truck3
    truck1_candidates -> 16 packages(truck obj capacity) ->  truck1
    Overflow goes to truck 2 until it's full and the remainer goes on truck 3

    """
    truck1_candidates = []
    truck2_candidates = []
    truck3_candidates = []

    #create candidate lists for the 3 trucks (packages that could be potentially loaded on a given truck)
    for i in range(1,41):
        package = manifest.lookup(i)
        if "Can only be on truck 2" in package.notes or "Must be delivered with" in package.notes:
            truck2_candidates.append(package)
        #skip loading package 6, truck 1 will return to the hub sometime after it arrives at 9:05
        elif i == 6:
            continue
        elif "will arrive" in package.notes:
            package.delivery_status = "DELAYED"
            truck3_candidates.append(package)
        elif "Wrong address" in package.notes:
            truck3_candidates.append(package)
        else:
            truck1_candidates.append(package)
    #load truck two, overflow is added to truck 1 candidate list
    for i in range(len(truck2_candidates)):
        if truck2.unused_capacity > 0:
            truck2_candidates[i].loading_time = truck2.time
            truck2.add_package(truck2_candidates[i])
        else:
           truck1_candidates.append(truck2_candidates[i])
    #load truck 3
    for i in range(len(truck3_candidates)):
        if "will arrive" not in truck3_candidates[i].notes:
            truck3_candidates[i].loading_time = truck3.time
            truck3.add_package(truck3_candidates[i])
        else:
            #used to extract delayed packages loading time
            #extracted delivery time will be cast to a datetime.time obj and passed to the package
            #if a package can't be loaded until a certain time, update truck.time to whatever is larger, the trucks current time, or the package loading time
            truck3_candidates[i].loading_time = datetime.time(int(truck3_candidates[i].notes[12:14]),int(truck3_candidates[i].notes[15:18]),00)
            truck3.add_package(truck3_candidates[i])
            truck3.time = max(truck3.time, truck3_candidates[i].loading_time)
    #load truck one, overflow -> truck 2 -> truck 3
    for i in range(len(truck1_candidates)):
        truck1_candidates[i].loading_time = truck1.time
        if truck1.unused_capacity > 0:
            truck1.add_package(truck1_candidates[i])
        elif truck2.unused_capacity > 0:
            truck2.add_package(truck1_candidates[i])
        else:
            truck3.add_package(truck1_candidates[i])
    #update packages with truck_numbers
    for package in truck1.contents:
        package.truck_number = 1
    for package in truck2.contents:
        package.truck_number = 2
    for package in truck3.contents:
        package.truck_number = 3

    return truck1, truck2, truck3
