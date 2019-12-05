class Color:
    def __init__(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[31m'
        
class Element:
    def __init__(self, a, b):
        self.value = a
        self.color = b
        
class Triplet:
    def __init__(self, a, b, c):
        self.element = a
        self.element2 = b
        self.element3 = c
    
    def isSameColor(self):
        if self.element.color == self.element2.color and self.element.color == self.element3.color:
            return True
        else:
            return False
        

color = Color()
element = Element(2, color.green)
element2 = Element(4, color.red)
element3 = Element(1, color.purple)

triplet = Triplet(element, element2, element3)

print(triplet.element.value, "TEST")

if triplet.isSameColor():
    print("Same color")
else:
    print("Not same color")

