
MINIMUM_LENGTH = 10

password = input("Please enter your password: ")

while len(password) < MINIMUM_LENGTH:
    print(f"Password needs to be at least {MINIMUM_LENGTH} character long")

    password = input("Please enter your password: ")


print("*"*len(password))
