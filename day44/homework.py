# Python Syntax

# Write a Python script that prints "Hello, World!"
print("Hello, World!")


# Create a script that takes user input and prints it.
user_input = input("Enter something: ")
print("You entered:", user_input)


# Write a script that uses both single-line and multi-line comments
# single-line comment

"""
This is a multi-line comment.
It consists of multiple lines.
"""


# Write a script that demonstrates indentation in Python.
if 'me' in 'worth is':
    print('you are')
else:
    print('quit atp')


# Write a script that shows how to break lines in Python.
long_string = "a long string " \
              "broken into lines " \
              "by a slash."
print(long_string)



# Python Comments


# Add comments to explain each line of a given script.

# Define a function to add two names
def names(x, y):
    return x, y  # Return the names separatedly

# Call the function and print the result
result = names('nina', 'deme')
print("names:", result)


# add a block comment to describe the script's overall functionality
"""
This script defines a function which has two names as parametr
and prints the result, this two names separated by a coma.
"""

# Use comments to disable a part of the script and re-enable it.
# print("This line is disabled")
print("This line is enabled")


# Write a script with intentional errors and comment on why they occur.
# a = 10
# print(b)  # NameError: b is not defined



# Python Variables

# Create and initialize multiple variables of different data types.
integer_var = 17
float_var = 91.6
string_var = "ara"
boolean_var = True
list_var = [8, 'ki', False]
dict_var = {"song": "pretend", "artist": "alex G"}

# Swap the values of two variables.
a, b = 5, 10
a, b = b, a
print("Swapped values:", a, b)

# Create a script that takes user input to assign values to variables.
user_input = input("Enter a value: ")
variable = user_input
print("You entered:", variable)

# Write a script that uses both global and local variables.
global_var = "I am global"

def function():
    local_var = "I am local"
    print(local_var)
    print(global_var)

function()

# Demonstrate variable naming conventions in Python.
variable = 1
variable_name = 2
variableName = 3


# Python Data Types

# Create variables of types: integer, float, string, and boolean.
integer_var = 10
float_var = 20.5
string_var = "Hello"
boolean_var = True

# Write a script to convert between different data types.
int_to_float = float(126)
float_to_int = int(55)
string_to_int = int("123")
int_to_string = str(31)
print(int_to_float, float_to_int, string_to_int)

# Demonstrate the use of type() function to check variable types.
print(type(7), type(9.1), type('bb'), type(False))

# Perform basic arithmetic operations on different data types.
sum_result = 9 + 9.1
print("Sum:", sum_result)

# Write a script to compare different data types using relational operators.
print(10 == 10.0)  
print(10 > 17)  
print(6<=6)



# Python Numbers

# Write a script to perform arithmetic operations.
a = 15
b = 4
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Create a script that generates a random number.
import random
random_number = random.randint(1, 100)
print("Random number:", random_number)

# Write a script that calculates the square root of a number
import math
square_root = math.sqrt(16)
print("Square root:", square_root)

# Demonstrate the use of math functions like ceil() and floor().
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))

# Write a script to find the greatest common divisor (GCD) of two numbers.
gcd = math.gcd(48, 18)
print("GCD:", gcd)



# Python Casting

# Write a script to convert integers to floats and vice versa.
int_var = 10
float_var = float(int_var)
int_var_again = int(float_var)
print(float_var, int_var_again)

# Create a script to convert strings to integers and floats.
str_int = "123"
str_float = "123.45"
int_from_str = int(str_int)
float_from_str = float(str_float)
print(int_from_str, float_from_str)

# Demonstrate casting between lists and tuples.
list_var = [1, 2, 3]
tuple_var = tuple(list_var)
list_from_tuple = list(tuple_var)
print(tuple_var, list_from_tuple)

# Write a script to handle casting errors.
try:
    invalid_int = int("abc")
except ValueError:
    print("Cannot convert 'abc' to integer")

# Create a script to convert a string representing a number to an integer.
num_str = "456"
num_int = int(num_str)
print(num_int)



# Python Booleans

# Write a script to demonstrate the use of boolean values.
bool_var = True
print("Boolean value:", bool_var)

# Create a script to perform logical operations (and, or, not).
a = True
b = False
print("a and b:", a and b)  # False
print("a or b:", a or b)   # True
print("not a:", not a)     # False

# Demonstrate the use of comparison operators to return boolean values.
print("5 > 3:", 5 > 3)      # True
print("5 == 5:", 5 == 5)   # True
print("5 != 3:", 5 != 3)   # True

