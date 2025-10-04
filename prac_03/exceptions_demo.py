"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("please enter a nonzero denominator")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")



#1When will a ValueError occur?
#A: when anything except an integer is put in either the numerator or denominator

#2When will a ZeroDivisionError occur?
#A: when the denominator is 0

#3Could you change the code to avoid the possibility of a ZeroDivisionError?
#yes