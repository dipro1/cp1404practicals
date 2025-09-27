

def main():

    MINIMUM_LENGTH = 10                                                           #set initial password requirements

    password = get_password(MINIMUM_LENGTH)

    print_asterisks(password)


def print_asterisks(password: str):
    print("*" * len(password))  # print hidden password


def get_password(MINIMUM_LENGTH: int) -> str:
    password = input("Please enter your password: ")  # get user password

    while len(password) < MINIMUM_LENGTH:  # error correction
        print(f"Password needs to be at least {MINIMUM_LENGTH} character long")

        password = input("Please enter your password: ")  # get correct password
    return password


#f __name__ == "__main__":
main()