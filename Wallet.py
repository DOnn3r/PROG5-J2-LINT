class Wallet:

    def __init__(self, color: str, size: str, initialVola: float = 0.0):
        self.color = color
        self.size = size
        self.volaAmount = initialVola
        self.isOpen = False
        self.isLost = False

    def addVola(self, amount: float):
        if amount > 0:
            self.volaAmount += amount
            return True
        return False

    def getVola(self, amount: float):
        if self.volaAmount >= amount and amount > 0:
            self.volaAmount -= amount
            return amount
        return 0.0

    def open(self):
        self.isOpen = True

    def close(self):
        self.isOpen = False

    def isLost(self) -> bool:
        return self.isLost

    def checkVola(self) -> float:
        return self.volaAmount


my_wallet = Wallet("noir", "moyen", 50.0)
my_wallet.addVola(10.5)
print(f"Montant actuel: {my_wallet.checkVola()}")
print(my_wallet.isLost)
