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
    available_taxis(taxis)

    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            current_taxi = taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")



def drive_taxi():
    pass

def available_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()