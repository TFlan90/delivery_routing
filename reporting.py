import datetime
def report_status(manifest, query_time):
    print(f"TIME IS: {query_time}")
    for i in range(1,41):
        package = manifest.lookup(i)
        address = package.delivery_address
        loading_time = package.loading_time
        delivery_time = package.delivery_time
        truck_number = package.truck_number
        deadline = package.delivery_deadline
        #revert package 9 to old address if time is before 10:20
        if i == 9 and query_time < datetime.time(hour=10,minute=20):
            address = "300 State St"
        #mark packages 6, 25, 28, and 32 as DELAYED before 9:05
        if query_time < datetime.time(hour=9,minute=5) and ( i == 6 or i == 25 or i == 28 or i == 32):
            status = "DELAYED"
            print(f"Package {package.package_id}: Address: {address}, Loading Time: {loading_time}")
            print(f"Current Status: {status}, Delivery Deadline: {deadline}, Delivery Time: TBD, Current Time Is: {query_time}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #any packages loaded to truck 3 are at the hub prior to 9:58:20
        elif truck_number == 3  and query_time < datetime.time(hour=9, minute=58, second=20):
            status = "AT HUB"
            print(f"Package {package.package_id}: Address: {address}, Loading Time: {loading_time},  Truck Number: {truck_number}")
            print(f"Current Status: {status}, Delivery Deadline: {deadline}, Delivery Time: TBD, Current Time Is: {query_time}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #report delivered package
        elif delivery_time != "TBD" and delivery_time <= query_time:
            status = "DELIVERED"
            print(f"Package {package.package_id}: Address: {address}, Loading Time: {loading_time},  Truck Number: {truck_number}")
            print(f"Current Status: {status}, Delivery Deadline: {deadline}, Delivery Time: {delivery_time}, Current Time Is: {query_time}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #report package is in transit
        elif loading_time != "TBD" and loading_time <= query_time:
            status ="IN TRANSIT"
            print(f"Package {package.package_id}: Address: {address}, Loading Time: {loading_time},  Truck Number: {truck_number}")
            print(f"Current Status: {status}, Delivery Deadline: {deadline}, Delivery Time: TBD, Current Time Is: {query_time}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #otherwise package is waiting at hub and not associated with a truck yet
        else:
            status = "AT HUB"
            print(f"Package {package.package_id}: Address: {address}, Loading Time: {loading_time}, Truck Number: {truck_number}")
            print(f"Current Status: {status}, Delivery Deadline: {deadline}, Delivery Time: TBD, Current Time Is: {query_time}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
