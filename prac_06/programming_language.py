"""
Estimate: 15 minutes
Start time:  04:20 am
Finish time: 4:56 am
"""

class ProgrammingLanguage:
    """programing language build"""
    def __init__(self, name, typing, reflection, year):
        """Programing language parameters"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def is_dynamic(self):
        """check for dynamic"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """compile all relevant info"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"