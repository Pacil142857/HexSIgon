class Unit:
    def __init__(self, name, symbol, quantity, hex):
        self.name = name.lower() # Eg: Second
        self.symbol = self # Eg: s
        self.quantity = quantity.lower() # Eg: time
        self.hex = hex
        # self.description = description # Eg: "The second, symbol s, is the SI unit of time. It is defined by taking the fixed numerical value of the caesium frequency, ∆νCs, the unperturbed ground-state hyperfine transition frequency of the caesium 133 atom, to be 9192631770 when expressed in the unit Hz, which is equal to s−1."
