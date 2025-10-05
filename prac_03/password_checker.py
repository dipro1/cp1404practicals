"""
CP1404/CP5632 - Practical
Password checker code
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0
    for character in password:                                                      #checks characters in the input password
        if character.islower():                                                     #check for lower case in the password
            number_of_lower += 1                                                    #add count of lowercase
        elif character.isupper():                                                   #check for uppercase in password
            number_of_upper += 1                                                    #add count of uppercase
        elif character.isdigit():                                                   #check for digits
            number_of_digit += 1                                                    #add count of digits
        elif character in SPECIAL_CHARACTERS:                                       #check for cpecial character
            number_of_special += 1                                                  #add count of special characters



    if number_of_lower == 0 or number_of_upper == 0 or number_of_digit == 0:        #return false if any of the count is 0
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and number_of_special == 0:                    #check if special caracters are required and check for count of characters
        return False                                                                #return false if special character is not required
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()