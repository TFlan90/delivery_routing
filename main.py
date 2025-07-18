from hash_table import HashTable
from package import Package
import csv

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

def main():


    manifest = build_delivery_manifest("data/WGUPS Package File.csv")
    adjacency_matrix, address_key = load_distance_data("data/WGUPS Distance Table.csv")
    print("== address key ==")
    for k,v in address_key.items():
        print(str(v), k + '\n')
    print("== adj matrix  cell==")
    print(f"distance from the hub to dalton ave is {adjacency_matrix[1][0]}")
    print("== manifest ==")
    print(manifest)
    print("== manifest lookup ==")
    print(manifest.lookup(23))
    print(manifest.lookup(6))
    print(manifest.lookup(9))


if __name__ == "__main__":
    main()