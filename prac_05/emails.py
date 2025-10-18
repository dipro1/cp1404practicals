


def main():


    email_to_name = {}
    email = input("Email: ")



def get_name(email):
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts)
    return name


def display_email(email_to_name):
    for email, name in email_to_name():
        print(f"{name} {email}")

if __name__ == "__main__":
    main()
