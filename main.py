from hash_table import HashTable
from package import Package
import csv

def build_delivery_manifest(filename):
    """build manifest(hash_table) from csv file of packages"""
    manifest = HashTable()
    # https://stackoverflow.com/questions/52400408/import-csv-file-into-python
    with open(filename, newline='', mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            package = Package(int(row[0]), row[1], row[2], row[3], int(row[4]), row[5], row[6], row[7], "At the hub",
                              "TBD", "TBD")
            manifest.insert(package)
    return manifest

def main():

    print("main")
    manifest = build_delivery_manifest("data/WGUPS Package File.csv")
   

    print(manifest)
    print(manifest.lookup(23))
    print(manifest.lookup(6))
    print(manifest.lookup(9))

if __name__ == "__main__":
    main()