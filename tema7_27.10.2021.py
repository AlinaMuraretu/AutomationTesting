# 1. Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of the rectangle.
# Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def Perimeter(self):
#         return 2*(self.length + self.width)
#
#     def Area(self):
#         return self.length * self.width
#
#     def display(self):
#         print('The length of rectangle is: ', self.length)
#         print('The width of rectangle is: ', self.width)
#         print('The perimeter of rectangle is: ', self.Perimeter())
#         print('The area of rectangle is: ', self.Area())
#
# myRectangle = Rectangle(7 , 5)
# myRectangle.display()


# 2. Define a Book class with the following attributes: Title, Author (Full name), Price.
# Set the View() method to display information for the current book.
# Write a program to testing the Book class.

# class Book:
#     def __init__(self, Title, Author, Price):
#         self.Title = Title
#         self.Author = Author
#         self.Price = Price
#
#     def view(self):
#         print('The book(s) title is: ', self.Title)
#         print('The book(s) author is: ', self.Author)
#         print('The book(s) price is: ', self.Price, 'euro')
#
# myBook = Book('Memoirs of a Geisha', 'Arthur Golden', 50)
# myBook.view()


# 3.  Create a Vehicle class with name,  max_speed and mileage instance attributes
# class Vehicle:
#     def __init__(self,name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Asta e mai grea. cat puteti din ea
# :)
# 1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# 2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.
# 3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.
# 4 - Create a method called testPrim() in  the Calculation class to test the primality of a given integer. Test this method.
# 4 - Create  a method called testPrims() allowing to test if two numbers are prime between them.
# 5 - Create a tableMult() method which creates and displays the multiplication table of a given integer.
# Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

class Computation:
    def __init__(self):
        pass
#----Factorial---
    def factorial(self, n):
        j = 1
        for i in range(1, n + 1):
            j = j * i
        return j

# --- Sum of the first n numbers ----
    def sum(self, n):
        j = 0
        for i in range(1, n + 1):
            j = j + i
        return j


# --- Primality test of a number ------------
    def testPrim(self, n):
        if n>1:
            for i in range(2,n):
                if(n%i)==0:
                    return False
            return True
        else:
            return  False

# --- Primality test of two integers ------------
    def testprims(self, n, m):
        # initialize the number of commons divisors
        commonDiv = 0
        for i in range(1, n + 1):
            if (n % i == 0 and m % i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print("The numbers", n, "and", m, "are co-primes")
        else:
            print("The numbers", n, "and", m, "are not co-primes")


# ---Multiplication table-------------
    def tableMult(self, k):
        for i in range(1, 10):
            print(i, "x", k, "=", i * k)

# --- All multiplication tables of the numbers 1, 2, .., 9
    def allTables(self):
        for k in range(1, 10):
            print("\nthe multiplication table of:", k, "is:")
            for i in range(1, 10):
                print(i, "x", k, "=", i * k)

Comput = Computation()
print('The factorial of an integer: ', Comput.factorial(4))
print('The sum of the first n numbers: ', Comput.sum(4))
print('Primality test of a number: ', Comput.testPrim(2))
Comput.testprims(2,6)
Comput.tableMult(2)
Comput.allTables()

