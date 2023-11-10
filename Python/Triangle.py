class Triangle: 
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c


    def validTriangle(self):
        if self._a < self._b + self._c and self._b < self._a + self._c and self._c < self._a + self._b:
            print("Good triangle")
        else:
            raise Exception("This is not a valid triangle!")


    

