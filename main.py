from data_loader import *
from truck import Truck
from delivery_route import start_delivery_route
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
    start_delivery_route(t1,adjacency_matrix,address_key,manifest)
    start_delivery_route(t2, adjacency_matrix, address_key,manifest)
    #truck 3 goes out once truck 2 is done with their route (making a driver available)
    t3.time = t2.time
    start_delivery_route(t3, adjacency_matrix, address_key,manifest)


    print(f"POST DELIVERIES:\n Truck 1 unused capacity: {t1.unused_capacity}\n Truck 2 unused capacity: {t2.unused_capacity}\n Truck 3 unused capacity:"
          f" {t3.unused_capacity}" )
    print(f"Combined miles traveled for all 3 trucks: {t1.distance_traveled + t2.distance_traveled + t3.distance_traveled}")
    print(t3.list_contents())
if __name__ == "__main__":
    main()