# Write a script that uses if-else statements based on boolean values.
if 8 > 9:
    print(True)
else:
    print(False)

# Create a script that returns a boolean result from a function.
def is_even(number):
    return number % 2 == 0

print("Is 4 even?", is_even(4))  # True



# Python Operators

# Write a script that demonstrates arithmetic operators.
x = 10
y = 3
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponentiation:", x ** y)
print("Floor Division:", x // y)

# Create a script to use assignment operators.
z = 5
z += 2  
print("After += operation:", z)
z -= 1  
print("After -= operation:", z)

# Write a script to show the use of comparison operators.
print("7 > 2:", 7 > 2)        # True
print("7 < 2:", 7 < 2)        # False
print("7 >= 7:", 7 >= 7)     # True
print("7 <= 5:", 7 <= 5)     # False

# Demonstrate the use of logical operators in a script.
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("not True:", not True)              # False

# Create a script to use identity operators (is, is not).
a = [1, 2, 3]
b = [1, 2, 3]
print("a is b:", a is b)     # False, because a and b are different objects
print("a is not b:", a is not b)  # True




# Python Lists

# Write a script to create and print a list.
listn = [1, 2, 3, 4, 5]
print("List:", listn)

# Create a script to add and remove elements from a list.
listn.append(6)   
print("List after append:", listn)
listn.pop(3)   
print("List after remove:", listn)

# Write a script to sort a list.
listn.sort()
print("Sorted list:", listn)

# Demonstrate the use of list comprehension.
squares = [x**2 for x in range(5)]
print("List comprehension - squares:", squares)

# Create a script to find the length of a list.
print("Length of the list:", len(listn))



# Python If...Else

# Write a script that uses an if statement to check a condition.
if 'a' in 'banana':
    print("a is in banana")

# Create a script that uses an if-else statement.
if len(listn) > 3:
    print("List has more than 3 elements")
else:
    print("List has 3 or fewer elements")

# Write a script that uses an if-elif-else statement.
value = 10
if value > 10:
    print("Value is greater than 10")
elif value == 10:
    print("Value is 10")
else:
    print("Value is less than 10")

# Demonstrate nested if statements.
num = 15
if num > 10:
    if num < 20:
        print("Number is between 10 and 20")

# Write a script that uses the ternary operator.
x = 10
y = 20

max_value = x if x > y else y

print(max_value)


 
# Python While Loops

# Demonstrate a while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Use a while loop with a break statement
count = 0
while True:
    if count == 2:
        break
    print("Breaking count:", count)
    count += 1

# Use a while loop with a continue statement
count = 0
while count < 3:
    count += 1
    if count == 2:
        continue
    print("Skipping 2, count:", count)

# Demonstrate an infinite loop and how to stop it

# while True:
#     print("This is an infinite loop")

# Use a while loop to iterate over a list
numbers = [1, 2, 3]
i = 0
while i < len(numbers):
    print("Number from list:", numbers[i])
    i += 1



# Python For Loops

# Demonstrate a for loop
for i in range(3):
    print("For loop count:", i)

# Use a for loop to iterate over a list
listx = [1, 2, 3, 4]
for number in listx:
    print("Number from list:", number)

# Use a for loop with the range() function
for i in range(5):
    print("Number from range:", i)

# Demonstrate nested for loops
for i in range(2):
    for j in range(2):
        print(f"Nested loop values: i={i}, j={j}")

# Use a for loop with an else clause
for i in range(3):
    print("Looping through", i)
else:
    print("For loop completed")

# Python Functions

# Define and call a function
def greet(name):
    print("Hello,", name)

greet("Alice")

# Use a function with parameters
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum:", result)

# Use a function with a return value
def multiply(a, b):
    return a * b

product = multiply(4, 5)
print("Product:", product)

# Demonstrate the use of default parameters in a function
def greet(name="Guest"):
    print("Hello,", name)

greet()       # Uses default parameter
greet("Bob")  # Uses provided parameter

# Use a function with keyword arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=30, name="Charlie")  # Keyword arguments



# Basic Arithmetic Operators

# Using all basic arithmetic operators with two numbers
a = 10
b = 5

print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b)  
print("Division:", a / b)        
print("Modulus:", a % b)         
print("Floor Division:", a // b) 
print("Exponentiation:", a ** b) 



# Assignment Operators

# Demonstrating the use of assignment operators
x = 10
x += 5  
print("After += operation:", x)
x -= 3   
print("After -= operation:", x)
x *= 2   
print("After *= operation:", x)
x /= 4   
print("After /= operation:", x)
x %= 3  
print("After %= operation:", x)
x //= 1 
print("After //= operation:", x)
x **= 2  
print("After **= operation:", x)



# Comparison Operators

# Comparing two numbers
num1 = 8
num2 = 12

print("num1 == num2:", num1 == num2)  # ==
print("num1 != num2:", num1 != num2)  # !=
print("num1 > num2:", num1 > num2)    # >
print("num1 < num2:", num1 < num2)    # <
print("num1 >= num2:", num1 >= num2)  # >=
print("num1 <= num2:", num1 <= num2)  # <=



# Logical Operators

# Demonstrating logical operators
x = True
y = False

print("x and y:", x and y)  # and
print("x or y:", x or y)   # or
print("not x:", not x)     # not

# Bitwise Operators

# Showing the use of bitwise operators
a = 10  # 1010 in binary
b = 4   # 0100 in binary

print("a & b:", a & b)  # Bitwise AND
print("a | b:", a | b)  # Bitwise OR
print("a ^ b:", a ^ b)  # Bitwise XOR
print("~a:", ~a)       # Bitwise NOT
print("a << 1:", a << 1)  # Bitwise left shift
print("a >> 1:", a >> 1)  # Bitwise right shift

# Checking if a number is within a specified range
number = 7
lower = 5
upper = 10
print(lower <= number <= upper)  # True if number is between 5 and 10 inclusive


# Identity Operators

# Comparing objects and variables
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)       # False, different objects
print("x is z:", x is z)       # True, same object
print("x is not y:", x is not y)  # True


