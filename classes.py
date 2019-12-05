class Color:
    def __init__(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.colors = [self.white, self.red, self.green, self.orange, self.blue, self.purple]
                

class Element:
    def __init__(self, a, b):
        self.value = a
        self.color = b
    
    def print(self):
        print(self.color, str(self.value))
    
    def printable(self):
        val = self.color + str(self.value)
        return val
        
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
    
    def print(self):
        print("(" + self.element.printable() + ", " + self.element2.printable() + ", " + self.element3.printable() + ")")
    
    def printable(self):
        return "(" + self.element.printable() + ", " + self.element2.printable() + ", " + self.element3.printable() + ")"