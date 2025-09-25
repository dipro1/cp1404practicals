# """
# CP1404/CP5632 - Practical
# Pseudocode for temperature conversion
# """
# #break line can also be used \n cant make coments onthe menu section
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))   #same as the first if satement
        celsius = (fahrenheit - 32)*5/9
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

print("ok")

# x = 5
# for i in range(x):
#     x = x + i
#     print(x, end=" ")