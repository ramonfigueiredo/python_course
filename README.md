Python Course - From Beginner to Expert
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
      1. [List](#list)
      2. [Tuple](#tuple)
      3. [More 10 Lists and Tuples examples](#more-10-lists-and-tuples-examples)
   2. [Dictionaries](#dictionaries)
      1. [More 10 Dictionaries examples](#more-10-dictionaries-examples)
   3. [Sets](#sets)
      1. [More 10 Sets examples](#more-10-sets-examples)
4. [Functions](#functions)
   1. [Defining Functions](#defining-functions)
   2. [Parameters and Return Value](#parameters-and-return-value)
   3. [Scope](#scope)
   4. [More 10 Functions examples](#more-10-functions-examples)
5. [Error Handling](#error-handling)
   1. [Exceptions](#exceptions)
   2. [Try-Except Block](#try-except-block)
   3. [Finally Clause](#finally-clause)
   4. [Some Error Handling examples](#some-error-handling-examples)
   5. [More 10 Error Handling examples](#more-10-error-handling-examples)
6. [Intermediate Python](#error-handling)
   1. [Comprehensions](#comprehensions)
      1. [List Comprehensions](#list-comprehensions)
      2. [Dictionary Comprehensions](#dictionary-comprehensions)
      3. [Set Comprehensions](#set-comprehensions)
      4. [Some Comprehensions examples](#some-comprehensions-examples) 
   2. [Lambda Functions](#lambda-functions)
      1. [Lambda Function Example](#lambda-function-example)
      2. [Lambda Functions Usage](#lambda-functions-usage)
      3. [Some Lambda Functions examples](#some-lambda-functions-examples)
   3. [Map and Filter](#map-and-filter)
      1. [The map function](#the-map-function)
      2. [The filter function](#the-filter-function)
      3. [Some Map and Filter examples](#some-map-and-filter-examples)
7. [Object-Oriented Programming](#object-oriented-programming)
   1. [Classes and Objects](#classes-and-objects)
   2. [Class Member Visibility](#class-member-visibility)
      1. [Public Members](#public-members)
      2. [Protected Members](#protected-members)
      3. [Private Members](#private-members)
      4. [Default Visibility](#default-visibility)
      5. [Name mangling in Python](#name-mangling-in-python)
   3. [Inheritance](#inheritance)
   4. [Encapsulation and Polymorphism](#encapsulation-and-polymorphism)
   5. [Abstract Method](#abstract-method)
   6. [Class Method and Static Method](#class-method-and-static-method)
   7. [Property decorators - getter setter deleter](#property-decorators---getter-setter-deleter)
   8. [Some Object-Oriented Programming examples](#some-object-oriented-programming-examples)
8. [Modules and Packages](#modules-and-packages)
   1. [Modules](#modules)
   2. [Packages](#packages)
   3. [Import Statements](#import-statements)
9. [Working with Files](#working-with-files)
   1. [File Operations](#file-operations)
   2. [File Handling Modes](#file-handling-modes)
   3. [Context Managers](#context-managers)
10. [Python Scripting and Programming](#python-scripting-and-programming)
   1. [Scripting vs Programming](#scripting-vs-programming)
   2. [Automating Tasks](#automating-tasks)
   3. [Best Practices](#best-practices)
11. [Python Libraries](#python-libraries)
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
12. [Unit Tests in Python](#unit-tests-in-python)
    1. [unittest](#unittest)
    2. [pytest](#pytest)
13. [Conclusion](#conclusion)
   1. [Summary of Key Points](#summary-of-key-points)
   2. [Further Learning Resources](#further-learning-resources)
14. [Contact](#contact)
15. [License](#license)

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

Next, we will explore some of the most versatile and fundamental data structures in Python: 
* Lists and Tuples
* Dictionaries
* Sets.

Go back to [Contents](#contents).

### Lists and Tuples

Lists and Tuples: Both are used to store collections of items, but they have some key differences. 

Go back to [Contents](#contents).

#### List
  * List is dynamic.
    * It can be altered after its creation, which means you can add, remove, or change items. 
  * Lists are defined by square brackets []

Here's an example:

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an item
print(fruits)
```

Go back to [Contents](#contents).

#### Tuple
*  Tuple is immutable. 
  * Once a tuple is created, you cannot change its contents. 
* Tuples are a great choice when you need a constant set of values throughout your program and are defined by parentheses ().

```python
coordinates = (10.0, 20.0)
print(coordinates)
```

#### More 10 Lists and Tuples examples

**Problem 1:** Concatenating Two Lists

Concatenate (combine) two lists.

Solution: 

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
```

Go back to [Contents](#contents).

**Problem 2:** Finding the Maximum and Minimum in a List

Find the maximum and minimum number in a list.

Solution: 

```python
numbers = [50, 20, 40, 30, 10]
print("Max:", max(numbers))  # Output: Max: 50
print("Min:", min(numbers))  # Output: Min: 10
```

Go back to [Contents](#contents).

**Problem 3:** List Reversal

Reverse the elements of a list.

Solution: 

```python
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```

Go back to [Contents](#contents).

**Problem 4:** Tuple to List Conversion

Convert a tuple into a list.

Solution: 

```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Output: [1, 2, 3]
```

Go back to [Contents](#contents).

**Problem 5:** Slicing a List

Extract a portion of a list.

Solution: 

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced = numbers[2:5]  # Get elements from index 2 to 4
print(sliced)  # Output: [2, 3, 4]
```

Go back to [Contents](#contents).

**Problem 6:** List Element Count

Count the occurrences of an element in a list.

Solution: 

```python
items = ['apple', 'banana', 'cherry', 'apple', 'cherry']
count = items.count('apple')
print("Apple count:", count)  # Output: Apple count: 2
```

Go back to [Contents](#contents).

**Problem 7:** Flattening a Nested List

Flatten a list containing other lists.

Solution: 

```python
nested_list = [[1, 2, 3], [4, 5], [6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
```

Go back to [Contents](#contents).

**Problem 8:** Removing Duplicates from a List

Remove all duplicates from a list.

Solution: 

```python
original_list = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(original_list))
print(unique_list)  # Output: [1, 2, 3, 4]
```

Go back to [Contents](#contents).

**Problem 9:** Sum of Tuple Elements

Calculate the sum of all numbers in a tuple.

Solution: 

```python
numbers_tuple = (1, 2, 3, 4, 5)
total = sum(numbers_tuple)
print("Total:", total)  # Output: Total: 15
```

Go back to [Contents](#contents).

**Problem 10:** Appending an Element to a List

Add an element to the end of a list.

Solution: 

```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
```

Go back to [Contents](#contents).


Go back to [Contents](#contents).

### Dictionaries

Dictionaries in Python are used to store data in key-value pairs.
* Each key is unique and is used to access its corresponding value.
* Dictionaries are highly efficient for looking up and retrieving data. 
* They are defined with curly braces {}.

Here's an example:

```python
student = {"name": "John", "age": 25, "course": "Python"}
print(student["name"])  # Accessing value using key
```

Go back to [Contents](#contents).

#### More 10 Dictionaries examples

**Problem 1:** Creating a Dictionary

Create a dictionary with keys and values.

Solution: 

```python
person = {"name": "John", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

Go back to [Contents](#contents).

**Problem 2:** Accessing Dictionary Values

Access the value of a specific key in a dictionary.

Solution: 

```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

Go back to [Contents](#contents).

**Problem 3:** Adding New Key-Value Pairs

Add a new key-value pair to an existing dictionary.

Solution: 

```python
person = {"name": "Bob", "age": 20}
person["city"] = "London"
print(person)  # Output: {'name': 'Bob', 'age': 20, 'city': 'London'}
```

Go back to [Contents](#contents).

**Problem 4:** Updating Values

Update the value of an existing key in a dictionary.

Solution: 

```python
person = {"name": "Carol", "age": 30}
person["age"] = 31
print(person)  # Output: {'name': 'Carol', 'age': 31}
```

Go back to [Contents](#contents).

**Problem 5:** Removing Key-Value Pairs

Remove a specific key-value pair from a dictionary.

Solution: 

```python
person = {"name": "Dave", "age": 40, "city": "Berlin"}
person.pop("age")
print(person)  # Output: {'name': 'Dave', 'city': 'Berlin'}
```

Go back to [Contents](#contents).

**Problem 6:** Iterating Over a Dictionary

Iterate through the keys and values of a dictionary.

Solution: 

```python
person = {"name": "Eve", "age": 35}
for key, value in person.items():
    print(f"{key}: {value}")
```

Go back to [Contents](#contents).

**Problem 7:** Merging Two Dictionaries

Merge two dictionaries into one.

Solution: 

```python
dict1 = {"name": "Frank", "age": 29}
dict2 = {"city": "Paris", "job": "Engineer"}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'name': 'Frank', 'age': 29, 'city': 'Paris', 'job': 'Engineer'}
```

Go back to [Contents](#contents).

**Problem 8:** Dictionary Comprehension

Create a dictionary from two lists using dictionary comprehension.

Solution: 

```python
keys = ["name", "age", "city"]
values = ["Grace", 32, "Sydney"]
person = {keys[i]: values[i] for i in range(len(keys))}
print(person)  # Output: {'name': 'Grace', 'age': 32, 'city': 'Sydney'}
```

Go back to [Contents](#contents).

**Problem 9:** Checking if Key Exists

Check if a key exists in a dictionary.

Solution: 

```python
person = {"name": "Henry", "age": 27}
if "name" in person:
    print("Name is present.")
```

Go back to [Contents](#contents).

**Problem 10:** Nested Dictionaries

Work with nested dictionaries.

Solution: 

```python
family = {
    "child1": {"name": "Ivy", "age": 5},
    "child2": {"name": "John", "age": 7}
}
print(family["child1"])  # Output: {'name': 'Ivy', 'age': 5}
```

Go back to [Contents](#contents).

### Sets

A set is a collection which is unordered, unchangeable* and unindexed. 
* Sets are written with curly braces. 
* They are ideal for membership testing and eliminating duplicate entries.

**Note:** * When I say 'unchangeable', I mean that while you can add or remove items from a set, you cannot change the items already present.

Here's an example:

```python
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)
```

Go back to [Contents](#contents).

#### More 10 Sets examples

**Problem 1:** Creating a Set

Create a set of numbers.

Solution: 

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}
```

Go back to [Contents](#contents).

**Problem 2:** Adding Elements to a Set

Add an element to an existing set.

Solution: 

```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'banana', 'orange', 'apple', 'cherry'}
```

Go back to [Contents](#contents).

**Problem 3:** Removing Elements from a Set

Remove an element from a set.

Solution: 

```python
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}
```

Go back to [Contents](#contents).

**Problem 4:** Union of Two Sets

Create a union of two sets.

Solution: 

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

Go back to [Contents](#contents).

**Problem 5:** Intersection of Two Sets

Find the intersection of two sets.

Solution: 

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {2, 3}
```

Go back to [Contents](#contents).

**Problem 6:** Difference Between Sets

Find the difference between two sets.

Solution: 

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
```

Go back to [Contents](#contents).

**Problem 7:** Symmetric Difference of Two Sets

Find the symmetric difference of two sets.

Solution: 

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

Go back to [Contents](#contents).

**Problem 8:** Checking for Subset

Check if a set is a subset of another set.

Solution: 

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True
```

Go back to [Contents](#contents).

**Problem 9:** Checking for Superset

Check if a set is a superset of another set.

Solution: 

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True
```

Go back to [Contents](#contents).

**Problem 10:** Clearing a Set

Remove all elements from a set.

Solution: 

```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()
```

Go back to [Contents](#contents).


## Functions

Functions are the building blocks of any Python program. They help you to organize your code into manageable parts and promote code reusability. 

Let's start by understanding how to define and call functions.

Go back to [Contents](#contents).

### Defining Functions

A function in Python is defined using the `def` keyword, followed by the **function name** and parentheses `()`.
* Inside these parentheses, you can pass arguments or parameters that your function can use. 
* After the colon, the indented block of code is the function body. 

Here's a simple example:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function with 'Alice' as an argument
```

This function greet takes one parameter, name, and prints a greeting message using that parameter.

Go back to [Contents](#contents).

### Parameters and Return Value

Functions can return values using the return statement. The return value can be the result of an expression, a value, or a data structure. 

Here's an example:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

In this example, the add function returns the sum of the two arguments a and b.

Go back to [Contents](#contents).

### Scope

The scope of variables in functions refers to where a variable is accessible in your code. 
* **Local variables:** Variables defined inside a function are called local variables and are only accessible within that function. 
* **Global variables:** Variables defined outside of all functions are known as global variables and can be accessed anywhere in your program.

Here's an example to illustrate this:

```python
def my_function():
    local_variable = "I am local"
    print(local_variable)

my_function()
# print(local_variable)  # This would raise an error as local_variable is not accessible here

global_variable = "I am global"

def access_global_variable():
    print(global_variable)

access_global_variable()
```

In this example, `local_variable` is only accessible within my_function, while `global_variable` is accessible globally, even inside `access_global_variable`.

**Notes:** 

* Understanding how to define and use functions, including how to handle parameters, return values, and variable scope, is crucial for efficient and organized Python programming. 
* Functions not only make your code more readable and maintainable but also enable you to avoid repetition and make your programming workflow much more efficient.

Go back to [Contents](#contents).

### More 10 Functions examples

**Problem 1:** Greeting Function

Create a function that greets a user with their name.

Solution: 

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Laura"))  # Output: Hello, Laura!
```

Go back to [Contents](#contents).

**Problem 2:** Adding Two Numbers

Define a function to add two numbers.

Solution: 

```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

Go back to [Contents](#contents).

**Problem 3:** Calculating Area of a Circle

Write a function to calculate the area of a circle given its radius.

Solution: 

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

print(circle_area(5))  # Output: 78.53981633974483
```

Go back to [Contents](#contents).

**Problem 4:** Checking Prime Numbers

Create a function to check if a number is prime.

Solution: 

```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(7))  # Output: True
```

Go back to [Contents](#contents).

**Problem 5:** Finding Maximum in a List

Write a function to find the maximum number in a list.

Solution: 

```python
def find_max(lst):
    return max(lst)

print(find_max([3, 1, 4, 2]))  # Output: 4
```

Go back to [Contents](#contents).

**Problem 6:** Fibonacci Sequence Generator

Create a function that returns the Fibonacci sequence up to N terms.

Solution: 

```python
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
```

Go back to [Contents](#contents).

**Problem 7:** Factorial Calculation

Define a function to calculate the factorial of a number.

Solution: 

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

Go back to [Contents](#contents).

**Problem 8:** Temperature Conversion

Write a function to convert Celsius to Fahrenheit.

Solution: 

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(30))  # Output: 86.0
```

Go back to [Contents](#contents).

**Problem 9:** Counting Vowels in a String

Create a function to count the number of vowels in a string.

Solution: 

```python
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 3
```

Go back to [Contents](#contents).

**Problem 10:** Global and Local Variable Demonstration

Demonstrate the use of local and global variables.

Solution: 

```python
x = "global"

def demo_global_local():
    y = "local"
    print("Inside function:", x, y)  # Accessing global x and local y

demo_global_local()
print("Outside function:", x)  # Accessing global x
# print(y)  # This would raise an error as y is not accessible outside the function
```

Go back to [Contents](#contents).


## Error Handling

Error handling is crucial for creating reliable and user-friendly programs.

Go back to [Contents](#contents).

### Exceptions

In Python, exceptions are errors detected during execution that interrupt the normal flow of a program. 

These could be due to logical errors, like trying to divide by zero, or runtime errors, like attempting to open a file that doesn't exist. 

Exceptions are Python's way of signaling that something has gone wrong.

Go back to [Contents](#contents).

### Try-Except Block

Python provides a try-except block for handle exceptions.
* In the 'try' block, you write code that might cause an exception. 
* In the 'except' block, you handle the exception, providing a response or a fallback action. 

Here's a basic example:

```python
try:
    num = int(input("Enter a number: "))
    inverse = 1 / num
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("The inverse is:", inverse)
```

In this example, if the user enters '0', a ZeroDivisionError is raised, and the except block handles it by printing a message. 

Otherwise, the 'else' block executes, printing the inverse of the number.

Go back to [Contents](#contents).

### Finally Clause

The 'finally' block is optional and is executed no matter what, whether an exception is raised or not. 

It's often used for clean-up actions, such as closing a file or releasing resources.

Here's an example:

```python
try:
    file = open("example.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
```

Here, whether the file opening succeeds or fails, the 'finally' block ensures the file is closed.

Notes:

* Understanding exceptions and how to handle them with try-except blocks, along with the use of the finally clause, is essential for writing resilient Python programs. 
* It allows you to gracefully deal with unexpected situations, maintaining the integrity and reliability of your application.

Go back to [Contents](#contents).

### Some Error Handling examples

Go back to [Contents](#contents).

#### Exceptions

**Problem 1:** Handling a Division by Zero Error

Solution: 

```python
try:
    number = int(input("Enter a number: "))
    result = 1 / number
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"The result is {result}")
```

Go back to [Contents](#contents).

#### Try-Except Block

**Problem 2:** Handling a File Not Found Error

Solution: 

```python
try:
    with open("nonexistent_file.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("Sorry, the file does not exist.")
else:
    print(content)
```

Go back to [Contents](#contents).

#### Finally Clause

**Problem 3:** Using Finally for Cleanup

Solution: 

```python
try:
    file = open("example.txt")
    data = file.read()
    # Process data here
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
```

Go back to [Contents](#contents).

#### Combined Example (Try-Except-Else-Finally)

**Problem 4:** Comprehensive Error Handling Example

Solution: 

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"Result: {result}")
finally:
    print("Operation completed.")
```

Go back to [Contents](#contents).

### More 10 Error Handling examples

**Problem 1:** Division by Zero

Handle the exception when dividing by zero.

Solution: 

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Go back to [Contents](#contents).

**Problem 2:** Invalid Input for Integer Conversion

Handle the exception when input is not an integer.

Solution: 

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not an integer!")
```

Go back to [Contents](#contents).

**Problem 3:** Accessing a Non-existent File

Handle the exception when a file does not exist.

Solution: 

```python
try:
    with open("non_existent_file.txt") as file:
        content = file.read()
except FileNotFoundError:
    print("File does not exist.")
```

Go back to [Contents](#contents).

**Problem 4:** Index Out of Range in a List

Handle the exception for an invalid list index.

Solution: 

```python
try:
    lst = [1, 2, 3]
    print(lst[3])
except IndexError:
    print("Index out of range.")
```

Go back to [Contents](#contents).


**Problem 5:** Key Error in Dictionary Access

Handle the exception when accessing a non-existent dictionary key.

Solution: 

```python
try:
    dict = {'a': 1, 'b': 2}
    print(dict['c'])
except KeyError:
    print("Key not found in the dictionary.")
```

Go back to [Contents](#contents).

**Problem 6:** Handling Multiple Exceptions

Handle different types of exceptions from one try block.

Solution: 

```python
try:
    lst = [1, 2, 3]
    print(lst[3])
    number = int(input("Enter a number: "))
except (IndexError, ValueError) as e:
    print(f"An error occurred: {e}")
```

Go back to [Contents](#contents).

**Problem 7:** Using Finally for Cleanup

Use finally to ensure code execution even after an exception.

Solution: 

```python
try:
    file = open("example.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()
    print("File closed.")
```

Go back to [Contents](#contents).

**Problem 8:** Custom Exception Message

Provide a custom error message for an exception.

Solution: 

```python
try:
    number = int(input("Enter a positive number: "))
    if number <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)
```

Go back to [Contents](#contents).

**Problem 9:** Nested Try-Except Blocks

Use nested try-except blocks for multiple error checks.

Solution: 

```python
try:
    file = open("example.txt")
    try:
        data = file.read()
    except UnicodeDecodeError:
        print("File decoding error.")
    finally:
        file.close()
except FileNotFoundError:
    print("File not found.")
```

Go back to [Contents](#contents).

**Problem 10:** Re-raising an Exception

Catch an exception and then re-raise it for the outer scope.

Solution: 

```python
def process_file():
    try:
        file = open("example.txt")
        data = file.read()
    except FileNotFoundError as e:
        print("Handling error locally.")
        raise e  # Re-raise the exception

try:
    process_file()
except FileNotFoundError:
    print("File not found error caught in the outer scope.")
```

Go back to [Contents](#contents).


## Intermediate Python

As we advance, we'll look at more sophisticated features of Python. 

We'll cover comprehensions, lambda functions, and how to use map and filter. These concepts will elevate your Python skills to a new level.

Go back to [Contents](#contents).

### Comprehensions

Comprehensions in Python provide a concise, readable way to create lists, dictionaries, and sets. They offer a simpler syntax when you want to create a new collection based on the values of an existing collection.

Go back to [Contents](#contents).

#### List Comprehensions

List Comprehensions are a beautiful way to create new lists by applying an expression to each element of an existing iterable. 

For example, let’s say we want to square each number in a list. Here’s how you can do it with a list comprehension:

```python
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

This one-line (`squared = [number ** 2 for number in numbers]`) replaces multiple lines of a traditional `for` loop, making your code compact and readable.

Go back to [Contents](#contents).

#### Dictionary Comprehensions

Moving on to Dictionary Comprehensions, which are similar, but they create dictionaries instead of lists. You can transform and filter data into key-value pairs. 

For example, creating a dictionary where keys are numbers and values are their squares:

```python
numbers = [1, 2, 3, 4, 5]
squared_dict = {number: number ** 2 for number in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Go back to [Contents](#contents).

#### Set Comprehensions

Set Comprehensions work similarly, but are used for creating sets. The syntax is almost identical to list comprehensions, but with curly braces. 

An example can be creating a set of even numbers:

```python
numbers = [1, 2, 3, 4, 5, 2, 3, 4]
evens = {number for number in numbers if number % 2 == 0}
print(evens)  # Output: {2, 4}
```

Notice how duplicates are automatically removed, which is a characteristic of sets.

Go back to [Contents](#contents).

#### Some Comprehensions examples

Go back to [Contents](#contents).

#### Exceptions

**Problem 1:** Square Numbers in Range

Create a list of squares for numbers from 1 to 10.

Solution: 

```python
squares = [x**2 for x in range(1, 11)]
print(squares)
```

Go back to [Contents](#contents).

**Problem 2:** Filter Even Numbers

From a list, create a new list of only even numbers.

Solution: 

```python
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [num for num in original if num % 2 == 0]
print(evens)
```

Go back to [Contents](#contents).

**Problem 3:** Create a Dictionary from Two Lists

Make a dictionary from lists of countries and capitals.

Solution: 

```python
countries = ["Japan", "Canada", "Germany"]
capitals = ["Tokyo", "Ottawa", "Berlin"]
country_capitals = {countries[i]: capitals[i] for i in range(len(countries))}
print(country_capitals)
```

Go back to [Contents](#contents).

**Problem 4:** Invert a Dictionary

Swap keys and values in a dictionary.

Solution: 

```python
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)
```

Go back to [Contents](#contents).

**Problem 5:** Generate a Set of Unique Characters

From a string, create a set of unique characters.

Solution: 

```python
string = "hello world"
unique_chars = {char for char in string}
print(unique_chars)
```

Go back to [Contents](#contents).

**Problem 6:** Square Even Numbers Only

Square only the even numbers in a range.

Solution: 

```python
squared_evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print(squared_evens)
```

Go back to [Contents](#contents).

**Problem 7:** Create a List of Tuples

Generate a list of (number, square of number) tuples.

Solution: 

```python
tuples = [(x, x**2) for x in range(1, 6)]
print(tuples)
```

Go back to [Contents](#contents).

**Problem 8:** List of Lowercase and Uppercase Letters

From a string, create a list of tuples with lowercase and uppercase versions of each letter.

Solution: 

```python
string = "abcd"
letter_cases = [(char, char.upper()) for char in string]
print(letter_cases)
```

Go back to [Contents](#contents).

**Problem 9:** Dictionary of Word-Length

Create a dictionary with words and their lengths from a list of words.

Solution: 

```python
words = ["apple", "banana", "cherry"]
word_length = {word: len(word) for word in words}
print(word_length)
```

Go back to [Contents](#contents).

**Problem 10:** Filter and Transform

From a range of numbers, create a list of strings for even numbers only.

Solution: 

```python
numbers = range(1, 11)
even_str = [f"Even: {num}" for num in numbers if num % 2 == 0]
print(even_str)
```

Go back to [Contents](#contents).

### Lambda Functions

Lambda functions are a distinctive feature of Python, providing a quick and efficient way to create small, unnamed, or 'anonymous' functions. They are particularly useful for short, simple functions that are used only once or a limited number of times.

Let's start by understanding what lambda functions are and how they work. 

- In Python, a lambda function is a small anonymous function defined by the keyword 'lambda'. 
- It can take any number of arguments, but can only have one expression. 

The syntax of a lambda function is:

```python
lambda arguments: expression
```

This expression is evaluated and returned.

Go back to [Contents](#contents).

#### Lambda Function Example

Lambda functions are often used in situations where you need a simple function for a short period and don’t want to formally define it using the standard `def` keyword.

For example, consider a simple lambda function that adds two numbers:

```python
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

In this example, `lambda x, y: x + y` is an anonymous function that takes two arguments and returns their sum. This code assign this lambda function to the variable `add`, and then we can use it just like any other function.

Go back to [Contents](#contents).

#### Lambda Functions Usage

Lambda functions are particularly powerful when used in conjunction with functions like `map()`, `filter()`, and `reduce()`, which allow for functional-style programming. 
* **Functional programming (FP)** is an approach to software development that uses pure functions to create maintainable software. In other words, building programs by applying and composing functions.

For instance, let’s use a lambda function with `map()` to square each number in a list:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

Here, `map()` applies the lambda function to each item in the list numbers.

Go back to [Contents](#contents).

#### Some Lambda Functions examples

Go back to [Contents](#contents).

**Problem 1:** Compute Square of a Number

Create a lambda function to compute the square of a number.

Solution: 

```python
square = lambda x: x**2
print(square(5))  # Output: 25
```

Go back to [Contents](#contents).

**Problem 2:** Add Two Numbers

Use a lambda function to add two numbers.

Solution: 

```python
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10
```

Go back to [Contents](#contents).

**Problem 3:** Filter Even Numbers

Use a lambda function with filter to extract even numbers from a list.

Solution: 

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

Go back to [Contents](#contents).

**Problem 4:** Sort a List of Tuples

Use a lambda function to sort a list of tuples by the second item.

Solution: 

```python
pairs = [(1, 'three'), (3, 'one'), (2, 'two')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(3, 'one'), (2, 'two'), (1, 'three')]
```

Go back to [Contents](#contents).

**Problem 5:** Multiply Elements of a List

Use a lambda function with map to double each element in a list.

Solution: 

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]
```

Go back to [Contents](#contents).

**Problem 6:** Get Maximum of Two Values

Create a lambda function to find the maximum of two values.

Solution: 

```python
max_value = lambda a, b: a if a > b else b
print(max_value(10, 20))  # Output: 20
```

Go back to [Contents](#contents).

**Problem 7:** Concatenate Strings

Use a lambda function to concatenate two strings.

Solution: 

```python
concat = lambda s1, s2: s1 + s2
print(concat("Hello, ", "World!"))  # Output: Hello, World!
```

Go back to [Contents](#contents).

**Problem 8:** Convert Celsius to Fahrenheit

Create a lambda function to convert Celsius to Fahrenheit.

Solution: 

```python
c_to_f = lambda c: (c * 9/5) + 32
print(c_to_f(0))  # Output: 32.0
```

Go back to [Contents](#contents).

**Problem 9:** Find Length of Each Word

Use a lambda function with map to find the length of each word in a list.

Solution: 

```python
words = ["apple", "banana", "cherry"]
lengths = list(map(lambda word: len(word), words))
print(lengths)  # Output: [5, 6, 6]
```

Go back to [Contents](#contents).

**Problem 10:** Reverse a String

Use a lambda function to reverse a string.

Solution: 

```python
reverse_str = lambda s: s[::-1]
print(reverse_str("hello"))  # Output: olleh
```

Go back to [Contents](#contents).

### Map and Filter

Next, let's explore two of Python's built-in functions that incorporate functional programming: `map` and `filter`. 

These functions provide elegant, concise ways to perform operations on iterable collections like lists, tuples, or even strings.

Notes: 

- `map` and `filter` are incredibly useful for handling iterable collections in Python. 
- They enable you to write cleaner, more readable code by abstracting the loop mechanism, making your code more in line with the functional programming paradigm.

Go back to [Contents](#contents).

#### The map function

The `map` function applies a given function to each item of an iterable and returns a map object (which is an iterator). 

Essentially, `map` helps you transform a collection based on a transformation rule. This is particularly useful when you want to apply a single operation to all elements in a collection. 

For example:

```python
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

In this example:

- We have a simple function `square` that we map across a list of numbers. 
- The `map` function applies the square function to each element in numbers.

Go back to [Contents](#contents).

#### The filter function

Moving on to the filter function. Whereas `map` is about transforming data, the `filter` function is about selecting data. 

The `filter` function constructs an iterator from elements of an iterable for which a function returns true. In other words, it filters out all the elements of an iterable, for which the function returns `True`. 

Here's how you can use the `filter` function:

```python
def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

Here, the `filter` function is used to extract even numbers from a list. The function `is_even` returns `True` for even numbers, which are then included in the `even_numbers` list.

Go back to [Contents](#contents).

#### Some Map and Filter examples

The next are some examples that demonstrate the power of `map` and `filter` in transforming and filtering data in lists, utilizing lambda functions for inline processing.

Go back to [Contents](#contents).

**Problem 1:** Convert All Strings in a List to Upper Case

Use `map` to convert each string in a list to upper case.

Solution: 

```python
strings = ["hello", "world", "python"]
upper_strings = list(map(str.upper, strings))
print(upper_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

Go back to [Contents](#contents).

**Problem 2:** Find Length of Each Word

Use `map` to find the length of each word in a list of words.

Solution: 

```python
words = ["apple", "banana", "cherry"]
lengths = list(map(len, words))
print(lengths)  # Output: [5, 6, 6]
```

Go back to [Contents](#contents).

**Problem 3:** Square Each Number

Use `map` to square each number in a list.

Solution: 

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

Go back to [Contents](#contents).

**Problem 4:** Filter Out Negative Numbers

Use `filter` to remove negative numbers from a list.

Solution: 

```python
numbers = [1, -2, 3, -4, 5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # Output: [1, 3, 5]
```

Go back to [Contents](#contents).

**Problem 5:** Extract Names Starting with a Specific Letter

Use `filter` to get names starting with 'J' from a list.

Solution: 

```python
names = ["Jack", "Sarah", "James", "Rachel"]
j_names = list(filter(lambda name: name.startswith('J'), names))
print(j_names)  # Output: ['Jack', 'James']
```

Go back to [Contents](#contents).

**Problem 6:** Convert Temperatures from Celsius to Fahrenheit

Use `map` to convert a list of temperatures from Celsius to Fahrenheit.

Solution: 

```python
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]
```

Go back to [Contents](#contents).

**Problem 7:** Convert Strings to Floats

Use `map` to convert a list of numeric strings to floats.

Solution: 

```python
str_numbers = ["1.2", "2.3", "3.4"]
float_numbers = list(map(float, str_numbers))
print(float_numbers)  # Output: [1.2, 2.3, 3.4]
```

Go back to [Contents](#contents).

**Problem 8:** Remove Empty Strings from a List

Use `filter` to remove empty strings from a list of strings.

Solution: 

```python
strings = ["apple", "", "banana", " ", "cherry"]
non_empty = list(filter(None, strings))
print(non_empty)  # Output: ['apple', 'banana', ' ', 'cherry']
```

Go back to [Contents](#contents).

**Problem 9:** Create a List of Tuples (Number, Square)

Use `map` to create a list of tuples, each containing a number and its square.

Solution: 

```python
numbers = [1, 2, 3, 4, 5]
squared_tuples = list(map(lambda x: (x, x**2), numbers))
print(squared_tuples)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

Go back to [Contents](#contents).

**Problem 10:** Extract Even-Length Words

Use `filter` to get words of even length from a list.

Solution: 

```python
words = ["apple", "banana", "kiwi", "grape"]
even_length_words = list(filter(lambda x: len(x) % 2 == 0, words))
print(even_length_words)  # Output: ['apple', 'banana', 'grape']
```

Go back to [Contents](#contents).

## Object-Oriented Programming

Object-oriented programming, often abbreviated as OOP, is a fundamental programming paradigm used widely in software development. 

OOP concepts provide a structured approach to writing programs.

Let's break down these concepts starting with **Classes** and **Objects**, explain what is member visibility in Python classes and how to use them, then move on to **Inheritance**, and finally discuss **Encapsulation** and **Polymorphism**.

Go back to [Contents](#contents).

### Classes and Objects

In Python, 

- A **class** is a template definition (blueprint) for creating objects.
- **Objects** are instances of classes and can have properties and behaviors, known as **attributes** and **methods**. 

Think of a class as a template for creating individual instances, each with their own specific data and functionality. 

Here's a basic example of a class in Python:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

# Creating an instance of Dog
my_dog = Dog('Rex', 5)
print(my_dog.bark())  # Output: Woof!
```

In this example, `Dog` is a class with attributes (`name` and `age`) and a method (`bark`). The `my_dog` is an object or instance of the `Dog` class.

Go back to [Contents](#contents).

### Class Member Visibility

The visibility of a class member variable or member function determines from where that variable can be accessed/modified or from where the member function can be called. 

In Python, visibility of class members is determined by naming conventions, as opposed to explicit keywords (public, protected, private) found in many other programming languages like Java, C# or C++.

The class member visibility in Python can be public (default), protected, or private.

Go back to [Contents](#contents).

#### Public Members

- Public members can be accessed from inside and outside of their class without any restriction.
- By default, all attributes and methods in a Python class are public.

Example:

```python
class Car:
    def __init__(self):
        self.make = "Tesla"  # Public attribute
        self.model = "Model S"  # Public attribute
    
    def display_info(self):  # Public method
        print(f"This car is a {self.make} {self.model}.")

my_car = Car()
print(my_car.make)  # Accessible
my_car.display_info()  # Accessible
```

Go back to [Contents](#contents).

#### Protected Members

- Protected members are intended to be accessible only from within the class and its subclasses.
- In Python, a member is made protected by prefixing its name with a single underscore `_`
- This is only a convention and is not enforced by Python (except in a very specific scenario involving name mangling).

Example:

```python
class Car:
    def __init__(self):
        self._engine_type = "Electric"  # Protected attribute

class ElectricCar(Car):
    def display_engine_type(self):
        print(f"This car uses a {self._engine_type} engine.")  # Accessible

my_electric_car = ElectricCar()
my_electric_car.display_engine_type()  # Accessible
print(my_electric_car._engine_type)  # Accessible, but not recommended
```

Go back to [Contents](#contents).

#### Private Members

- Private members are intended to be accessible only from within their own class.
- In Python, a member is made private by prefixing its name with two underscores `__`.
- This triggers name mangling, where `_ClassName__memberName` is how the member can be accessed from outside the class.

Example:

```python
class Car:
    def __init__(self):
        self.__vin_number = "1234"  # Private attribute
    
    def display_vin(self):
        print(f"The VIN number is {self.__vin_number}.")  # Accessible

my_car = Car()
my_car.display_vin()  # Accessible
# print(my_car.__vin_number)  # Raises an AttributeError
print(my_car._Car__vin_number)  # Accessible due to name mangling, but not recommended
```

Go back to [Contents](#contents).

#### Default Visibility

As mentioned, in Python, members are public by default. 
- There are no specific keywords to define visibility explicitly. 
- it is all managed through naming conventions (`_` for protected and `__` for private).

These conventions allow for a flexible but clear way to signal the intended visibility of class members. 

However, it's important to note that because Python is a dynamically typed language, these access modifiers are based on a "gentleman's agreement" and can be bypassed if necessary, as seen in the private member access through **name mangling**.

Go back to [Contents](#contents).

#### Name mangling in Python

- A technique used to make a class attribute or method private by prefixing its name with at least two leading underscores and at most one trailing underscore (e.g., `__attribute`). 
- This alters the way the attribute or method is stored in the class namespace, effectively making it inaccessible by its original name from outside the class. 
- Python internally changes the name to `_ClassName__attribute`, allowing class methods to access it while making it less accessible from outside the class.

Go back to [Contents](#contents).

### Inheritance

**Inheritance** allows a new class to inherit attributes and methods from an existing class. 

The new class is called a derived (or child) class, and the class from which it inherits is called the base (or parent) class. 

Inheritance promotes code reuse and establishes a relationship between classes. 

Here's an example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this method")

class Cat(Animal):
    def speak(self):
        return "Meow"

my_cat = Cat("Whiskers")
print(my_cat.speak())  # Output: Meow
```

In this example, `Cat` inherits from `Animal` and implements the speak method.

Go back to [Contents](#contents).

### Encapsulation and Polymorphism

**Encapsulation** involves grouping the data and methods that operate on the data within one unit, like a class. This concept helps in hiding the internal state of the object from the outside. 

**Polymorphism** refers to the way in which different object classes can share the same method name, but those methods can act differently based on which object calls them. 

Here's a brief example:

```python
## The class 'Animal' was defined in previous example
class Bird(Animal):
    def speak(self):
        return "Tweet"

def animal_speak(animal):
    print(animal.speak())

## The next line uses the my_cat object from the previous example
animal_speak(my_cat)  # Output: Meow
animal_speak(Bird("Polly"))  # Output: Tweet
```

In this example, `animal_speak` demonstrates polymorphism by calling the speak method on different animal types.

Go back to [Contents](#contents).

### Abstract Method

An abstract method is a method defined in an abstract base class without an implementation. 

Subclasses inheriting from the abstract base class are required to provide an implementation for the abstract methods. 

Abstract methods are declared using the `@abstractmethod` decorator from the `abc` (Abstract Base Class) module, indicating that the derived class must override this method. 

This mechanism enforces a contract for class hierarchies to ensure certain methods are implemented by child classes.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
```

In this example, any subclass of `Shape` must implement the `area` method, or it will raise an error if instantiated.

Go back to [Contents](#contents).

### Class Method and Static Method

Class methods and static methods are two types of methods that behave differently from regular instance methods.

Go back to [Contents](#contents).

Class Method:
- A class method is a method that is bound to the class rather than its object. It can modify a class state that applies across all instances of the class.
- Class methods take the class as the first argument (conventionally named `cls`) to access or modify class attributes.
- Defined with the `@classmethod` decorator.

Static Method:
- A static method does not depend on the state of the object or class. 
  - It can't access or modify class state.
- Static methods are utility functions that perform a task in isolation. 
  - They don't take a class or instance reference as their first argument.
- Defined with the `@staticmethod` decorator.

Example:

```python
class MyClass:
    _my_var = 5
    
    @classmethod
    def class_method(cls):
        cls._my_var += 1
        return cls._my_var
    
    @staticmethod
    def static_method(value):
        return value * 2

# Usage
print(MyClass.class_method())  # Modifies class state, output: 6
print(MyClass.static_method(3))  # Purely functional, output: 6
```

Go back to [Contents](#contents).

### Property decorators - getter setter deleter

In Python, property decorators are used to define getter, setter, and deleter functions for managing the access to an attribute of a class. 

The `@property` decorator turns a method into a "getter" for a property, allowing you to access the value of a private attribute without directly exposing the attribute itself. 

The `@<property_name>.setter` and `@<property_name>.deleter` decorators are used to define corresponding setter and deleter methods for the property, enabling controlled setting or deletion of the property's value.

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Getter method for name property."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter method for name property."""
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @name.deleter
    def name(self):
        """Deleter method for name property."""
        del self._name

# Usage
person = Person("Alice")
print(person.name)  # Accesses the getter
person.name = "Bob"  # Calls the setter
del person.name  # Calls the deleter
```

This approach provides a way to encapsulate data, ensuring that attributes of a class can be accessed and modified in a controlled manner, such as performing validation or transformation of the data before it's assigned.

Go back to [Contents](#contents).

Notes about a deleter:
- A deleter is used in conjunction with property decorators to manage the deletion of an attribute's value in a controlled manner. 
- The need for a deleter arises in scenarios where simply removing an attribute from an object isn't enough, and additional actions or cleanup operations are required upon deletion. 

Here are some reasons why a deleter might be needed:
- **Resource Management:** 
  - To ensure proper release or cleanup of resources (e.g., closing files or network connections) associated with an attribute when it's no longer needed.
- **Data Integrity:** 
  - To maintain the integrity of related data or states within an object. Deleting an attribute might necessitate updating or validating other attributes.
- **Encapsulation and Safety:** 
  - To prevent direct access to attribute deletion, allowing the class to encapsulate its behavior and ensure that any deletion operation goes through a controlled process.
- **Custom Behavior:** 
  - To implement custom behavior or logic when an attribute is deleted, such as logging, notifying observers, or setting related attributes to default values.
- **Consistency:** 
  - To maintain a consistent interface for accessing and modifying object attributes, providing getters, setters, and deleters ensures a uniform way of interacting with class properties.

Go back to [Contents](#contents).

### Some Object-Oriented Programming examples

Go back to [Contents](#contents).

**Problem 1:** Create a Basic Class and Object

Define a Book class and create an object of that class.

Solution: 

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("2024", "Ramon Figueiredo")
print(book1.title)  # Output: 2024
```

Go back to [Contents](#contents).

**Problem 2:** Class with a Method

Add a method to a class that displays information about an object.

Solution: 

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"Car: {self.make} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.display_info())  # Output: Car: Toyota Corolla
```

Go back to [Contents](#contents).

**Problem 3:** Public Method and Attribute

Solution: 

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Public attribute

    def speak(self):  # Public method
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.name)  # Accessing public attribute
print(my_dog.speak())  # Calling public method
```

Go back to [Contents](#contents).

**Problem 4:** Protected Method and Attribute

Solution: 

```python
class Car:
    def __init__(self, make):
        self._make = make  # Protected attribute

    def _display_make(self):  # Protected method
        return f"This is a {self._make}."

my_car = Car("Tesla")
print(my_car._make)  # Not recommended, but possible
print(my_car._display_make())  # Not recommended, but possible
```

Go back to [Contents](#contents).

**Problem 5:** Private Method and Attribute

Solution: 

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __display_balance(self):  # Private method
        return f"Account balance: ${self.__balance}"

    def public_method(self):
        return self.__display_balance()  # Accessing private method

my_account = Account(1000)
# print(my_account.__balance)  # AttributeError
# print(my_account.__display_balance())  # AttributeError
print(my_account.public_method())  # Accessing private method via public method
```

Go back to [Contents](#contents).

**Problem 6:** Inheritance with Protected Members

Solution: 

```python
class Animal:
    def __init__(self):
        self._legs = 4  # Protected attribute

    def _make_sound(self):  # Protected method
        return "Some sound"

class Dog(Animal):
    def bark(self):
        return self._make_sound()  # Accessing protected method from parent

my_dog = Dog()
print(my_dog.bark())
```

Go back to [Contents](#contents).

**Problem 7:** Name Mangling with Private Members

Solution: 

```python
class Person:
    def __init__(self, age):
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

john = Person(30)
# print(john.__age)  # AttributeError
print(john.get_age())  # Correct way to access private attribute
```

Go back to [Contents](#contents).

**Problem 8:** Changing Protected Member in Subclass

Solution: 

```python
class Vehicle:
    def __init__(self):
        self._wheels = 4  # Protected attribute

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self._wheels = 2  # Changing protected attribute in subclass

my_bike = Bike()
print(my_bike._wheels)  # Accessing changed protected attribute
```

Go back to [Contents](#contents).

**Problem 9:** Using Private Members Across Methods in the Same Class

Solution: 

```python
class Computer:
    def __init__(self):
        self.__os = "Windows"  # Private attribute

    def __update_os(self):  # Private method
        self.__os = "Linux"

    def change_os(self):
        self.__update_os()  # Calling private method
        return f"OS changed to {self.__os}"

my_computer = Computer()
print(my_computer.change_os())
```

Go back to [Contents](#contents).

**Problem 10:** Direct Access to Name Mangled Private Members (Not Recommended)

Solution: 

```python
class Sample:
    def __init__(self):
        self.__privateVar = "I'm private"

sample = Sample()
print(sample._Sample__privateVar)  # Directly accessing a name mangled private variable
```

Go back to [Contents](#contents).

**Problem 11:** Mix of Public, Protected, and Private Members

Solution: 

```python
class MyData:
    def __init__(self):
        self.name = "Public Name"  # Public
        self._data = "Protected Data"  # Protected
        self.__info = "Private Info"  # Private

    def public_method(self):
        return f"Public can access {self.name}, {self._data}, and {self.__info}"

obj = MyData()
print(obj.public_method())  # Accesses all types within the class
```

Go back to [Contents](#contents).

**Problem 12:** Overriding Protected Method in Subclass

Solution: 

```python
class Parent:
    def _protected_method(self):
        return "Parent's protected method"

class Child(Parent):
    def _protected_method(self):
        return "Child's overridden protected method"

child_obj = Child()
print(child_obj._protected_method())  # Accessing overridden protected method
```

Go back to [Contents](#contents).

**Problem 13:** Inheritance

Create a derived class that inherits from a base class.

Solution: 

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak())  # Output: Woof
```

Go back to [Contents](#contents).

**Problem 14:** Multi-level Inheritance

Implement multi-level inheritance.

Solution: 

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    pass

class Parrot(Bird):
    def speak(self):
        return "Squawk"

parrot = Parrot("Polly")
print(parrot.name, parrot.speak())  # Output: Polly Squawk
```

Go back to [Contents](#contents).

**Problem 15:** Multiple Inheritance

Create a class that inherits from two parent classes.

Solution: 

```python
class Father:
    father_name = "John"

class Mother:
    mother_name = "Jane"

class Child(Father, Mother):
    def parents(self):
        return f"Father: {self.father_name}, Mother: {self.mother_name}"

child = Child()
print(child.parents())  # Output: Father: John, Mother: Jane
```

Go back to [Contents](#contents).

**Problem 16:** Encapsulation - Using Private Members

Implement encapsulation using private members.

Solution: 

```python
class Account:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = Account()
account.deposit(100)
print(account.get_balance())  # Output: 100
```

Go back to [Contents](#contents).

**Problem 17:** Polymorphism with Methods

Demonstrate polymorphism with methods.

Solution: 

```python
class Canada:
    def capital(self):
        return "Ottawa"

class USA:
    def capital(self):
        return "Washington"
    
class Brazil:
    def capital(self):
        return "Brasília"

def country_capital(country):
    print(country.capital())

canada = Canada()
usa = USA()
brazil = Brazil()

country_capital(canada)  # Output: Ottawa
country_capital(usa)    # Output: Washington
country_capital(brazil)    # Output: Brasília
```

Go back to [Contents](#contents).

**Problem 18:** Abstract Base Class and Method

Create an abstract class with an abstract method.

Solution: 

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(10, 20)
print(rectangle.area())  # Output: 200
```

Go back to [Contents](#contents).

**Problem 19:** Class Method and Static Method

Use class methods and static methods.

Solution: 

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(20))  # Output: True
print(Person.get_population())  # Output: 0
```

Go back to [Contents](#contents).

**Problem 20:** Property Decorators - Getter and Setter

Use property decorators to define getters and setters.

Solution: 

```python
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible."
                             "\nAbsolute zero, technically known as zero kelvins, "
                             "equals −273.15 degrees Celsius or -459.67 Fahrenheit")
        self._temperature = value

temp = Celsius()
temp.temperature = 30
print(temp.temperature)  # Output: 30

'''
The next two lines throw an ValueError with the message
Temperature below -273.15 is not possible.
Absolute zero, technically known as zero kelvins, equals −273.15 degrees Celsius or -459.67 Fahrenheit
'''
# temp.temperature = -274.5
# print(temp.temperature)  # Output: 30
```

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
* Homepage: https://ramonfigueiredo.github.io/
* GitHub: https://github.com/ramonfigueiredo
* YouTube: www.youtube.com/@ramon-figueiredo

Go back to [Contents](#contents).

## License

[Apache License Version 2.0](https://github.com/ramonfigueiredo/kinematics_analysis_of_diving/blob/master/LICENSE)

Go back to [Contents](#contents).