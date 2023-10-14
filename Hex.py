class Hex:
    def __init__(self, meter=0, kilogram=0, second=0, ampere=0, kelvin=0, mole=0, candela=0):
        self.meter = meter
        self.kilogram = kilogram
        self.second = second
        self.ampere = ampere
        self.kelvin = kelvin
        self.mole = mole
        self.candela = candela
    
    # Add methods
    def addMeter(self):
        self.meter += 1
    def addKilogram(self):
        self.kilogram += 1
    def addSecond(self):
        self.second += 1
    def addAmpere(self):
        self.ampere += 1
    def addKelvin(self):
        self.kelvin += 1
    def addMole(self):
        self.mole += 1
    def addCandela(self):
        self.candela += 1
    
    # Remove methods
    def removeMeter(self):
        self.meter -= 1
    def removeKilogram(self):
        self.kilogram -= 1
    def removeSecond(self):
        self.second -= 1
    def removeAmpere(self):
        self.ampere -= 1
    def removeKelvin(self):
        self.kelvin -= 1
    def removeMole(self):
        self.mole -= 1
    def removeCandela(self):
        self.candela -= 1

    def __str__(self):
        return f"Meter: {self.meter}, Kilogram: {self.kilogram}, Second: {self.second}, Ampere: {self.ampere}, Kelvin: {self.kelvin}, Mole: {self.mole}, Candela: {self.candela}"
