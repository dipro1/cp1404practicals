class Band:
    def __init__(self, name=""):
        self.name = name
        self.musicians = []


    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        return "\n".join(musician.play() for musician in self.musicians)
