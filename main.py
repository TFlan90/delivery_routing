from data_loader import *
from truck import Truck

def start_delivery_route(truck,adj_matrix,addr_key):


    #test var:
    packages_delivered = 1
    #while the truck still has packages to be delivered
    while truck.unused_capacity < 16:
        min_distance_to_nearest_location = float('inf')
        potential_next_delivery_location = ""
        time_spent_traveling = 0
        package_to_log = None
        # loop over the packages in the truck
        for package in truck.contents:
            if package.delivery_status in ("in transit", "At the hub"):
                #position of package address in adjacency matrix
                potential_next_delivery = addr_key[package.delivery_address]
                #position of trucks current addr in adjacency matrix
                current_location = addr_key[truck.current_location]
                #test line
                #print(package.delivery_address," ", truck.current_location)
                #distance between truck and package - calling max for x to prevent out of bounds errors and min for y for same reason
                potential_distance = float(adj_matrix[max(current_location,potential_next_delivery)][min(current_location,potential_next_delivery)])
                #current candidate for nearest neighbor: if this package is closer than current nearest, update nearest
                #
                if potential_distance < min_distance_to_nearest_location:
                    #update min_distance
                    min_distance_to_nearest_location = potential_distance
                    #assign potential_delivery_location to the current packages address
                    potential_next_delivery_location = package.delivery_address
                    #assign pack to be logged
                    package_to_log = package
                    time_spent_traveling = ((min_distance_to_nearest_location / 18) * 60)

        #update truck
        truck.deliver_package(time_spent_traveling,min_distance_to_nearest_location,potential_next_delivery_location)
        #update package
        package_to_log.log_delivery(potential_next_delivery_location)
        print(f"truck new location: {truck.current_location} and current time is {truck.time}")
        print(f"Total miles traveled so far {truck.distance_traveled}")
        print(packages_delivered)
        packages_delivered += 1






def main():


    manifest = build_delivery_manifest("data/WGUPS Package File.csv")
    adjacency_matrix, address_key = load_distance_data("data/WGUPS Distance Table.csv")
    print("== address key ==")
    for k,v in address_key.items():
        print(k + '\n')
    print("== adj matrix  cell==")
    print(f"distance from the hub to dalton ave is {adjacency_matrix[1][0]}")
    print("== manifest ==")
    print(manifest)
    print("== manifest lookup ==")
    package = (manifest.lookup(23))
    print(package)
    print(manifest.lookup(6))
    print(manifest.lookup(9))


    t1 = Truck(1)
    t2 = Truck(2)
    t3 = Truck(3)

    load_truck(manifest, t1, t2, t3)
    #print("======trucks after loading=====")
    #print(t1)
    #print(t2)
    #print(t3)
    #print("======trucks 1 contents=====")
    #print(t1.list_contents())
    #print(t2)
    #print("======trucks 2 contents=====")
    #print(t2.list_contents())
    #print(t3)
    #print("======trucks 3 contents=====")
    #print(t3.list_contents())
    #print(t3.contents[1])
    print("==truck 1 contents===")
    print(t1.list_contents())
    print(f"Truck 1 unused capacity: {t1.unused_capacity}")
    print("===Delivery Test===")
    start_delivery_route(t1,adjacency_matrix,address_key)
    start_delivery_route(t2, adjacency_matrix, address_key)
    start_delivery_route(t3, adjacency_matrix, address_key)

    print(t1.distance_traveled + t2.distance_traveled + t3.distance_traveled )
if __name__ == "__main__":
    main()