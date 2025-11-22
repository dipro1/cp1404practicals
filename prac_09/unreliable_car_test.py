from unreliable_car import UnreliableCar


def main():
    car_30 = UnreliableCar("30% Reliable", 100, 30)

    attempts = 100

    print("Testing 30% reliable car:")
    reliability_test(car_30, attempts)


def reliability_test(car, attempts):
    successful_drives = 0

    for i in range(attempts):
        distance_driven = car.drive(1)
        if distance_driven > 0:
            successful_drives += 1

    print(f"Tried to drive {attempts} times.")
    print(f"Successful drives: {successful_drives}")


if __name__ == "__main__":
    main()
