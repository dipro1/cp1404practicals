from silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

    fancy_taxi.drive(18)

    expected_fare = 48.78
    actual_fare = fancy_taxi.get_fare()
    assert f"{actual_fare:.2f}" == f"{expected_fare:.2f}"

    print("The fare is fair")


if __name__ == "__main__":
    main()
