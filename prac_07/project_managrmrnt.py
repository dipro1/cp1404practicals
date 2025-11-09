
from datetime import datetime

from Scripts.pywin32_testall import project_root

from project import Project

DEFAULT_FILENAME = "projects.txt"


def parse_date(dmy: str):
    return datetime.strptime(dmy.strip(), "%d/%m/%Y").date()


def load_projects(filename: str) -> list[Project]:

    projects: list[Project] = []
    with open(filename, "r", encoding="utf-8") as f:
        f.readline()  # skip header
        for line in f:
            if not line.strip():
                continue
            name, start_s, priority_s, cost_s, complete_s = line.strip().split("\t")
            projects.append(
                Project(
                    name=name,
                    start_date=parse_date(start_s),
                    priority=int(priority_s),
                    cost_estimate=float(cost_s),
                    percent_complete=int(complete_s),
                )
            )
    return projects


def menu() -> str:
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")
    return input(">>> ").strip().upper()



def display_projects(projects: list[Project]) -> None:
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = [project for project in projects if not project.check_if_complete()]
    completed = [project for project in projects if project.check_if_complete()]
    incomplete.sort()
    completed.sort()
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")



def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = menu()
    while choice != "Q":
        if choice == "L":
            print("")
        elif choice == "S":
            print("")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("")
        elif choice == "A":
            print("")
        elif choice == "U":
            print("")
        else:
            print("Invalid choice")
        choice = menu()

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()