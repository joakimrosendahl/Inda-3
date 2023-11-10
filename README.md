Code assignment like the earlier reposetoreis but this time I will fokus on Java and Python only.




Exercise 3.0 -- A Triangle Object
Create a new class called Triangle.java in the src directory.

The triangle class should have three fields of type int -- the sides a, b and c. Add a constructor that takes one parameter per side of the triangle, setting each sides' value to the corresponding parameter.

The main method of the example below should compile if implemented correctly.

🛠 Main method example
Exercise 3.1 -- The Triangle Inequality
The Triangle Inequality is a popular theorem in mathematics. In simplified terms, it lets you know if three sides, a, b, and, c, can make a triangle. For example, if I give you a = 3, b = 1 and c = 1, you can not make a triangle. An example of valid input is a = 1, b = 1 and c = 1.

Create a method in the Triangle class with the following header private boolean validTriangle(int a, int b, int c), that returns true if the parameters can construct the sides of a triangle, and false in all other cases.

A straightforward approach is checking if the three following relations are true. If they are, then the sides a, b and c, can make a triangle:

drawing

You should put the check at the top of your constructor and try the previous example again:

public Triangle(int a, int b, int c) {
  if(validTriangle(a, b, c)) {
    // Okay to create the Triangle object!
  } else {
    // End the program with an error message
    throw new IllegalArgumentException("This is not a valid triangle!");
  }
}
Assistant's Note: There are various ways to achieve this. Under the Wikipedia page for the Triangle Inequality there are some useful expressions you can use. Although it is not necessary, you may also use the Java Math Library.

Exercise 3.2 -- The three types of Triangles
From the Wikipedia page on Triangles you can read about the three types of triangles. Make a method in the Triangle class called String getTriangleType() that returns a String of what type the triangle is ("Equilateral", "Isosceles" or "Scalene").

Equilateral Triangle	Isosceles Triangle	Scalene Triangle
		
From Wikipedia: Hatch marks, also called tick marks, are used in diagrams of triangles and other geometric figures to identify sides of equal lengths. A side can be marked with a pattern of "ticks", short line segments in the form of tally marks; two sides have equal lengths if they are both marked with the same pattern.

Exercise 3.3 -- Triangle.getArea()
In this exercise, you have to calculate the area of a triangle. Mathematicans have come up with many formulas to achive this, but since our triangle object has the side lengths as fields, we recommend using Heron's Formula. The formula states that the area of a triangle whose sides have lengths a, b and c is

Heron's formula

where s is the semi-perimeter of the triangle:

Semi-perimeter

The method should be called getArea() and returns a double. Test your implementation before you push your solution to GitHub!

📚 How-to: square root (Java Math Library)
Assistant's Note: To use Heron's Formula you need the semi-perimeter s. We suggest you add a helper method, called getPerimeter(), to your Triangle class.

💭 Food for thought
An example of why one would use getters and setters to ensure encapsulation:

Create a triangle with the sides a = 1, b = 1, and, c = 1.
Change a from 1 to 3.
Do you still have a valid triangle?
How would you fix this?
You don't have to provide any answers, but it will be helpful to think about how to solve this with the code you already have.

Exercise 3.4 -- Reverse Engineering
Now that you have created a Triangle class, let's also create a Rectangle class along with some useful methods.

For this exercise, you will not be given detailed instructions. Instead, you will need to read trough the code in the src/RectangleExample file. This code will attempt to create a Rectangle object and call three different methods on it. At the moment, it will not compile and run, since there is no Rectangle.java file, so start by creating this file in your src folder.

You will now need to create the fields, getters, setters and required methods in your Rectangle class that will allow RectangleExample to run and produce the correct results. Your code does not need to cover every edge case, but make sure to run the RectangleExample and check that your methods return the expected values. If you get stuck, don't hesitate to get help through any of the channels listed in the Troubleshooting section.

🐞 Bugs and errors?
If you find any inconsistencies or errors in this exercise, please open a New Issue with the title "Task x Error: summary of error here". Confirmed bugs will be rewarded by mentions in the acknowledgment section.

🙏 Acknowledgment
This task was designed by
Linus Östlund
Sofia Bobadilla
Gabriel Skoglund
Arvid Siberov