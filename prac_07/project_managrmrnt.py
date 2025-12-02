
from datetime import datetime


from project import Project
from operator import itemgetter


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



def display_projects(projects):
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

def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    target = parse_date(date_string)
    matches = [project for project in projects if project.check_cutoff(target)]
    sortable = [(project.start_date, project.priority, project.name, project) for project in matches]
    sortable.sort(key=itemgetter(0, 1, 2))
    for project in matches:
        print(project)

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_date = input("Start date (dd/mm/yyyy): ").strip()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    projects.append(
        Project(
            name=name,
            start_date=parse_date(start_date),
            priority=priority,
            cost_estimate=cost_estimate,
            percent_complete=percent_complete,
        )
    )

def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = input("Project choice: ").strip()
    if choice == "":
        return
    index = int(choice)
    project = projects[index]
    print(project)

    new_percent = input("New Percentage: ").strip()
    if new_percent != "":
        project.percent_complete = int(new_percent)

    new_priority = input("New Priority: ").strip()
    if new_priority != "":
        project.priority = int(new_priority)

def save_projects(filename: str, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n"
            )



def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = menu()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ").strip()
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = menu()

    save_answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip()
    if save_answer and save_answer[0].lower() == "y":
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")


    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()