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
1000. [Contact](#contact)
1001. [License](#license)

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

## Contact

#### Ramon Figueiredo Pessoa

* LinkedIn: https://www.linkedin.com/in/ramonfigueiredo/
* GitHub: https://ramonfigueiredo.github.io/
* YouTube: www.youtube.com/@ramon-figueiredo

Go back to [Contents](#contents).

## License

[Apache License Version 2.0](https://github.com/ramonfigueiredo/kinematics_analysis_of_diving/blob/master/LICENSE)

Go back to [Contents](#contents).