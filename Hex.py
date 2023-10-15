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

    def getAsList(self):
        return [self.second, self.meter, self.kilogram, self.ampere, self.kelvin, self.mole, self.candela]

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
        # Check to see if this hex matches a derived unit
        for unit in derived_units:
            if self == unit[3]:
                return unit[1]
        
        numerator = ""
        denominator = ""
        # Create numerator and denominator
        for unit, symbol in ((self.meter, "m"), (self.kilogram, "kg"), (self.second, "s"),
                             (self.ampere, "A"), (self.kelvin, "K"), (self.mole, "mol"), (self.candela, "cd")):
            if unit > 0:
                if unit > 1:
                    if unit == 4:
                        numerator += f"{symbol}⁴·"
                    if unit == 3:
                        numerator += f"{symbol}³·"
                    if unit == 2:
                        numerator += f"{symbol}²·"
                    else:
                        numerator += f"({symbol}^{unit})·"
                else:
                    numerator += f"{symbol}·"
            elif unit < 0:
                if unit < -1:
                    if unit == -4:
                        denominator += f"{symbol}⁴·"
                    if unit == -3:
                        denominator += f"{symbol}³·"
                    if unit == -2:
                        denominator += f"{symbol}²·"
                    else:
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

derived_units = [
    ( 'Hertz', 'Hz', 'Frequency', Hex(second = -1, meter = 0, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Newton', 'N', 'Force', Hex(second = -2, meter = 1, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Pascal', 'Pa', 'Pressure', Hex(second = -2, meter = -1, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Joule', 'J', 'Energy',  Hex(second = -2, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Watt', 'W', 'Power',  Hex(second = -3, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Coulomb', 'C', 'Electric Charge', Hex(second = 1, meter = 0, kilogram = 0, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Volt', 'V', 'Electric Potential',  Hex(second = -3, meter = 2, kilogram = 1, ampere = -1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Farad', 'F', 'Capacitance', Hex(second = 4, meter = -2, kilogram = -1, ampere = 2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Ohm', 'Ω', 'Resistance',  Hex(second = -3, meter = 2, kilogram = 1, ampere = -2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Siemens', 'S', 'Electrical Conductance', Hex(second = 3, meter = -2, kilogram = -1, ampere = 2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Weber', 'Wb', 'Magnetic Flux', Hex(second = -2, meter = 2, kilogram = 1, ampere = -1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Tesla', 'T', 'Magnetic Flux Density', Hex(second = -2, meter = 0, kilogram = 1, ampere = -1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Henry', 'H', 'Inductance', Hex(second = -2, meter = 2, kilogram = 1, ampere = -2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Lux', 'lx', 'Illuminance', Hex(second = 0, meter = -2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 1)),
    ( 'Becquerel', 'Bq', 'Activity Referred to a Radionuclide', Hex(second = -1, meter = 0, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Gray', 'Gy', 'Absorbed Dose (of Ionizing Radiation)', Hex(second = -2, meter = 2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Sievert', 'Sv', 'Equivalent Dose (of Ionizing Radiation)', Hex(second = -2, meter = 2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Katal', 'kat', 'Catalytic Activity', Hex(second = -1, meter = 0, kilogram = 0, ampere = 0, kelvin = 0, mole = 1, candela = 0)),
    ( 'Square Meter', 'm²', 'Area', Hex(second = 0, meter = 2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Cubic Meter', 'm³', 'Volume', Hex(second = 0, meter = 3, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Meter per Second', 'm/s', 'Velocity', Hex(second = -1, meter = 1, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Meter per Second Squared', 'm/s²', 'Acceleration', Hex(second = -2, meter = 1, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Reciprocal Meter', 'm⁻¹', 'Wavenumber', Hex(second = 0, meter = -1, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Kilogram per Cubic Meter', 'kg/m³', 'Density', Hex(second = 0, meter = -3, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Kilogram per Square Meter', 'kg/m²', 'Surface Density', Hex(second = 0, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Cubic Meter per Kilogram', 'm³/kg', 'Specific Volume', Hex(second = 0, meter = 3, kilogram = -1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Ampere per Square Meter', 'A/m²', 'Current Density', Hex(second = 0, meter = -2, kilogram = 0, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Ampere per Meter', 'A/m', 'Magnetic Field Strength', Hex(second = 0, meter = -1, kilogram = 0, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Mole per Cubic Meter', 'mol/m³', 'Concentration', Hex(second = 0, meter = -3, kilogram = 0, ampere = 0, kelvin = 0, mole = 1, candela = 0)),
    ( 'Kilogram per Cubic Meter', 'kg/m³', 'Mass Concentration', Hex(second = 0, meter = -3, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Candela per Square Meter', 'cd/m²', 'Luminance', Hex(second = 0, meter = -2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 1)),
    ( 'Pascal-Second', 'Pa⋅s', 'Dynamic Viscosity', Hex(second = -1, meter = -1, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Newton-Metre', 'N⋅m', 'Moment of Force', Hex(second = -2, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Newton per Meter', 'N/m', 'Surface Tension', Hex(second = -2, meter = 0, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Radian per Second', 'rad/s', 'Angular Velocity', Hex(second = -1, meter = 0, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Radian per Second Squared', 'rad/s²', 'Angular Acceleration', Hex(second = -2, meter = 0, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Watt per Square Meter', 'W/m²', 'Heat Flux Density',  Hex(second = -3, meter = 0, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Joule per Kelvin', 'J/K', 'Entropy',  Hex(second = -2, meter = 2, kilogram = 1, ampere = 0, kelvin = -1, mole = 0, candela = 0)),
    ( 'Joule per Kilogram-Kelvin', 'J/(kg⋅K)', 'Specific Heat Capacity',  Hex(second = -2, meter = 2, kilogram = 0, ampere = 0, kelvin = -1, mole = 0, candela = 0)),
    ( 'Joule per Kilogram', 'J/kg', 'Specific Energy', Hex(second = -2, meter = 2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Watt per Meter-Kelvin', 'W/(m⋅K)', 'Thermal Conductivity', Hex(second = -3, meter = 1, kilogram = 1, ampere = 0, kelvin = -1, mole = 0, candela = 0)),
    ( 'Joule per Cubic Meter', 'J/m³', 'Energy Density', Hex(second = -2, meter = -1, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Volt per Meter', 'V/m', 'Electric Field Strength', Hex(second = -3, meter = 1, kilogram = 1, ampere = -1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Coulomb per Cubic Meter', 'C/m³', 'Electric Charge Density', Hex(second = 1, meter = -3, kilogram = 0, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Coulomb per Square Meter', 'C/m²', 'Surface Charge Density', Hex(second = 1, meter = -2, kilogram = 0, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Farad per Meter', 'F/m', 'Permittivity', Hex(second = 4, meter = -3, kilogram = -1, ampere = 2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Henry per Meter', 'H/m', 'Permeability', Hex(second = -2, meter = 1, kilogram = 1, ampere = -2, kelvin = 0, mole = 0, candela = 0)),
    ( 'Joule per Mole', 'J/mol', 'Molar Energy', Hex(second = -2, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = -1, candela = 0)),
    ( 'Joule per Mole-Kelvin', 'J/(mol⋅K)', 'Molar Entropy',  Hex(second = -2, meter = 2, kilogram = 1, ampere = 0, kelvin = -1, mole = -1, candela = 0)),
    ( 'Coulomb per Kilogram', 'C/kg', 'Exposure (X- and γ-Rays)', Hex(second = 1, meter = 0, kilogram = -1, ampere = 1, kelvin = 0, mole = 0, candela = 0)),
    ( 'Gray per Second', 'Gy/s', 'Absorbed Dose Rate', Hex(second = -3, meter = 2, kilogram = 0, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Watt per Steradian', 'W/sr', 'Radiant Intensity', Hex(second = -3, meter = 2, kilogram = 1, ampere = 0, kelvin = 0, mole = 0, candela = 0)),
    ( 'Katal per Cubic Meter', 'kat/m³', 'Catalytic Activity Concentration', Hex(second = -1, meter = -3, kilogram = 0, ampere = 0, kelvin = 0, mole = 1, candela = 0)),
]
