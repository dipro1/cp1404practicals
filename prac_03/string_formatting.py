"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

NAME = "Gibson L-5 CES"
YEAR = 1922
COST = 16035.9


#fstring print with conditional

print(f"{YEAR} {NAME} for about ${COST:,.0f}!")


#for loop in n+1 range


for power in range(11):
    print(f"2^{power:2} is {2**power:>6}")