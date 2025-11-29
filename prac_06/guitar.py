"""
Estimate: 30 minutes
Start time:  12:04 am
Finish time: 12:38 am
"""
YEAR = 2025 #current year

class Guitar:
    """guitar class with 3 variables"""
    def __init__(self, name = "", year = 0, cost = 0.0):
        """variables for the class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return the info of the guitar"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """check for age of guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """check if guitar is vintage"""
        return self.get_age() >= 50
