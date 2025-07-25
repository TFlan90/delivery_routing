import datetime

def calculate_distance(i,j,adj_matrix):
    """abstract distance calculation logic to account for triangular matrix input"""
    return float(adj_matrix[max(i,j)][min(i,j)])

def calculate_time(distance_traveled):
    """calculate time traveled @18 mph"""
    return (distance_traveled / 18) * 60



def start_delivery_route(truck,adj_matrix,addr_key,manifest):
    """Runs delivery route for a single truck using the nearest neighbor approach"""
    #test var:
    packages_delivered = 1
    package_6_retrieved = False
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
            #retrieves package number 6 after it is available at 9:05
            if truck.truck_number == 1 and package_6_retrieved == False and truck.time > datetime.time(hour=9,minute=5):
                distance_to_hub = calculate_distance(addr_key[truck.current_location],0,adj_matrix)
                time_to_hub = calculate_time(distance_to_hub)
                #address edge case
                truck.return_to_hub(distance_to_hub, time_to_hub,manifest)
                print("RETURNING TO HUB FOR PACKAGE 6")
                #flag that package_6 has been picked up
                package_6_retrieved = True
                print(truck.list_contents())
            #only considers packages that are not delivered and have the correct address
            if package.delivery_status in ("in transit", "At the hub") and "Wrong address listed" not in package.notes:
                #position of package address in adjacency matrix
                potential_next_delivery = addr_key[package.delivery_address]
                #position of trucks current addr in adjacency matrix
                current_location = addr_key[truck.current_location]
                potential_distance = calculate_distance(current_location,potential_next_delivery,adj_matrix)
                #current candidate for nearest neighbor: if this package is closer than current nearest, update nearest
                #
                if potential_distance < min_distance_to_nearest_location:
                    #update min_distance
                    min_distance_to_nearest_location = potential_distance
                    #assign potential_delivery_location to the current packages address
                    potential_next_delivery_location = package.delivery_address
                    #assign pack to be logged
                    package_to_log = package
                    time_spent_traveling = calculate_time(min_distance_to_nearest_location)

        #update truck
        truck.log_delivery(time_spent_traveling,min_distance_to_nearest_location,potential_next_delivery_location)
        #update package
        package_to_log.deliver_package(truck.time)
        print(f"[Address of most recent delivery + truck number {truck.truck_number} new location: {truck.current_location} and current time is/delivery time was {truck.time}")
        print(f"package number {package_to_log.package_id}, delivery deadline was {package_to_log.delivery_deadline} : delivery time was {package_to_log.delivery_time}")
        print(f"Total miles traveled so far {truck.distance_traveled}")


        print(packages_delivered, "]")
        packages_delivered += 1
