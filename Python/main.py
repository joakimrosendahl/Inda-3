from Triangle import Triangle
from Rectangle import Rectangle


def main():
    triangle = Triangle(1, 1, 1)
    print("Triangle type:", triangle.getTriangleType())
    print("Triangle area:", triangle.getArea(), "\n")
    
    rectangle = Rectangle(40, 50)
    print("Rectangle area:", rectangle.getArea())
    print("Rectangle diagonal:", rectangle.getDiagonalLength())
    print("Is rectangle square?", rectangle.isSquare(), "\n")

    rectangle = Rectangle(20, 20)
    print("Rectangle area:", rectangle.getArea())
    print("Rectangle diagonal:", rectangle.getDiagonalLength())
    print("Is rectangle square?", rectangle.isSquare())
main()

