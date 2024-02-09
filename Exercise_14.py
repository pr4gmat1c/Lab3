from Exercise_1 import convert_ounces
print("You are doing Exercise 1")
grams = input("Enter grams:")
convert_ounces(int(grams))

from Exercise_2 import convert_C
print("You are doing Exercise 2")
F = input("Enter Farenheit:")
convert_C(int(F))

from Exercise_3 import solve
print("You are doing Exercise 3")
numheads = input("Enter number of heads:")
numlegs = input("Enter number of legs:")
solve(int(numheads), int(numlegs))

from Exercise_4 import prime
print("You are doing Exercise 4")
numbers = input("Enter numbers:").split(" ")
print(prime(numbers))

from Exercise_5 import permut
print("You are doing Exercise 5")
a = input("Enter a word:")
permut(a)

from Exercise_6 import my_reverse
print("You are doing Exercise 6")
my_reverse()

from Exercise_7 import has_33
print("You are doing Exercise 7")
numbers = input("Enter numbers:").split(" ")
has_33(numbers)

from Exercise_8 import spy_game
print("You are doing Exercise 8")
a = input("Enter numbers:").split(" ")
spy_game(a)

from Exercise_9 import S_volume
print("You are doing Exercise 9")
R = float(input("Enter radius:"))
volume = S_volume(R)

from Exercise_10 import unique_elements
print("You are doing Exercise 10")
list = input("Enter list:").split(" ")
unique_elements(list)

from Exercise_11 import is_palindrome
print("You are doing Exercise 11")
word = input("Enter a word:")
is_palindrome(word)

from Exercise_12 import histogram
print("You are doing Exercise 12")
nums = input("Enter numbers:").split(" ")
histogram(nums)

from Exercise_13 import guess
print("You are doing Exercise 13")
guess()