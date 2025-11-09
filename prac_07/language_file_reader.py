"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from programming_language import ProgrammingLanguage

POINTER_ARITHMETIC_LANGUAGES = {"c", "c++", "c#", "d"}
HEADER = ["Language", "Typing", "Reflection", "Year", "PointerArithmetic"]


def _pointer_flag(name: str) -> str:
    return "Yes" if name.strip().casefold() in POINTER_ARITHMETIC_LANGUAGES else "No"


def add_new_colum():
    rows = []
    with open("languages.csv", "r", newline="") as f:
        first = f.readline()
        if not first:
            with open("languages.csv", "w", newline="") as out:
                csv.writer(out).writerow(HEADER)
            return

        rows.append(HEADER)
        line = f.readline()
        while line != "":
            raw = line.strip()
            if raw:
                parts = [p.strip() for p in raw.split(",")]
                base = (parts + ["", "", "", ""])[:4]
                lang_name, typing, reflection, year = base
                pointer = _pointer_flag(lang_name)
                rows.append([lang_name, typing, reflection, year, pointer])
            line = f.readline()

    with open("languages.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def add_language():
    new_language = ["C#", "Static", "Yes", "2000"]
    try:
        with open("languages.csv", "r", newline="") as language:
            reader = csv.reader(language)
            existing_names = {row[0] for row in reader if row}
        if new_language[0] not in existing_names:
            with open("languages.csv", "a", newline="") as language:
                writer = csv.writer(language)
                writer.writerow(new_language)
    except FileNotFoundError:
        with open("languages.csv", "w", newline="") as language:
            writer = csv.writer(language)
            writer.writerow(["Language", "Typing", "Reflection", "Year"])
            writer.writerow(new_language)


def main():
    """Read file of programming language details, save as objects, display."""
    add_language()
    add_new_colum()
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    # First, open the file for reading - note: specify newline
    # to avoid quoted \n in strings being considered a new record
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        print(row)
    in_file.close()


# using_csv()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    # Language will be a new subclass of the tuple data type class
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        # print(row)
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()
