Python Course
===========================

by [Ramon Figueiredo](https://ramonfigueiredo.github.io/)

## Contents

1. [Introduction to Python](#introduction-to-python)
   1. [Keywords and Identifiers](#keywords-and-identifiers)
   2. [Comments](#comments)
   3. [Indentation](#indentation)
   4. [Variables](#variables)
   5. [Operators](#operators)
   6. [Input and Output Functions](#input-and-output-functions)
2. [Control Structures](#control-structures)
   1. [Conditional Statements](#conditional-statements)
      1. [More 10 conditional statements examples](#10-conditional-statements-examples)
   2. [Loops](#loops)
      1. [The for loop](#the-for-loop)
      2. [The while loop](#the-while-loop)
      3. [Loop statements - break  - continue - pass](#loop-statements---break---continue---pass)
      4. [More 10 loops examples](#10-loops-examples)
3. [Data Structures](#data-structures)
   1. [Lists and Tuples](#lists-and-tuples)
   2. [Dictionaries](#dictionaries)
   3. [Sets](#sets)
4. [Functions](#functions)
   1. [Defining Functions](#defining-functions)
   2. [Parameters and Return Value](#parameters-and-return-value)
   3. [Scope](#scope)
5. [Error Handling](#error-handling)
   1. [Exceptions](#exceptions)
   2. [Try-Except Block](#try-except-block)
   3. [Finally Clause](#finally-clause)
6. [Intermediate Python](#error-handling)
   1. [Comprehensions](#comprehensions)
   2. [Lambda Functions](#lambda-functions)
   3. [Map and Filter](#map-and-filter)
7. [Object-Oriented Programming](#object-oriented-programming)
   1. [Classes and Objects](#classes-and-objects)
   2. [Inheritance](#inheritance)
   3. [Encapsulation and Polymorphism](#encapsulation-and-polymorphism)
7. [Modules and Packages](#modules-and-packages)
   1. [Modules](#modules)
   2. [Packages](#packages)
   3. [Import Statements](#import-statements)
8. [Working with Files](#working-with-files)
   1. [File Operations](#file-operations)
   2. [File Handling Modes](#file-handling-modes)
   3. [Context Managers](#context-managers)
8. [Python Scripting and Programming](#python-scripting-and-programming)
   1. [Scripting vs Programming](#scripting-vs-programming)
   2. [Automating Tasks](#automating-tasks)
   3. [Best Practices](#best-practices)
9. [Python Libraries](#python-libraries)
   1. [NumPy](#numpy)
   2. [SciPy](#scipy)
   3. [Pandas](#pandas)
   4. [Matplotlib](#matplotlib)
   5. [Seaborn](#seaborn)
   6. [Plotly](#plotly)
   7. [Flask](#flask)
   8. [Django](#django)
   9. [Pillow](#pillow)
   10. [OpenCV](#opencv)
   11. [NLTK](#nltk)
   12. [Scikit-Learn](#scikit-learn)
   13. [TensorFlow](#tensorflow)
   14. [PyTorch](#pytorch)
   15. [Keras](#keras)
10. [Unit Tests in Python](#unit-tests-in-python)
   1. [unittest](#unittest)
   2. [pytest](#pytest)
11. [Conclusion](#conclusion)
   1. [Summary of Key Points](#summary-of-key-points)
   2. [Further Learning Resources](#further-learning-resources)
12. [Contact](#contact)
13. [License](#license)

## Introduction to Python

Go back to [Contents](#contents).

### Keywords and Identifiers

* **Keywords:** Python reserved words (e.g., **if**, **else**, **for**, **while**, **return**).

```python
# Example of using Python keywords
def my_func(n1, n2):
    if n1 < n2:
        return True
    else:
        return False

if __name__ == '__main__':
    n1 = input("Enter a number: ")
    n2 = input("Enter another number: ")
    ans = my_func(n1, n2)
    print('Result: {}'.format(ans))
```

Go back to [Contents](#contents).

* **Identifiers:** Names given to variables, functions, classes, etc.

```python
# Correct identifiers
count = 10
my_variable = "Hello"
class MyClass:
    pass

# Incorrect identifier - starts with a digit
# 1variable = 20  # This will cause a syntax error
```

Go back to [Contents](#contents).

### Comments

* **Comments** start with # and can be used to explain the code.

```python
# This is a single-line comment explaining the next line of code
total = price * quantity  # Calculate total price

"""
This is a multi-line comment
used for longer explanations
or disabling multiple lines of code at once.
"""
```

Go back to [Contents](#contents).

### Indentation

* **Role of Indentation:** Indentation is used to define scopes.

```python
# Correct Indentation
for i in range(5):
    print(i)  # This line is part of the for loop

# Incorrect Indentation - will cause an IndentationError
# for i in range(5):
# print(i)  # This line should be indented
```

Go back to [Contents](#contents).

### Variables

In Python, a variable is like a container that holds data. 
Unlike some languages, Python doesn’t require explicit declaration of the variable type. It's dynamically typed, meaning the type is determined at runtime. 

We have different data types like integers, floating-point numbers, strings, and booleans. Creating a variable in Python is simple – just assign a value to a variable name:

Understanding variables is crucial because they are the basic units for storing and manipulating data in your programs.

```python
count = 10          # An integer
temperature = 25.5  # A floating-point number
name = "Python"     # A string
is_valid = True     # A boolean
```

Go back to [Contents](#contents).

### Operators

Python supports various types of operators, but we'll focus on three main categories: Arithmetic, Comparison, and Logical operators.

* **Arithmetic operators** include addition (+), subtraction (-), multiplication (*), and division (/). These operators are used to perform mathematical operations:

```python
a = 10
b = 5
sum = a + b  # 15
difference = a - b  # 5
product = a * b  # 50
quotient = a / b  # 2.0
```

Go back to [Contents](#contents).

* **Comparison operators**, like equal to (==), not equal to (!=), greater than (>), and less than (<), are used to compare values:

```python
a = 10
b = 5
print(a == b)  # False
print(a > b)   # True
print(a < b)   # False
```

Go back to [Contents](#contents).

* **Logical operators** include AND, OR, and NOT. They are used to combine conditional statements:

```python
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

### Input and Output Functions

Basic input and output are essential for any program to interact with users. In Python, we use the `print()` function for output and the `input()` function for input.

The `print()` function is used to display information to the user:

```python
print("Hello, Python!")
```

The `input()` function is used to take input from the user. Remember, it always returns data as a string:

```python
name = input("Enter your name: ")
print("Hello, " + name)
```

Go back to [Contents](#contents).



## Control Structures

Go back to [Contents](#contents).

### Conditional Statements

In Python, the conditional statements are primarily the 'if', 'elif', and 'else' statements. They allow your program to execute different actions based on certain conditions. 

An 'if' statement checks a condition and executes a block of code if the condition is true. 

The 'elif' (short for 'else if') provides additional conditions to check, and 'else' executes a block of code if none of the previous conditions were true.

Here's a simple example:

```python
age = 18
if age < 18:
    print("Minor")
elif age == 18:
    print("Just turned 18")
else:
    print("Adult")
```

In this example, Python evaluates each condition in turn and executes the block of code under the first true condition.

Go back to [Contents](#contents).

#### More 10 conditional statements examples

Go back to [Contents](#contents).

**Problem 1:** Age Group Categorization

Categorize a person's age group based on their age.

Solution: 

```python
age = int(input("Enter age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
```

Go back to [Contents](#contents).

**Problem 2:** Grading System

Convert numeric grades to letter grades (90-100: A, 80-89: B, etc.).

Solution: 

```python
grade = int(input("Enter your grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

Go back to [Contents](#contents).

**Problem 3:** Leap Year Checker

Check if a year is a leap year.

Solution: 

```python
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

Go back to [Contents](#contents).

**Problem 4:** Smallest of Three Numbers

Find the smallest number among three given numbers.

Solution: 

```python
a, b, c = map(int, input("Enter three numbers: ").split())
if a < b and a < c:
    print(f"The smallest number is {a}")
elif b < c:
    print(f"The smallest number is {b}")
else:
    print(f"The smallest number is {c}")
```

Go back to [Contents](#contents).

**Problem 5:** Eligibility for Voting

Determine if a person is eligible to vote based on their age.

Solution: 

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

Go back to [Contents](#contents).

**Problem 6:** Calculator

Perform basic arithmetic operations (+, -, *, /) based on user input.

Solution: 

```python
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print("Invalid operator")
```

Go back to [Contents](#contents).

**Problem 7:** Odd or Even

Check if a number is odd or even.

Solution: 

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
```

Go back to [Contents](#contents).

**Problem 8:** Password Strength Checker

Check if a password is strong (at least 8 characters, contains a number).

Solution: 

```python
password = input("Enter your password: ")
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is strong.")
else:
    print("Password is weak.")
```

Go back to [Contents](#contents).

**Problem 9:** Traffic Light Simulator

Simulate traffic light actions (Red: Stop, Green: Go, Yellow: Wait).

Solution: 

```python
light = input("Enter traffic light color (Red, Yellow, Green): ").lower()
if light == 'red':
    print("Stop")
elif light == 'yellow':
    print("Wait")
elif light == 'green':
    print("Go")
else:
    print("Invalid color")
```

Go back to [Contents](#contents).

**Problem 10:** Number Classification

Classify a number as positive, negative, or zero.

Solution: 

```python
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```

Go back to [Contents](#contents).

### Loops

Python provides two types of loops - 'for' and 'while'. 

A 'for' loop is used for iterating over a sequence like a list, tuple, string, or range. 

Meanwhile, a 'while' loop repeats as long as a certain boolean condition is met.

Go back to [Contents](#contents).

#### The for loop

Here's how a 'for' loop works:

```python
for i in range(5):
    print(i)
```

This loop prints numbers from 0 to 4. The 'range(5)' function generates a sequence of numbers, which the loop iterates through.

Go back to [Contents](#contents).

#### The while loop

Here's how a 'while' loop works:

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

This loop continues running until 'count' is no longer greater than 0.

Go back to [Contents](#contents).


#### Loop statements - break  - continue - pass
Furthermore, loops can be controlled with 'break', 'continue', and 'pass' statements. 

* 'break' exits the loop
* 'continue' skips to the next iteration
* 'pass' does nothing and is generally used as a placeholder

For example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

This loop will print numbers from 0 to 4. When it reaches 5, the 'break' statement terminates the loop.

Go back to [Contents](#contents).

#### More 10 loops examples

Go back to [Contents](#contents).

**Problem 1:** Sum of Natural Numbers

Find the sum of the first N natural numbers.

Solution: 

```python
n = int(input("Enter N: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of the first {n} natural numbers is {sum}")
```

Go back to [Contents](#contents).

**Problem 2:** Multiplication Table

Print the multiplication table for a given number.

Solution: 

```python
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

Go back to [Contents](#contents).

**Problem 3:** Factorial of a Number

Calculate the factorial of a given number.

Solution: 

```python
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")
```

Go back to [Contents](#contents).

**Problem 4:** Prime Number Check

Check if a number is prime.

Solution: 

```python
num = int(input("Enter a number: "))
is_prime = True
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
```

Go back to [Contents](#contents).

**Problem 5:** Fibonacci Series

Print the first N numbers of the Fibonacci sequence.

Solution: 

```python
n = int(input("Enter the number of Fibonacci terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

Go back to [Contents](#contents).

**Problem 6:** Counting Vowels

Count the number of vowels in a given string.

Solution: 

```python
string = input("Enter a string: ").lower()
count = 0
for char in string:
    if char in "aeiou":
        count += 1
print(f"Number of vowels in the string is {count}")
```

Go back to [Contents](#contents).

**Problem 7:** Number Guessing Game

A simple number guessing game where the user has to guess a number between 1 and 10.

Solution: 

```python
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input("Guess a number between 1 and 10 until you get it right: "))
print("Well guessed!")
```

Go back to [Contents](#contents).

**Problem 8:** Reverse a String

Reverse a given string.

Solution: 

```python
string = input("Enter a string: ")
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print("Reversed String:", reversed_string)
```

Go back to [Contents](#contents).

**Problem 9:** Find the Largest Number in a List

Find the largest number in a list of numbers.

Solution: 

```python
numbers = [3, 6, 2, 8, 4, 10]
largest_num = numbers[0]
for num in numbers:
    if num > largest_num:
        largest_num = num
print("The largest number is:", largest_num)
```

Go back to [Contents](#contents).

**Problem 10:** Exit on Command

Continuously prompt the user for input until they type "exit".

Solution: 

```python
while True:
    command = input("Enter command: ")
    if command.lower() == 'exit':
        break
    else:
        print(f"You entered: {command}")
print("Exited the loop")
```

Go back to [Contents](#contents).

## Data Structures

Go back to [Contents](#contents).

### Lists and Tuples

Go back to [Contents](#contents).

### Dictionaries

Go back to [Contents](#contents).

### Sets

Go back to [Contents](#contents).



## Functions

Go back to [Contents](#contents).

### Defining Functions

Go back to [Contents](#contents).

### Parameters and Return Value

Go back to [Contents](#contents).

### Scope

Go back to [Contents](#contents).



## Error Handling

Go back to [Contents](#contents).

### Exceptions

Go back to [Contents](#contents).

### Try-Except Block

Go back to [Contents](#contents).

### Finally Clause

Go back to [Contents](#contents).



## Intermediate Python

Go back to [Contents](#contents).

### Comprehensions

Go back to [Contents](#contents).

### Lambda Functions

Go back to [Contents](#contents).

### Map and Filter

Go back to [Contents](#contents).



## Object-Oriented Programming

Go back to [Contents](#contents).

### Classes and Objects

Go back to [Contents](#contents).

### Inheritance

Go back to [Contents](#contents).

### Encapsulation and Polymorphism

Go back to [Contents](#contents).



## Modules and Packages

Go back to [Contents](#contents).

### Modules

Go back to [Contents](#contents).

### Packages

Go back to [Contents](#contents).

### Import Statements

Go back to [Contents](#contents).



## Working with Files

Go back to [Contents](#contents).

### File Operations

Go back to [Contents](#contents).

### File Handling Modes

Go back to [Contents](#contents).

### Context Managers

Go back to [Contents](#contents).



## Python Scripting and Programming

Go back to [Contents](#contents).

### Scripting vs Programming

Go back to [Contents](#contents).

### Automating Tasks

Go back to [Contents](#contents).

### Best Practices

Go back to [Contents](#contents).



## Python Libraries

Go back to [Contents](#contents).

### NumPy

Go back to [Contents](#contents).

### SciPy

Go back to [Contents](#contents).

### Pandas

Go back to [Contents](#contents).

### Matplotlib

Go back to [Contents](#contents).

### Seaborn

Go back to [Contents](#contents).

### Plotly

Go back to [Contents](#contents).

### Flask

Go back to [Contents](#contents).

### Django

Go back to [Contents](#contents).

### Pillow

Go back to [Contents](#contents).

### OpenCV

Go back to [Contents](#contents).

### NLTK

Go back to [Contents](#contents).

### Scikit-Learn

Go back to [Contents](#contents).

### TensorFlow

Go back to [Contents](#contents).

### PyTorch

Go back to [Contents](#contents).

### Keras

Go back to [Contents](#contents).



## Unit Tests in Python

Go back to [Contents](#contents).

### unittest

Go back to [Contents](#contents).

### pytest

Go back to [Contents](#contents).



## Conclusion

### Summary of Key Points

### Further Learning Resources

Go back to [Contents](#contents).



## Contact

#### Ramon Figueiredo Pessoa

* LinkedIn: https://www.linkedin.com/in/ramonfigueiredo/
* GitHub: https://ramonfigueiredo.github.io/
* YouTube: www.youtube.com/@ramon-figueiredo

Go back to [Contents](#contents).

## License

[Apache License Version 2.0](https://github.com/ramonfigueiredo/kinematics_analysis_of_diving/blob/master/LICENSE)

Go back to [Contents](#contents).