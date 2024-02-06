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
   2. [Loops](#loops)
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

Go back to [Contents](#contents).

### Loops

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