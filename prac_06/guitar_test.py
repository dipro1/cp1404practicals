"""
Estimate: 30 minutes
Start time:  12:40 am
Finish time: 12:38 am
"""


from guitar import Guitar
YEAR = 2025


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    expected_gibson_age = YEAR - 1922
    expected_another_age = YEAR - 2013
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age()}")



if __name__ == "__main__":
    main()