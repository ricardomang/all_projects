import math

class Circle():
    def __init__(self, diameter):
        self.dia = diameter

    def area_of_circle(self):
        x = float(self.dia/2)
        return x ** 2 * math.pi
        
