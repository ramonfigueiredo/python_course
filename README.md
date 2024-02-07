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