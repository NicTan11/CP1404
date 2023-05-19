from prac_09.unreliable_car import UnreliableCar


def main():

    reliable_car = UnreliableCar("Mostly Good", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 11):
        print(f"Attempting to drive {i}km:")
        print(f"{reliable_car.name} drove {reliable_car.drive(i)}km")
        print(f"{unreliable_car.name} drove {unreliable_car.drive(i)}km")

    # print the final states of the cars
    print(reliable_car)
    print(unreliable_car)


main()
