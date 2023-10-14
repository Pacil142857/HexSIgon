from Hex import Hex
from Order import Order

class Board:
    compatibility = [[2, 3, 1], # Hex 0
                     [0, 3, 4], # Hex 1
                     [0, 3, 5], # Hex 2
                     [0, 1, 2, 4, 5, 6], # Hex 3
                     [1, 3, 6], # Hex 4
                     [2, 3, 6], # Hex 5
                     [3, 4, 5]] # Hex 6
    
    def __init__(self, hex_0=Hex(), hex_1=Hex(), hex_2=Hex(), hex_3=Hex(), hex_4=Hex(), hex_5=Hex(), hex_6=Hex()):
        self.hexes = [hex_0, hex_1, hex_2, hex_3, hex_4, hex_5, hex_6]
        self.orders = [Order(), Order(), Order()]



        self.moveCount = 0
        self.orderCount = 0

    def refresh_order(self, order_index):
        





        self.orders[order_index]
    def __str__(self):
        return f"Hex0: {self.hex_0.__str__}, Hex1: {self.hex_1.__str__}, Hex2: {self.hex_0.__str__}, Hex3: {self.hex_3.__str__}, Hex4: {self.hex_4.__str__}, Hex5: {self.hex_5.__str__}, Hex6: {self.hex_6.__str__},"

    # We move the first hex INTO the second hex, thus first hex may disappear. 
    def multiplyHexes(self, hex_index_1, hex_index_2):
        if(hex_index_2 in self.compatibility[hex_index_1]):
            self.moves+=1
            self.hexes[hex_index_2].multiply(self.hexes[hex_index_1])
            self.hexes[hex_index_1].clear()

    # We move the first hex INTO the second hex, thus first hex may disappear. 
    def divideHexes(self, hex_index_1, hex_index_2):
        if(hex_index_2 in self.compatibility[hex_index_1]):
            self.moves+=1
            self.hexes[hex_index_2].divide(self.hexes[hex_index_1])
            self.hexes[hex_index_1].clear()


