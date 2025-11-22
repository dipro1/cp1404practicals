from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)


    my_taxi.drive(40)
    print(f"{my_taxi.get_fare()}") #test


if __name__ == "__main__":
    main()