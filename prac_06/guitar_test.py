"""
Estimate: 30 minutes
Start time:  12:40 am
Finish time: 1:11 am
"""

from guitar import Guitar

YEAR = 2025


def main():
    """handel all testing"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)  # add the guitar with the 3 variables
    another = Guitar("Another Guitar", 2013, 0)

    expected_gibson_age = YEAR - 1922  # calculate age
    expected_another_age = YEAR - 2013
    """compare results from Guitar.py and calculated age"""
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age()}")

    expected_gibson_vintage = expected_gibson_age >= 50
    expected_another_vintage = expected_gibson_age >= 50
    """compare results from Guitar.py and vintage check"""
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected {expected_another_vintage}. Got {another.is_vintage()}")


if __name__ == "__main__":
    main()
