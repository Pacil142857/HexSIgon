class Order:
    def __init__(self, hex, points, quantity_name, unit_name):
        self.hex = hex
        self.points = points
        self.quantity_name = quantity_name
        self.unit_name = unit_name
    
    def compare_to(self, hex):
        return self.hex == hex
    
    def __str__(self):
        if (self.unit_name):
            return f"Create a {self.unit_name}, the unit for {self.quantity_name}"
        return f"Create the unit for {self.quantity_name}"