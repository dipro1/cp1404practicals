


def main():
    """Get mail and prompt varification and store the info"""

    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        name_varify = input(f"Is your name {name}? (Y/n) ").lower()
        if name_varify not in ("", "y"):
            name = get_name(email)
        email_to_name[email] = name
        email = input("Email: ")
    display_email(email_to_name)

def get_name(email):
    """Split the email to get the name"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts)
    return name


def display_email(email_to_name):
    """Display names and email"""
    for email, name in email_to_name.items():
        print(f"{name} {email}")

if __name__ == "__main__":
    main()
