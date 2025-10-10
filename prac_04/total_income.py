"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    try:
        number_of_months = int(input("How many months? "))  # get number of months
        if number_of_months < 1:  # check for valid month
            print("Minimum number of months is 1")  # error message for months less than 1
            return
    except ValueError:
        print("Invalid input")  # error message for month not a number
        return

    for month in range(1, number_of_months + 1):
        try:
            income = float(input(f"Enter income for month {month}: "))  # get income of the month
            incomes.append(income)
        except ValueError:  # error check for income not a number
            print("invalid input")
            return

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
