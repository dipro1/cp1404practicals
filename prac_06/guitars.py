"""
Estimate: 30 minutes
Start time:  1:20 am
Finish time: 1:52 am
"""



from guitar import Guitar

def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "" :
        year =int(input("year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    #guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    #guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are my guitars:")
        """check for width"""
        name_width = max(len(guitar.name) for guitar in guitars)
        cost_strings = [f"${guitar.cost:,.2f}" for guitar in guitars]
        cost_width = max(len(string) for string in cost_strings)

        """output of all the listed guitar"""
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            cost_string = f"{guitar.cost:,.2f}"
            print(f"Guitar {i}: {guitar.name:{name_width}} ({guitar.year}), worth ${cost_string:>{cost_width}}{vintage_string}")
    else:
        print("No guitars")

if __name__ == "__main__":
    main()