# Membership Operators

# Checking if a value exists in a list
listn = [1, 2, 3, 4, 5]
print("3 in listn:", 3 in listn)      # True
print("10 not in listn:", 10 not in listn)  # True


# Operator Precedence

# Creating a complex expression to demonstrate operator precedence
result = (5 + 2) * (3 ** 2) / (4 - 1)
print("Complex expression result:", result)

# Taking two user inputs and performing all basic arithmetic operations
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Floor Division:", num1 // num2)
print("Exponentiation:", num1 ** num2)

# Swapping the values of two variables without using a third variable
x = 5
y = 10
x, y = y, x
print("Swapped values: x =", x, "y =", y)


# Lists

# Create a list of five numbers and print the list.
numbers = [1, 2, 3, 4, 5]
print("List of five numbers:", numbers)

# Access elements from a list using positive and negative indexing.
print("First element (positive indexing):", numbers[0])     
print("Last element (positive indexing):", numbers[4])       
print("Last element (negative indexing):", numbers[-1])      
print("Second to last element (negative indexing):", numbers[-2])  

# Add, remove, and update elements in a list.
numbers.append(6)          
print("List after appending 6:", numbers)

numbers.remove(2)        
print("List after removing 2:", numbers)

numbers[1] = 10        
print("List after updating second element to 10:", numbers)

# Concatenate two lists.
more_numbers = [7, 8, 9]
combined_list = numbers + more_numbers
print("Concatenated list:", combined_list)

# Find the length of a list using the len() function.
print("Length of the list:", len(combined_list))

# Check if a specified element is present in a list.
print("Is 10 in the list?", 10 in combined_list)  # True
print("Is 5 in the list?", 5 in combined_list)   # True
print("Is 20 in the list?", 20 in combined_list) # False

# Slice a list and print the sliced list.
print("Sliced list (index 2 to 4):", combined_list[2:5])

# Sort a list in ascending and descending order.
combined_list.sort()
print("List sorted in ascending order:", combined_list)

combined_list.sort(reverse=True)
print("List sorted in descending order:", combined_list)

# Demonstrate the use of list comprehension.
squares = [x**2 for x in range(1, 6)]  # Create a list of squares from 1 to 5
print("List of squares:", squares)

# Find the maximum and minimum values in a list.
print("Maximum value in the list:", max(combined_list))
print("Minimum value in the list:", min(combined_list))

# Reverse the elements of a list.
combined_list.reverse()
print("List after reversing:", combined_list)

# While Loops

# Print numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print("Number:", i)
    i += 1

# Calculate the sum of the first 10 natural numbers using a while loop.
total = 0
i = 1
while i <= 10:
    total += i
    i += 1
print("Sum of the first 10 natural numbers:", total)

