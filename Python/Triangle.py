class Triangle: 
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c


    def validTriangle(self):
        if self._a < self._b + self._c and self._b < self._a + self._c and self._c < self._a + self._b:
            return True
        else:
            raise Exception("This is not a valid triangle!")
            


    def getTriangleType(self):
        if self._a == self._b == self._c:
            return "Equilateral Triangle"
        elif self.validTriangle() and (self._a == self._b or self._a == self._c or self._b == self._c):
            return "Isosceles Triangle"
        elif self.validTriangle():
            return "Scalene Triangle"
        else:
            return self.validTriangle()


    

