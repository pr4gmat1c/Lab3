import math
# Exercise_1
class IO:
    def getString(self):
        self.str = input("Enter string:")
    def printString(self):
        print(self.str.upper())

pac = IO()
pac.getString()
pac.printString()


# Exercise_2
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

shape = Shape()
print("Area of shape:", shape.area())

square = Square(777)
print("Area of square:", square.area())


# Exercise_3
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(10, 5)
print("Area of rectangle:", rectangle.area())

# Exercise_4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Point is:", self.x, ",", self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

point1 = Point(1, 2)
point2 = Point(3, 4)

point1.show()
point2.show()

point1.move(2, 4)
point1.show()

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)


# Exercise_5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("New balance:", self.balance)
        else:
            print("Too low.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("New balance:", self.balance)
        else:
            print("You are broke")

account = BankAccount("Yerik", 1000000)

account.deposit(250000)
account.withdraw(220000)
account.withdraw(215000)
account.deposit(-210000)


# Exercise_6
def prime(n):
    i = 2
    if n == 1:
        return False
    while n % i != 0:
        i += 1
    if i == n:
        return True
    else:
        return False

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = list(filter(lambda x: prime(x), numbers))

print("Prime numbers:", prime_numbers)