# Print the multiplication table of a given number using a while loop.
number = 5
i = 1
print(f"Multiplication table for {number}:")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Find the factorial of a number using a while loop.
number = 4
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"Factorial of {number}:", factorial)

# Print all even numbers between 1 and 50 using a while loop.
i = 1
print("Even numbers between 1 and 50:")
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

# Reverse a given number using a while loop.
number = 12345
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print("Reversed number:", reversed_number)

# Calculate the sum of digits of a number using a while loop.
number = 12345
sum_of_digits = 0
while number > 0:
    sum_of_digits += number % 10
    number //= 10
print("Sum of the digits:", sum_of_digits)

# Find the greatest common divisor (GCD) of two numbers using a while loop.
a = 48
b = 18
while b:
    a, b = b, a % b
print("GCD of 48 and 18:", a)

# Print the Fibonacci sequence up to a specified number using a while loop.
n = 10
a, b = 0, 1
print("Fibonacci sequence up to 10 terms:")
while a < n:
    print(a, end=' ')
    a, b = b, a + b
print()

# Print numbers from 1 to 100, but skip numbers divisible by 5, using a while loop.
i = 1
print("Numbers from 1 to 100, skipping those divisible by 5:")
while i <= 100:
    if i % 5 != 0:
        print(i, end=' ')
    i += 1
print()


# Python For Loops

# Print each element of a list using a for loop.
fruits = ['apple', 'banana', 'cherry']
print("Elements of the list:")
for fruit in fruits:
    print(fruit)

# Print numbers from 1 to 10 using a for loop.
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# Calculate the sum of elements in a list using a for loop.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number
print("\nSum of elements in the list:", sum_of_numbers)

# Print the multiplication table of a given number using a for loop.
number = 5
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Print all even numbers between 1 and 50 using a for loop.
print("\nEven numbers between 1 and 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i)

# Print the Fibonacci sequence up to a specified number using a for loop.
n = 10
a, b = 0, 1
print(f"\nFibonacci sequence up to {n} terms:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
print()

# Iterate over a dictionary and print each key-value pair.
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("\nDictionary key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")

# Find the maximum and minimum values in a list using a for loop.
values = [10, 20, 4, 45, 99]
max_value = values[0]
min_value = values[0]
for value in values:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
print("\nMaximum value:", max_value)
print("Minimum value:", min_value)

# Print each character of a string using a for loop.
string = "hello"
print("\nCharacters of the string:")
for char in string:
    print(char)

# Print the reverse of a list using a for loop.
numbers = [1, 2, 3, 4, 5]
reversed_list = []
for number in numbers:
    reversed_list.insert(0, number)
print("\nReversed list:", reversed_list)

# Use nested for loops to print a pattern, such as a triangle of stars.
print("\nTriangle of stars:")
for i in range(1, 6):
    print('*' * i)



# Python Functions

# Function that takes two numbers as arguments and returns their sum.
def add_numbers(a, b):
    return a + b

print("\nSum of 3 and 4:", add_numbers(3, 4))

# Function that checks if a given number is prime.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Is 7 a prime number?", is_prime(7))

# Function that calculates the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

# Function that returns the largest number in a list.
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

print("Largest number in the list:", find_largest([10, 20, 4, 45, 99]))

# Function that returns the nth Fibonacci number.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print("The 5th Fibonacci number:", fibonacci(5))

# Function that checks if a given string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

print("Is 'radar' a palindrome?", is_palindrome('radar'))

# Function that takes a list and an element as arguments and returns the index of the element in the list.
def find_index(lst, element):
    if element in lst:
        return lst.index(element)
    return -1

print("Index of 'banana' in the list:", find_index(['apple', 'banana', 'cherry'], 'banana'))

# Function that takes a list of numbers and returns a new list with the squares of those numbers.
def square_numbers(numbers):
    return [x ** 2 for x in numbers]

print("Squares of [1, 2, 3, 4, 5]:", square_numbers([1, 2, 3, 4, 5]))

# Function that takes a string and returns the number of vowels in the string.
def count_vowels(s):
    vowels = 'aeiou'
    return sum(1 for char in s.lower() if char in vowels)

print("Number of vowels in 'hello world':", count_vowels('hello world'))

# Function that merges two dictionaries.
def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("\nMerged dictionary:", merge_dicts(dict1, dict2))

# Function that takes a variable number of arguments and returns their sum.
def sum_of_args(*args):
    return sum(args)

print("Sum of 1, 2, 3, 4, 5:", sum_of_args(1, 2, 3, 4, 5))
