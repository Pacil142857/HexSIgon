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

class Board:
    compatibility = [[2, 3, 1], #Hex 0
                     [0, 3, 4], #Hex 1
                     [0, 3, 5], #Hex 2
                     [0, 1, 2, 4, 5, 6], #Hex 3
                     [1, 3, 6], #Hex 4
                     [2, 3, 6], #Hex 5
                     [3, 4, 5]] #Hex 6
    def __init__(self, hex_0=Hex(), hex_1=Hex(), hex_2=Hex(), hex_3=Hex(), hex_4=Hex(), hex_5=Hex(), hex_6=Hex()):
        self.hexes= [hex_0, hex_1, hex_2, hex_3, hex_4, hex_5, hex_6]

    def __str__(self):
        return f"Hex0: {self.hex_0.__str__}, Hex1: {self.hex_1.__str__}, Hex2: {self.hex_0.__str__}, Hex3: {self.hex_3.__str__}, Hex4: {self.hex_4.__str__}, Hex5: {self.hex_5.__str__}, Hex6: {self.hex_6.__str__},"

    #We move the first hex INTO the second hex, thus first hex may dissapear. 
    def multiplyHexes(self, hex_index_1, hex_index_2):
        if(hex_index_2 in self.compatibility[hex_index_1]):
            self.hexes[hex_index_2].multiply(self.hexes[hex_index_1])
            self.hexes[hex_index_1].clear

    #We move the first hex INTO the second hex, thus first hex may dissapear. 
    def divideHexes(self, hex_index_1, hex_index_2):
        if(hex_index_2 in self.compatibility[hex_index_1]):
            self.hexes[hex_index_2].divide(self.hexes[hex_index_1])
            self.hexes[hex_index_1].clear




pygame.init()