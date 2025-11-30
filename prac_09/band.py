class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_text = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_text})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        return "\n".join(musician.play() for musician in self.musicians)
