import math

class Rectangle: 
    def __init__(self, a, b):
        self._a = a
        self._b = b


    def isSquare(self):
        if self._a == self._b:
            return True
        else:
            return False
  

# redo math for area calculation
    def getDiagonalLength(self):
        diagonal = math.sqrt(self._a * self._a + self._b * self._b)
        return diagonal
    

    def getArea(self):
        area = self._a * self._b
        return area


    

