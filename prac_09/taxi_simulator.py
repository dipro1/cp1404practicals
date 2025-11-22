""" Taxi simulation """
# imports
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"    #menu



def main():
    print("Let's drive!")   # welcome statement

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    # taxi list
    current_taxi = None
    bill_to_date = 0.0
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":    #menu options
        if choice == "c":
            current_taxi = choose_taxi(taxis, current_taxi)
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        else:
            print("invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Bill to date: ${bill_to_date:.2f}")
    print("Taxis are now:")
    available_taxis(taxis)

def choose_taxi(taxis,current_taxi):
    """User choice of taxi"""
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
    return current_taxi



def drive_taxi(current_taxi, bill_to_date):
    """Drive user selected taxi"""
    try:
        distance_to_drive = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return bill_to_date

    current_taxi.start_fare()
    current_taxi.drive(distance_to_drive)
    cost_of_trip = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${cost_of_trip:.2f}")
    bill_to_date += cost_of_trip
    return bill_to_date


def available_taxis(taxis):
    """Indexed taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()