import pygame

#THIS IS A TEST





class Hex:
    def __init__(self, meter=0, kilogram=0, second=0, ampere=0, kelvin=0, mole=0, candela=0):
        self.meter = meter
        self.kilogram = kilogram
        self.second = second
        self.ampere = ampere
        self.kelvin = kelvin
        self.mole = mole
        self.candela = candela

    def __str__(self):
        return f"Meter: {self.meter}, Kilogram: {self.kilogram}, Second: {self.second}, Ampere: {self.ampere}, Kelvin: {self.kelvin}, Mole: {self.mole}, Candela: {self.candela}"

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
            #TODO: Is there a way to just force it to be another Hex?? I just did this because idk
            raise ValueError("Can only multiply with another Hex object.")

    def divide(self, other):
        if isinstance(other, Hex):
            self.meter -= other.meter
            self.kilogram -= other.kilogram
            self.second -= other.second
            self.ampere -= other.ampere
            self.kelvin -= other.kelvin
            self.mole -= other.mole
            self.candela -= other.candela
        else:
            raise ValueError("Can only divide by another Hex object.")


pygame.init()