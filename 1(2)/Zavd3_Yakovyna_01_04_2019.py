class Celsius:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temp(self):
        return self.temperature

class Fahrenheit:
    def __init__(self, temperature):
        self.temperature = temperature

    def to_celsius(self):
        return (self.temperature -32) * 5 / 9

    def get_temp(self):
        return self.temperature

T1 = Celsius(32)
print("T1 in Fahreheit: ", T1.to_fahrenheit())
print("T1 in Celsius: ", T1.get_temp())
T2 = Fahrenheit(32)
print("T2 in Celsius: ", T2.to_celsius())

