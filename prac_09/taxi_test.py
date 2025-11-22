from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)


    my_taxi.drive(40)

    print(my_taxi)
    print(f"Current fare is ${my_taxi.get_fare()}")

    my_taxi.start_fare()

    my_taxi.drive(100)

    print(my_taxi)
    print(f"Current fare is ${my_taxi.get_fare()}")
    # have to change the initial fuel of my_taxi so that it can go to 100km it only does 100km odo

if __name__ == "__main__":
    main()