import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def load_guitars(filename=FILENAME):
    """Read guitars from CSV (Name,Year,Cost) into a list of Guitar objects."""
    guitars = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0].strip()
            year = int(row[1])
            cost = float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def add_new_guitar(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

def display_guitars(guitars):
    for guitar in guitars:
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage}")
    print()


def main():
    guitars = load_guitars()
    add_new_guitar(guitars)
    guitars.sort()
    display_guitars(guitars)

if __name__ == "__main__":
    main()