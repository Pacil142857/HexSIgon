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

    def __eq__(self, hex):
        return self.meter == hex.meter and self.kilogram == hex.kilogram

    def __str__(self):
        numerator = ""
        denominator = ""
        # Create numerator and denominator
        for unit, symbol in ((self.meter, "m"), (self.kilogram, "kg"), (self.second, "s"),
                             (self.ampere, "A"), (self.kelvin, "K"), (self.mole, "mol"), (self.candela, "cd")):
            if unit > 0:
                if unit > 1:
                    numerator += f"({symbol}^{unit})"
                else:
                    numerator += f"({symbol})"
            elif unit < 0:
                if unit < -1:
                    denominator += f"({symbol}^{unit})"
                else:
                    denominator += f"({symbol})"
        
        if denominator:
            return f"({numerator}) / ({denominator})"
        return numerator
