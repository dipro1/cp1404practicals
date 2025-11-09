
from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def parse_date(dmy: str):
    return datetime.strptime(dmy.strip(), "%d/%m/%Y").date()

def main():
    print("Welcome to Pythonic Project Management")
    pass


if __name__ == "__main__":
    main()
