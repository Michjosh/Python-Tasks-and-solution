# rite a Rectangle class that must be instantiated with two attributed:
# length and width. Add a .area() method to the class that
# returns the area (length * width) of the rectangle. Then write
# a Square class that inherits from the Rectangle class and that is
# instantiated with a single attribute called side_length. Test your
# Square class by instantiating a Square with a side_length of 4. Calling
# the .area() method should return 16.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


