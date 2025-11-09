
from datetime import date

class Project:

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, percent_complete: int):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __lt__(self, other: "Project") -> bool:
        """sort by less than"""
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.start_date != other.start_date:
            return self.start_date < other.start_date
        return self.name < other.name

    def check_if_complete(self) -> bool:
        """check if project is complete"""
        return self.percent_complete >= 100

    def check_cutoff(self, d: date) -> bool:
        """check if cutoff date is passed"""
        return self.start_date > d

    def check_start_date(self) -> str:
        """day/month/year"""
        return self.start_date.strftime("%d/%m/%Y")

    def __str__(self) -> str:
        return (f"{self.name}, start: {self.check_start_date()}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.percent_complete}%")