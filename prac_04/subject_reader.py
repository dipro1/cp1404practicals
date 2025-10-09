"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_details = load_data(FILENAME)
    display_subject(subject_details)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    sublect_list = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
            sublect_list.append(parts)  # See if that worked
    return sublect_list


def display_subject(subject_details):
    for subject, lecturer, number_of_students in subject_details:
        print(f"{subject} is taught by {lecturer} and has {number_of_students} students")


main()
