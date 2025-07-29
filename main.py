#Student_ID: 011095408
#Thomas Flanley
from data_loader import *
from truck import Truck
from delivery_route import start_delivery_route
from reporting import *
def main():
    #create package manifest using custom hash table
    manifest = build_delivery_manifest("data/WGUPS Package File.csv")
    #create 2d array of distances between addresses and dict that exposes a package ID given an address
    adjacency_matrix, address_key = load_distance_data("data/WGUPS Distance Table.csv")
    #init truck objects
    t1 = Truck(1)
    t2 = Truck(2)
    t3 = Truck(3)
    #load trucks by passing the 3 truck objects and the package manifest
    load_truck(manifest, t1, t2, t3)
   #take user input for UI
    print("Welcome to WGUPS - We get things done quick here, because time is money, friend!")
    print("First, we'll ask you for a military time - the hour first, followed by the minute")
    print("We'll first share with you a record of the days completed deliveries")
    print("Next, you will see a snapshot of all the packages, and their statuses at the time you indicated!")
    start_time = datetime.time(hour=int(input("Start hour: ")),minute=int(input("Start minute: ")), second=0)
    print(f"You entered: {start_time}")
    print("~~~~~~~~~~START OF DAILY RECORD~~~~~~~~~~")
    #run delivery route for truck 1
    start_delivery_route(t1,adjacency_matrix,address_key,manifest)
    #run delivery route for truck 2
    start_delivery_route(t2, adjacency_matrix, address_key,manifest)
    #There are only 2 drivers, so truck 3 can't start its route until truck 2 has finished its route
    t3.time = t2.time
    #run delivery route for truck 3
    start_delivery_route(t3, adjacency_matrix, address_key,manifest)
    print(f"Combined miles traveled for all 3 trucks: {t1.distance_traveled + t2.distance_traveled + t3.distance_traveled}")
    print("~~~~~~~~~~END OF RECORD~~~~~~~~~~\n\n\n")
    report_status(manifest, start_time)


if __name__ == "__main__":
    main()