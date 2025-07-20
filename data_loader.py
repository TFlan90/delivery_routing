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
                              "TBD", "TBD")
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
    when a package is loaded on a truck, it's considered "in transit"
    everything in truck2_candidates -> truck2
    everything in truck3_candidates -> truck3
    truck1_candidates -> 16 packages(truck obj capacity) ->  truck1
    Overflow goes to truck 2 until it's full and the remainer goes on truck 3

    """
    truck1_candidates = []
    truck2_candidates = []
    truck3_candidates = []


    for i in range(1,41):
        package = manifest.lookup(i)
        if "Can only be on truck 2" in package.notes or "Must be delivered with" in package.notes:
            truck2_candidates.append(package)
        elif "will arrive" in package.notes or "Wrong address" in package.notes:
            truck3_candidates.append(package)
        else:
            truck1_candidates.append(package)

    for i in range(len(truck2_candidates)):
        truck2_candidates[i].loading_time = truck2.time
        truck2.add_package(truck2_candidates[i])
    for i in range(len(truck3_candidates)):
        if "will arrive" not in truck3_candidates[i].notes:
            truck3_candidates[i].loading_time = truck3.time
            truck3.add_package(truck3_candidates[i])
        else:
            #used to extract delayed packages loading time
            #extracted delivery time will be cast to a datetime.time obj and passed to the package
            truck3_candidates[i].loading_time = datetime.time(int(truck3_candidates[i].notes[12:14]),int(truck3_candidates[i].notes[15:18]),00)
            truck3.add_package(truck3_candidates[i])
    for i in range(len(truck1_candidates)):
        truck1_candidates[i].loading_time = truck1.time
        if truck1.unused_capacity > 0:
            truck1.add_package(truck1_candidates[i])
        elif truck2.unused_capacity > 0:
            truck2.add_package(truck1_candidates[i])
        else:
            truck3.add_package(truck1_candidates[i])

    return truck1, truck2, truck3
