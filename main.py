import pygame

#THIS IS A TEST





class Hex:
    def init(self, meter=0, kilogram=0, second=0, ampere=0, kelvin=0, mole=0, candela=0):
        self.meter = meter
        self.kilogram = kilogram
        self.second = second
        self.ampere = ampere
        self.kelvin = kelvin
        self.mole = mole
        self.candela = candela

    def str(self):
        return f"Meter: {self.meter}, Kilogram: {self.kilogram}, Second: {self.second}, Ampere: {self.ampere}, Kelvin: {self.kelvin}, Mole: {self.mole}, Candela: {self.candela}"


board = [
    [Hex(0, 0, 0, 0, 0, 0, 0), Hex(0, 0, 0, 0, 0, 0, 0),],
    [Hex(0, 0, 0, 0, 0, 0, 0), Hex(0, 0, 0, 0, 0, 0, 0), Hex(0, 0, 0, 0, 0, 0, 0)],
    [Hex(0, 0, 0, 0, 0, 0, 0),Hex(0, 0, 0, 0, 0, 0, 0)]
]










pygame.init()