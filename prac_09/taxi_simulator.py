from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    print("Let's drive!")

    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("invalid input")

        print(MENU)
        choice = input(">>> ").lower()

if __name__ == "__main__":
    main()