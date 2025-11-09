
from datetime import date

class Project:

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, percent_complete: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete