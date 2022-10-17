class Player():
    def __init__(self, name):
        self.name = name
        self.prize = 0

    def setName(self, name):
        self.name = name

    def setPrize(self, prize):
        self.prize = prize

    def getName(self):
        return self.name

    def getPrize(self):
        return self.prize
