class Wallet:
    def _init_(self, color, vola):
        self.color = color
        self.vola = vola

    def addVola(self, vola):
        self.vola += vola
        print(vola)
    def getVola(self, vola):
        print(vola)
    
