from prac_04.list_comprehensions import names


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = names
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        return self.typing.lower() == "dynamic"