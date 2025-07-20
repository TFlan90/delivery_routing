from data_loader import *
from truck import Truck



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
    package = (manifest.lookup(23))
    print(package)
    print(manifest.lookup(6))
    print(manifest.lookup(9))


    t1 = Truck(1)
    t2 = Truck(2)
    t3 = Truck(3)

    load_truck(manifest, t1, t2, t3)
    print("======trucks after loading=====")
    print(t1)
    print(t2)
    print(t3)
    print("======trucks 1 contents=====")
    print(t1.list_contents())
    print(t2)
    print("======trucks 2 contents=====")
    print(t2.list_contents())
    print(t3)
    print("======trucks 3 contents=====")
    print(t3.list_contents())
if __name__ == "__main__":
    main()