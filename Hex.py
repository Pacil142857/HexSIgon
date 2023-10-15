class Hex:
    def __init__(self, second=0, meter=0, kilogram=0, ampere=0, kelvin=0, mole=0, candela=0):
        
        self.second = second
        self.meter = meter
        self.kilogram = kilogram
        self.ampere = ampere
        self.kelvin = kelvin
        self.mole = mole
        self.candela = candela
    
    def change(self, second=0, meter=0, kilogram=0, ampere=0, kelvin=0, mole=0, candela=0):
        self.second = second
        self.meter = meter
        self.kilogram = kilogram
        self.ampere = ampere
        self.kelvin = kelvin
        self.mole = mole
        self.candela = candela

    def clear(self):
        self.meter = 0
        self.kilogram = 0
        self.second = 0
        self.ampere = 0
        self.kelvin = 0
        self.mole = 0
        self.candela = 0
    
    def isClear(self):
        return (
            self.meter == 0 and
            self.kilogram == 0 and 
            self.second == 0 and
            self.ampere == 0 and
            self.kelvin == 0 and
            self.mole == 0 and
            self.candela == 0 
        )

    def difficulty(self):
        return(
            abs(self.second)+
            abs(self.meter)+
            abs(self.kilogram)+
            abs(self.ampere)+
            abs(self.kelvin)+
            abs(self.mole)+
            abs(self.candela)
        )

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

    def multiply(self, other):
        if isinstance(other, Hex):
            self.meter += other.meter
            self.kilogram += other.kilogram
            self.second += other.second
            self.ampere += other.ampere
            self.kelvin += other.kelvin
            self.mole += other.mole
            self.candela += other.candela
        else:
            raise ValueError("Can only multiply with another Hex object.")

    def divide(self, other):
        if isinstance(other, Hex):
            self.meter = other.meter - self.meter
            self.kilogram = other.kilogram - self.kilogram
            self.second = other.second - self.second
            self.ampere = other.ampere - self.ampere
            self.kelvin = other.kelvin - self.kelvin
            self.mole = other.mole - self.mole
            self.candela = other.candela - self.candela
        else:
            raise ValueError("Can only divide by another Hex object.")
    
    def __eq__(self, hex):
        return self.meter == hex.meter and self.kilogram == hex.kilogram and self.second == hex.second and \
            self.ampere == hex.ampere and self.kelvin == hex.kelvin and self.mole == hex.mole and self.candela == hex.candela

    def __str__(self):
        numerator = ""
        denominator = ""
        # Create numerator and denominator
        for unit, symbol in ((self.meter, "m"), (self.kilogram, "kg"), (self.second, "s"),
                             (self.ampere, "A"), (self.kelvin, "K"), (self.mole, "mol"), (self.candela, "cd")):
            if unit > 0:
                if unit > 1:
                    numerator += f"({symbol}^{unit})·"
                else:
                    numerator += f"{symbol}·"
            elif unit < 0:
                if unit < -1:
                    denominator += f"({symbol}^{-1 * unit})·"
                else:
                    denominator += f"{symbol}·"
        
        if numerator:
            numerator = numerator[:-1]
        if denominator:
            denominator = denominator[:-1]
        
        if denominator:
            return f"{numerator if numerator else 1}\n{'—' * max(len(numerator), len(denominator))}\n{denominator}"
        if numerator:
            return numerator
        return "1"
