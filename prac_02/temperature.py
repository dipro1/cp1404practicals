"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""


def celsius_to_fahrenheit(celsius):                                 #calculate c_to_f
    return celsius*9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):                              #calculated f_to_c
        return  5 / 9 * (fahrenheit - 32)



def main():
    #menu
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()                                  #cahnge the casing for the input
    while choice != "Q":                                            #option to opt out of the program
        if choice == "C":                                           #user set temp
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)             #call function c_to_f
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = fahrenheit_to_celsius(fahrenheit)             #call function f_to_c
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")                                 #error handling
        print(MENU)
        choice = input(">>> ").upper()                              #call choice
    print("Thank you.")

if __name__ == '__main__':
    main()                                                          #call main