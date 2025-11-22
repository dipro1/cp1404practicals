from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            choose_taxi(taxis)
        elif choice == "d":
            drive_taxi()
        else:
            print("invalid input")

        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    print("Taxis available:")
    print(f"{taxis}")

def drive_taxi():
    pass


if __name__ == "__main__":
    main()