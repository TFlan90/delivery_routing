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
            #update package with incorrect address sometime after 10:20
            if "Wrong address listed" in package.notes and truck.time >= datetime.time(hour=10,minute=20):
                package.delivery_address = "410 S State St"
                package.notes = ""

            #only considers packages that are not delivered and have the correct address
            if package.delivery_status in ("in transit", "At the hub") and "Wrong address listed" not in package.notes:
                #position of package address in adjacency matrix
                potential_next_delivery = addr_key[package.delivery_address]
                #position of trucks current addr in adjacency matrix
                current_location = addr_key[truck.current_location]
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
        truck.log_delivery(time_spent_traveling,min_distance_to_nearest_location,potential_next_delivery_location)
        #update package
        package_to_log.deliver_package(truck.time)
        print(f"[Address of most recent delivery + truck number {truck.truck_number} new location: {truck.current_location} and current time is/delivery time was {truck.time}")
        print(f"package number {package_to_log.package_id}, delivery deadline was {package_to_log.delivery_deadline} : delivery time was {package_to_log.delivery_time}")
        print(f"Total miles traveled so far {truck.distance_traveled}")


        print(packages_delivered, "]")
        packages_delivered += 1

def main():


    manifest = build_delivery_manifest("data/WGUPS Package File.csv")
    adjacency_matrix, address_key = load_distance_data("data/WGUPS Distance Table.csv")
    print("== address key ==")
    for k,v in address_key.items():
        print(k + '\n')
    print("== manifest ==")
    print(manifest)


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
    print("==truck 2 contents===")
    print(t2.list_contents())
    print("==truck 3 contents===")
    print(t3.list_contents())
    print(f"Truck 1 unused capacity: {t1.unused_capacity}\n Truck 2 unused capacity: {t2.unused_capacity}\n Truck 3 unused capacity:"
          f" {t3.unused_capacity}" )
    print("===Delivery Test===")
    start_delivery_route(t1,adjacency_matrix,address_key)
    start_delivery_route(t2, adjacency_matrix, address_key)
    t3.time = t2.time
    start_delivery_route(t3, adjacency_matrix, address_key)


    print(f"POST DELIVERIES:\n Truck 1 unused capacity: {t1.unused_capacity}\n Truck 2 unused capacity: {t2.unused_capacity}\n Truck 3 unused capacity:"
          f" {t3.unused_capacity}" )
    print(f"Combined miles traveled for all 3 trucks: {t1.distance_traveled + t2.distance_traveled + t3.distance_traveled}")
    print(t3.list_contents())
if __name__ == "__main__":
    main()