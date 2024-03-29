Python Course - From Beginner to Expert
===========================

by [Ramon Figueiredo](https://ramonfigueiredo.github.io/)

## Contents

1. [Introduction to Python](#introduction-to-python)
   1. [Installing Python](#installing-python)
      1. [Installing Python on Windows](#installing-python-on-windows)
      2. [Installing Python on Linux CentOS](#installing-python-on-linux-centos)
      3. [Installing Python on Linux Ubuntu](#installing-python-on-linux-ubuntu)
      4. [Installing Python on macOS](#installing-python-on-macos)
   2. [Package Installer for Python - pip](#package-installer-for-python---pip)
      1. [Some pip commands](#some-pip-commands)
   3. [Setting up a virtual environment](#setting-up-a-virtual-environment)
      1. [venv](#venv)
      2. [virtualenv](#virtualenv)
      3. [conda](#conda)
   4. [Transition from Python 2 to Python 3](#transition-from-python-2-to-python-3)
      1. [Syntax and Code Style](#syntax-and-code-style)
      2. [Performance and Features](#performance-and-features)
      3. [Compatibility and Community](#compatibility-and-community)
      4. [Porting from Python 2 to 3](#porting-from-python-2-to-3)
      5. [Conclusion - This Python Course focus-on Python 3](#conclusion---this-python-course-focus-on-python-3)
   5. [Running Python Code](#running-python-code)
      1. [Running Python code using the Terminal](#running-python-code-using-the-terminal)
      2. [Running Python code using Sublime Text](#running-python-code-using-sublime-text)
      3. [Running Python code using other text editors](#running-python-code-using-other-text-editors)
      4. [Running Python code using Visual Studio Code](#running-python-code-using-visual-studio-code)
      5. [Running Python code using PyCharm](#running-python-code-using-pycharm)
      6. [Running Python code using Google Colab](#running-python-code-using-google-colab)
      7. [Running Python code using Jupiter Notebook](#running-python-code-using-jupiter-notebook)
      8. [Running Python code using Anaconda](#running-python-code-using-anaconda)
   6. [Debugging the Python Code](#debugging-the-python-code)
      1. [Importance of Debugging the Code](#importance-of-debugging-the-code)
      2. [Debugging Code in Visual Studio Code](#debugging-code-in-visual-studio-code)
      3. [Debugging Code in PyCharm](#debugging-code-in-pycharm)
      4. [Python Debugger tool - pdb](#python-debugger-tool---pdb)
2. [Python Basics](#python-basics)
   1. [Keywords](#keywords)
   2. [Identifiers](#identifiers)
   3. [Comments](#comments)
   4. [Indentation](#indentation)
   5. [Variables](#variables)
   6. [Python type annotations](#python-type-annotations)
      1. [Python type annotations - Basic syntax](#python-type-annotations---basic-syntax)
      1. [Python type annotations examples](#python-type-annotations-examples)
   7. [Operators](#operators)
      1. [Arithmetic Operators](#arithmetic-operators)
      2. [Assignment Operators](#assignment-operators)
      3. [Comparison Operators](#comparison-operators)
      4. [Logical Operators](#logical-operators)
      5. [Identity Operators](#identity-operators)
      6. [Membership Operators](#membership-operators)
      7. [Bitwise Operators](#bitwise-operators)
      8. [Examples for each type of operator in Python](#examples-for-each-type-of-operator-in-python)
   8. [Input and Output Functions](#input-and-output-functions)
      1. [The print function](#the-print-function)
      2. [The input function](#the-input-function)
   9. [The Python main function](#the-python-main-function)
      1. [When to Use It](#when-to-use-it)
      2. [Do You Need to Use It](#do-you-need-to-use-it)
3. [Conditional Statements](#conditional-statements)
   1. [More 10 conditional statements examples](#10-conditional-statements-examples)
4. [Loops](#loops)
   1. [The for loop](#the-for-loop)
   2. [The while loop](#the-while-loop)
   3. [Loop statements - break  - continue - pass](#loop-statements---break---continue---pass)
   4. [More 10 loops examples](#10-loops-examples)
5. [Data Structures](#data-structures)
   1. [The length function for data structures](#the-length-function-for-data-structures)
   2. [Lists and Tuples](#lists-and-tuples)
      1. [List](#list)
      2. [Tuple](#tuple)
      3. [More 10 Lists and Tuples examples](#more-10-lists-and-tuples-examples)
   3. [Dictionaries](#dictionaries)
      1. [More 10 Dictionaries examples](#more-10-dictionaries-examples)
   4. [Sets](#sets)
      1. [More 10 Sets examples](#more-10-sets-examples)
   5. [Python Collections Module](#python-collections-module)
      1. [namedtuple](#namedtuple)
         1. [More 10 namedtuple examples](#more-10-namedtuple-examples)
      2. [deque](#deque)
         1. [More 10 deque examples](#more-10-deque-examples)
      3. [ChainMap](#chainmap)
         1. [More 10 ChainMap examples](#more-10-chainmap-examples)
      4. [Counter](#counter)
         1. [More 10 Counter examples](#more-10-counter-examples)
      5. [OrderedDict](#ordereddict)
         1. [More 10 OrderedDict examples](#more-10-ordereddict-examples)
      6. [defaultdict](#defaultdict)
         1. [More 10 defaultdict examples](#more-10-defaultdict-examples)
      7. [UserDict](#userdict)
         1. [More 10 UserDict examples](#more-10-userdict-examples)
      8. [UserList](#userlist)
         1. [More 10 UserList examples](#more-10-userlist-examples)
      9. [UserString](#userstring)
         1. [More 10 UserString examples](#more-10-userstring-examples)
6. [Strings](#strings)
   1. [The length function for Strings](#the-length-function-for-strings)
   2. [String Methods](#string-methods)
7. [Slicing](#slicing)
   1. [List Slicing](#list-slicing)
   2. [Tuple Slicing](#tuple-slicing)
   3. [String Slicing](#string-slicing)
8. [Functions](#functions)
   1. [Defining Functions](#defining-functions)
   2. [Parameters and Return Value](#parameters-and-return-value)
   3. [Scope](#scope)
   4. [More 10 Functions examples](#more-10-functions-examples)
9. [Error Handling](#error-handling)
   1. [Exceptions](#exceptions)
   2. [Try-Except Block](#try-except-block)
   3. [Finally Clause](#finally-clause)
   4. [Some Error Handling examples](#some-error-handling-examples)
   5. [More 10 Error Handling examples](#more-10-error-handling-examples)
10. [Comprehensions](#comprehensions)
    1. [List Comprehensions](#list-comprehensions)
    2. [Dictionary Comprehensions](#dictionary-comprehensions)
    3. [Set Comprehensions](#set-comprehensions)
    4. [Some Comprehensions examples](#some-comprehensions-examples) 
11. [Lambda Functions](#lambda-functions)
    1. [Lambda Function Example](#lambda-function-example)
    2. [Lambda Functions Usage](#lambda-functions-usage)
    3. [Some Lambda Functions examples](#some-lambda-functions-examples)
12. [Map and Filter](#map-and-filter)
    1. [The map function](#the-map-function)
    2. [The filter function](#the-filter-function)
    3. [Some Map and Filter examples](#some-map-and-filter-examples)
13. [Working with Files](#working-with-files)
    1. [File Operations](#file-operations)
    2. [File Handling Modes](#file-handling-modes)
    3. [Context Managers](#context-managers)
14. [Object-Oriented Programming](#object-oriented-programming)
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
15. [Modules and Packages](#modules-and-packages)
    1. [Modules](#modules)
    2. [Packages](#packages)
    3. [Import Statements](#import-statements)
    4. [Why use Modules and Packages](#why-use-modules-and-packages)
16. [Unit Tests in Python](#unit-tests-in-python)
    1. [unittest](#unittest)
    2. [pytest](#pytest)
17. [Python Scripting and Programming](#python-scripting-and-programming)
    1. [Scripting vs Programming](#scripting-vs-programming)
    2. [Automating Tasks](#automating-tasks)
    3. [Some Python Scripting examples](#some-python-scripting-examples)
18. [Python Libraries](#python-libraries)
    1. [The Python Standard Library](#the-python-standard-library)
       1. [sys](#sys)
       2. [os](#os)
       3. [time](#time)
       4. [datetime](#datetime)
       5. [math](#math)
       6. [random](#random)
       7. [collections](#collections)
       8. [json](#json)
       9. [re](#re)
       10. [subprocess](#subprocess)
       11. [threading](#threading)
       12. [urllib](#urllib)
       13. [socket](#socket)
       14. [sqlite3](#sqlite3)
       15. [logging](#logging)
       16. [glob](#glob)
       17. [argparse](#argparse)
    2. [Installing Python Libraries](#installing-python-libraries)
       1. [Step 1 - Ensure Python and pip are Installed](#step-1---ensure-python-and-pip-are-installed) 
       2. [Step 2 - Use pip to Install Libraries](#step-2---use-pip-to-install-libraries)
       3. [Step 3 - Verifying Installation](#step-3---verifying-installation)
       4. [Virtual Environments](#virtual-environments)
    3. [NumPy](#numpy)
       1. [Steps to install and use the Numpy library](#steps-to-install-and-use-the-numpy-library)
       2. [Numpy Examples](#numpy-examples)
    4. [SciPy](#scipy)
       1. [Steps to install and use the SciPy library](#steps-to-install-and-use-the-scipy-library)
       2. [SciPy Examples](#scipy-examples)
    5. [Pandas](#pandas)
       1. [Steps to install and use the Pandas library](#steps-to-install-and-use-the-pandas-library)
       2. [Pandas Examples](#pandas-examples)
    6. [Matplotlib](#matplotlib)
       1. [Steps to install and use the Matplotlib library](#steps-to-install-and-use-the-matplotlib-library)
       2. [Matplotlib Examples](#matplotlib-examples)
    7. [Seaborn](#seaborn)
       1. [Steps to install and use the Seaborn library](#steps-to-install-and-use-the-seaborn-library)
       2. [Seaborn Examples](#seaborn-examples)
    8. [Plotly](#plotly)
       1. [Steps to install and use the Plotly library](#steps-to-install-and-use-the-plotly-library)
       2. [Plotly Examples](#plotly-examples)
    9. [Requests](#requests)
       1. [Steps to install and use the requests library](#steps-to-install-and-use-the-requests-library)
       2. [Requests Examples](#requests-examples)
    10. [Flask](#flask)
        1. [Steps to install and use the Flask library](#steps-to-install-and-use-the-flask-library)
        2. [Flask Examples](#flask-examples)
        3. [Some examples of Flask projects are available on my GitHub account](#some-examples-of-flask-projects-are-available-on-my-github-account)
    11. [Django](#django)
        1. [Steps to install and use the Django library](#steps-to-install-and-use-the-django-library)
        2. [Django Examples](#django-examples)
        3. [Some examples of Django projects are available on my GitHub account](#some-examples-of-django-projects-are-available-on-my-github-account)
    12. [Pillow](#pillow)
        1. [Steps to install and use the Pillow library](#steps-to-install-and-use-the-pillow-library)
        2. [Pillow Examples](#pillow-examples)
    13. Some Python Libraries for Artificial Intelligence - AI
        1. Check out my Machine Learning and Deep Learning courses
            1. [ML 101: Introduction to Machine Learning and Deep Learning - YouTube Video](https://www.youtube.com/watch?v=E3onjLGGBxk)
            2. [Course: ML and DL - Practical code examples - YouTube Playlist](https://www.youtube.com/playlist?list=PLZjc37fQX2kVbZcc8iwm61lJW9fubDEtd)
            3. [Machine Learning in Python - GitHub Repository](https://github.com/ramonfigueiredo/machine_learning_in_python)
        2. [OpenCV](#opencv)
            1. [Steps to install and use the OpenCV library](#steps-to-install-and-use-the-opencv-library)
            2. [OpenCV Examples](#opencv-examples)
            3. [Converting MP4 video to GIF using FFmpeg](#converting-mp4-video-to-gif-using-ffmpeg)
        3. [NLTK](#nltk)
            1. [Steps to install and use the NLTK library](#steps-to-install-and-use-the-nltk-library)
            2. [NLTK Examples](#nltk-examples)
        4. [Scikit-Learn](#scikit-learn)
            1. [Steps to install and use the Scikit-Learn library](#steps-to-install-and-use-the-scikit-learn-library)
            2. [Scikit-Learn Examples](#scikit-learn-examples)
        5. [TensorFlow](#tensorflow)
            1. [Steps to install and use the TensorFlow library](#steps-to-install-and-use-the-tensorflow-library)
            2. [TensorFlow Examples](#tensorflow-examples)
        6. [Keras](#keras)
            1. [Steps to install and use the Keras library](#steps-to-install-and-use-the-keras-library)
            2. [Keras Examples](#keras-examples)
        7. [PyTorch](#pytorch)
            1. [Steps to install and use the PyTorch library](#steps-to-install-and-use-the-pytorch-library)
            2. [PyTorch Examples](#pytorch-examples)
        8. [Gensim](#gensim) 
            1. [Steps to install and use the Gensim library](#steps-to-install-and-use-the-gensim-library)
            2. [Gensim Examples](#gensim-examples)
        9. [OpenAI](#openai)
            1. [Steps to install and use the OpenAI library](#steps-to-install-and-use-the-openai-library)
            2. [OpenAI Examples](#openai-examples)
        10. [LangChain](#langchain)
             1. [Steps to install and use the LangChain library](#steps-to-install-and-use-the-langchain-library)
             2. [LangChain Examples](#langchain-examples)
        11. [MediaPipe](#mediapipe)
             1. [Steps to install and use the MediaPipe library](#steps-to-install-and-use-the-mediapipe-library)
             2. [MediaPipe Examples](#mediapipe-examples)
        12. [Detectron2](#detectron2)
             1. [Steps to install and use the Detectron2 library](#steps-to-install-and-use-the-detectron2-library)
             2. [Detectron2 Examples](#detectron2-examples)
        13. [TF-Graphics](#tf-graphics)
             1. [Steps to install and use the TF-Graphics library](#steps-to-install-and-use-the-tf-graphics-library)
             2. [TF-Graphics Examples](#tf-graphics-examples)
        14. [PyTorch3D](#pytorch3d)
             1. [Steps to install and use the PyTorch3D library](#steps-to-install-and-use-the-pytorch3d-library)
             2. [PyTorch3D Examples](#pytorch3d-examples)
        15. [Keras-GAN](#keras-gan)
             1. [Steps to install and use the Keras-GAN library](#steps-to-install-and-use-the-keras-gan-library)
             2. [Keras-GAN Examples](#keras-gan-examples)
        16. [DALL-E](#dall-e)
             1. [Steps to install and use the DALL-E library](#steps-to-install-and-use-the-dall-e-library)
             2. [DALL-E Examples](#dall-e-examples) 
    14. [How to publish your Python library on Python Package Index](#how-to-publish-your-python-library-on-python-package-index)
19. [Conclusion](#conclusion)
    1. [Summary of Key Points](#summary-of-key-points)
    2. [Further Learning Resources](#further-learning-resources)
20. [Contact](#contact)
21. [License](#license)



## Introduction to Python

Python official website: https://www.python.org/

About the Python programming language:
* Python is a high-level, interpreted programming language known for its simplicity and elegance.
* It is used in various domains, from web development to artificial intelligence.
* One of Python's greatest strengths is its readability, making it an excellent choice for beginners.
* Its extensive libraries and supportive community further enhance its appeal.
* Python is a powerful and versatile language, forming the backbone of many modern technologies and applications.

Go back to [Contents](#contents).



### Installing Python

Installing Python on different operating systems involves a few steps specific to each OS. 

Here's a guide to install Python on Windows, Linux (CentOS and Ubuntu), and macOS:

Go back to [Contents](#contents).


#### Installing Python on Windows

1. Download Python:
- Visit the official Python website at [python.org](https://www.python.org/)
- Click on the "Download Python" button
  - This will download the latest version suitable for Windows

2. Run the Installer:
- Locate the downloaded file and double-click on it to run the installer
- Ensure to check the box that says "Add Python X.X to PATH" at the beginning of the installation process 
- This will add Python to your environment variables and make it accessible from the command line

3. Verify Installation:
- Open Command Prompt and type 

```shell
python --version
```

- You should see the Python version number if the installation was successful

Go back to [Contents](#contents).



#### Installing Python on Linux CentOS

1. Install Using Yum (for CentOS)
- Open the Terminal
- Python might already be installed on your system 
  - You can check by typing `python --version` or `python3 --version`
- To install Python, use the command below
  - Enter your password if prompted

```shell
sudo yum install python3
````

2. Verify Installation:
- Once the installation is complete, verify it by typing `python3 --version`

Go back to [Contents](#contents).



#### Installing Python on Linux Ubuntu

1. Install Using APT (for Ubuntu)
- Open the Terminal
- Update the package list to have the latest versions of the packages and their dependencies:

```shell
sudo apt update
```
  - Then install Python 3 using: 

```shell
sudo apt install python3
```

- Ubuntu typically comes with Python pre-installed
  - You might want to check the version first

2. Verify Installation:
   - Verify the installation by typing `python3 --version`.

Go back to [Contents](#contents).



#### Installing Python on macOS

1. Install Python Using Homebrew

- First, install [Homebrew](https://brew.sh/) if it's not already installed. 
  - In the Terminal, paste:

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

- Once Homebrew is installed, you can install Python by typing the command below
  - This will install the latest version of Python

```shell
brew install python
```

2. Alternatively, Download from [python.org](https://www.python.org/)

- Go to [python.org](https://www.python.org/) and download the macOS Python installer
- Open the installer and follow the instructions to install Python

3. Verify Installation

- Open the Terminal and type `python3 --version` to verify the installation.

Go back to [Contents](#contents).



### Package Installer for Python - pip

The `pip` is the package installer for Python. 
- It is a command-line tool that allows you to install, manage, and uninstall Python packages from the Python Package Index (PyPI) and other package repositories.

Here are some key points about `pip`:

- **Installation:** 
  - The `pip` is typically installed automatically when you install Python. 
  - If you're using a version of Python 3.4 or newer, `pip` should already be available. 
  - For older versions of Python, you may need to install `pip` separately.

- **Usage:** 
  - You can use `pip` from the command line by running commands like `pip install <package_name>` to install packages, `pip uninstall <package_name>` to uninstall packages, and so on.

- **PyPI:** 
  - The [Python Package Index (PyPI)](https://pypi.org/) is the default repository for Python packages. 
  - When you use `pip` to install a package, it looks for the package on PyPI and downloads it if it's available.

- **Dependencies:** 
  - The `pip` automatically installs dependencies for the packages you install. 
  - This means that if a package requires other packages to function properly, `pip` will install those dependencies as well.

- **Virtual Environments:** 
  - The `pip` is often used in conjunction with virtual environments (`venv` or `virtualenv`) to create isolated environments for Python projects. 
  - This allows you to install packages for a specific project without affecting other projects or the system Python installation.

- **Package Management:** 
  - With `pip`, you can manage installed packages, upgrade them to newer versions, uninstall them, and more. 
  - This makes it easy to maintain your Python environment and keep your packages up to date.

Overall, `pip` is an essential tool for Python developers and makes it easy to work with third-party packages and libraries in Python projects.

Go back to [Contents](#contents).



#### Some pip commands

Here are some commonly used pip commands:

1. **Install a Package:** 
   - Use `pip install` followed by the name of the package to install it. 

For example:

```shell
pip install requests
```

2. **Install a Specific Version of a Package:** 
   - Specify the version number using the syntax `<package_name>==<version_number>`. 

For example:

```shell
pip install requests==2.25.1
```

3. **Upgrade a Package:** 
   - Use `pip install --upgrade` followed by the name of the package. 

For example:

```shell
pip install --upgrade requests
```

4. **Uninstall a Package:** 
    - Use `pip uninstall` followed by the name of the package.

For example:

```shell
pip uninstall requests
```

5. **List Installed Packages:** 
   - Use `pip list` to list all installed packages and their versions.

6. **Show Package Information:** 
   - Use `pip show` followed by the name of the package to display information about a specific package. 

For example:

```shell
pip show requests
```

Output:

```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /Users/ramon/Downloads/venv/lib/python3.12/site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:
```

7. **Freeze Installed Packages:**
   - Use `pip freeze` to output a list of installed packages and their versions in a format suitable for `requirements.txt` files.

8. **Install Packages from a Requirements File:** 
   - Use `pip install -r` followed by the path to a `requirements.txt` file to install packages listed in the file

For example:

```shell
pip install -r requirements.txt
```

9. **Download a Package Without Installing:**
   - Use `pip download` followed by the name of the package to download a package and its dependencies without installing them. 

For example:

```shell
pip download requests
```

These commands allow you to manage Python packages using `pip`, the package installer for Python, providing functionality for installation, upgrading, removal, and other package-related tasks.

Go back to [Contents](#contents).



### Setting up a virtual environment

After installing Python, consider setting up a virtual environment for your Python projects to manage dependencies more effectively. 

This can be done using venv (included in the standard library from Python 3.3 onwards):

```
python3 -m venv my_project_env
source my_project_env/bin/activate  # On Windows, use my_project_env\Scripts\activate
```

Using a virtual environment (such as [venv](https://docs.python.org/3/library/venv.html#module-venv), [virtualenv](https://virtualenv.pypa.io/en/latest/) or [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)) after installing Python is recommended for several reasons:

1. **Isolation:** 
   - Virtual environments provide isolated environments for Python projects. 
   - This means that any Python packages installed within a virtual environment are contained within that environment and won't affect other projects or the system-wide Python installation. 
   - This isolation helps avoid conflicts between different project dependencies and ensures reproducibility.

2. **Dependency Management:** 
   - Virtual environments allow you to manage project dependencies independently. 
   - You can install specific versions of Python packages within a virtual environment without affecting other projects. 
   - This makes it easier to manage dependencies and ensures that each project has the required packages and versions.

3. **Version Control:**
   - Virtual environments can be version-controlled along with your project code. 
   - By including the virtual environment directory (usually named venv or env) in your version control system (e.g., Git), you can ensure that anyone working on the project has access to the same environment setup, including the Python version and installed packages.

4. **Clean Environment:** 
   - Virtual environments provide a clean environment for development and testing. 
   - You can create and destroy virtual environments as needed, ensuring that each project starts with a clean slate. 
   - This helps avoid cluttering your system with unnecessary packages and dependencies.

5. **Security:** 
   - Using virtual environments can help improve security by isolating project dependencies from the system-wide Python installation. 
   - This reduces the risk of inadvertently installing malicious or incompatible packages that could compromise system stability or security.

Overall, using virtual environments is considered a best practice in Python development, as it helps manage dependencies, ensures reproducibility, and provides a clean and isolated environment for each project.

Go back to [Contents](#contents).



#### venv

The `venv` is a module in Python that allows you to create lightweight virtual environments for Python projects. 

Virtual environments are isolated from the system-wide Python installation, allowing you to install and manage dependencies specific to your project without affecting other projects or the system itself.

To use `venv`, you can follow these steps:

1. **Create a Virtual Environment:** 
    
- Navigate to your project directory in the terminal and run the following command to create a virtual environment named myenv:

```shell
python3 -m venv myenv
```

This command creates a directory named `myenv` containing the virtual environment.

2. **Activate the Virtual Environment:** 

- Once the virtual environment is created, you need to activate it. 
- In most Unix-based systems (e.g., Linux, macOS), you can activate the virtual environment by running:

```shell
source myenv/bin/activate
```

- On Windows, the activation command is slightly different:

```shell
myenv\Scripts\activate
```

After activation, you should see the name of the virtual environment `(myenv)` prefixed to your command prompt, indicating that the virtual environment is active.

Go back to [Contents](#contents).

3. **Install Dependencies:** 

- With the virtual environment activated, you can use `pip` to install dependencies for your project. 

For example:

```shell
pip install numpy
```

4. **Deactivate the Virtual Environment:** 

- When you're done working on your project, you can deactivate the virtual environment by running:

```shell
deactivate
```

This command returns you to the global Python environment.

Here are some commonly used venv commands:

- **python3 -m venv <name>**
  - Create a new virtual environment with the specified name
- **<venv_dir>/bin/activate** (Unix) or **<venv_dir>\Scripts\activate (Windows)** 
  - Activate the virtual environment
- **deactivate** 
  - Deactivate the virtual environment and return to the global Python environment.
- **python**
  - Launch the Python interpreter within the virtual environment.
- **pip**
  - Use the `pip` package manager within the virtual environment to install, upgrade, or remove Python packages.

Go back to [Contents](#contents).



#### virtualenv

The `virtualenv` (https://virtualenv.pypa.io/en/latest/) is a tool used to create isolated Python environments. 
- It allows you to create separate environments for different Python projects, each with its own set of dependencies, without interfering with the system-wide Python installation or other projects. 
- This is particularly useful when working on multiple projects with conflicting dependencies or when you want to ensure that your project uses specific versions of packages.

The `venv` and `virtualenv` are both tools in Python used to create isolated environments for Python projects, but they have some differences:

- **Built-in vs. Third-party:** 
  - The `venv` is a built-in module in Python 3, while `virtualenv` is a third-party package that needs to be installed separately. 
  - This means that `venv` is included with Python installations by default, while `virtualenv` requires an additional installation step.
- **Python Version Compatibility:** 
  - The `venv` is tightly integrated with the Python installation and may have better compatibility with the specific Python version you're using. 
  - On the other hand, `virtualenv` is more flexible and can be used with different Python versions, including older versions not supported by venv.
- **Features:** 
  - The `virtualenv` provides some additional features and options compared to `venv`, such as creating environments with specific Python interpreter versions or allowing the use of system site packages. 
  - The `virtualenv` also has more options for customizing environment creation, while `venv` is simpler and more straightforward.
- **Maintenance:** 
  - Since `venv` is included with Python, it may receive updates and improvements as part of the standard Python distribution. 
  - However, `virtualenv` is maintained separately, and updates may depend on the efforts of the community or the maintainers of the virtualenv project.

Here's how to use `virtualenv` along with some common commands:

1. **Installation:** 
   - If you don't have `virtualenv` installed, you can install it using `pip`:

```shell
pip install virtualenv
```

2. **Creating a Virtual Environment:**

To create a new virtual environment, navigate to the directory where you want the environment to be created and run:

```shell
virtualenv <env_name>
```
Replace `<env_name>` with the name you want to give to your virtual environment.

3. **Activating the Virtual Environment:** 

Once the virtual environment is created, you need to activate it before using it. 

- On Unix and macOS systems, you can activate the environment using:

```shell
source <env_name>/bin/activate
```

- On Windows, you can activate the environment using:

```shell
<env_name>\Scripts\activate
```

After activation, you should see the name of the virtual environment in your command prompt.

4. **Deactivating the Virtual Environment:** 

To deactivate the virtual environment and return to the global Python environment, simply run:

```shell
deactivate
```

5. **Deleting a Virtual Environment:** 

If you no longer need a virtual environment, you can delete it by removing its directory. 

Be careful with this command as it will permanently delete the virtual environment and all its contents.

```shell
rm -rf <env_name>
```

6. **Listing Installed Packages:** 

You can list all the packages installed in the virtual environment using `pip list`:

```shell
pip list
```

7. **Installing Packages:** 

With the virtual environment activated, you can install packages using `pip` as usual:

```shell
pip install <package_name>
```

Using `virtualenv`, you can create and manage isolated Python environments for your projects, ensuring that each project has its own set of dependencies and avoiding conflicts between packages.

Go back to [Contents](#contents).



#### conda

The `conda` is an open-source package management system and environment management system for installing multiple versions of software packages and their dependencies and managing isolated Python environments. 

It is particularly popular in the data science and machine learning communities due to its ability to easily install and manage complex dependencies required for scientific computing projects.

Here's how to use `conda` along with some common commands:

1. **Installation:** 

- If you don't have conda installed, you can download and install it from the Anaconda website: https://www.anaconda.com/download

2. **Creating a Conda Environment:** 

- To create a new conda environment, use the following command:

```shell
conda create --name <env_name>
```

Replace `<env_name>` with the name you want to give to your environment.

3. **Activating the Conda Environment:** 

Once the environment is created, you need to activate it before using it. 

- On Unix and macOS systems, you can activate the environment using:

```shell
conda activate <env_name>
```

- On Windows, you can activate the environment using:

```shell
activate <env_name>
```

4. **Deactivating the Conda Environment:** 

- To deactivate the conda environment and return to the base environment, you can use:

```shell
conda deactivate
```

5. **Listing Installed Packages:** 

- You can list all the packages installed in the conda environment using:

```shell
conda list
```

6. **Installing Packages:** 

- You can install packages into the conda environment using:

```shell
conda install <package_name>
```

7. **Updating Packages:** 

- To update packages in the environment to the latest versions, you can use:

```shell
conda update <package_name>
```

8. **Removing Packages:** 

- To remove a package from the environment, you can use:

```shell
conda remove <package_name>
```

9. **Exporting Environment:** 

- You can export the environment to a YAML file to recreate it later or on another machine using:

```shell
conda env export > environment.yml
```

10. **Creating Environment from YAML File:** 

To create an environment from a YAML file, you can use:

```shell
conda env create -f environment.yml
```

The `conda` provides a convenient way to manage dependencies and environments for Python projects, making it a popular choice for data scientists, machine learning practitioners, and scientific computing enthusiasts.

Go back to [Contents](#contents).



### Transition from Python 2 to Python 3

The transition from Python 2 to Python 3 is one of the most significant in Python's history, with Python 3 bringing in many changes and improvements over Python 2. 



#### Syntax and Code Style

Here are some of the key differences from Python 2 to Python 3:

1. **Print Statement:**
   - Python 2: print is a statement, e.g., print "Hello". 
   - Python 3: print is a function, e.g., print("Hello").

2. **Unicode Support:**
   - Python 2: Text strings are stored as ASCII by default. Unicode strings are defined with u, e.g., u"Hello".
   - Python 3: Text strings are Unicode by default. Byte strings are defined with b, e.g., b"Hello".

4. **Division of Integers:**
   - Python 2: Dividing integers using / returns an integer. To get a float, you need to use //.
   - Python 3: Dividing integers using / returns a float. To get floor division (integer division), you use //.

5. **Exception Syntax:**
   - Python 2: except Exception, e:
   - Python 3: except Exception as e:

6. **Xrange:**
   - Python 2: Has two range functions: range and xrange, with xrange being more memory efficient for large ranges.
   - Python 3: xrange is removed; range behaves like xrange in Python 2.

Go back to [Contents](#contents).



#### Performance and Features

1. **Python 3 Offers Improved Performance:** 
   - Features like more efficient garbage collection and faster dictionary access have improved overall performance in Python 3.

2. **Modern Libraries and Frameworks:** 
   - Many newer Python libraries and frameworks are developed specifically for Python 3.

3. **Type Hinting:** 
   - Introduced in Python 3.5, type hinting helps with code readability and allows for better static analysis.

Go back to [Contents](#contents).



#### Compatibility and Community

1. **End of Life for Python 2:** 
   - Python 2 reached its end of life in January 2020. 
   - This means it no longer receives updates, not even for security vulnerabilities.

2. **Community and Support:** 
   - The Python community has largely shifted to Python 3, meaning most ongoing development and community support are focused on Python 3.

Go back to [Contents](#contents).



#### Porting from Python 2 to 3

Python 3 is not backward-compatible with Python 2.

Tools like [2to3](https://docs.python.org/3/library/2to3.html) can help in converting Python 2 code to Python 3.

```shell
pip install 2to3
```

Writing code that is compatible with both versions can be challenging, especially for complex projects.

Go back to [Contents](#contents).



#### Conclusion - This Python Course focus-on Python 3

Python 3 is more modern, efficient, and the future of Python. 
- Its enhancements in terms of both language features and performance optimizations make it a preferred choice for Python developers. 
- For any new projects, it is highly recommended to use Python 3. 
- For existing Python 2 projects, planning for migration to Python 3 is advisable considering the end of support for Python 2.

This Python Course focus-on Python 3!

Go back to [Contents](#contents).



### Running Python Code

Running Python code can be done in various environments, including the terminal, using a text editor such as [Sublime Text](https://www.sublimetext.com/), [Visual Studio Code (VSCode)](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [Google Colab](https://colab.google/), [Jupiter Notebook](https://colab.google/), [Anaconda](https://www.anaconda.com/), and more. 

Here's how to run Python in each of these environments:

Go back to [Contents](#contents).



#### Running Python code using the Terminal

1. Open the Terminal:
   - On Windows, open Command Prompt or PowerShell.
   - On macOS or Linux, open the Terminal.

2. Check Python Installation:
   - Type `python --version` or `python3 --version` (depending on how Python is installed on your system) to check if Python is installed.

3. Run Python Code:
   - Navigate to the directory containing your Python script using the `cd` command.
   - Run the script by typing `python script_name.py` or `python3 script_name.py`

Go back to [Contents](#contents).



#### Running Python code using Sublime Text

1. Install Sublime Text: 
   - If you haven't already, download and install [Sublime Text](https://www.sublimetext.com/) from the official website.

2. Install Package Control: 
   - Package Control is a Sublime Text package manager that allows you to easily install additional packages. 
   - You can install it by following the instructions on this page: https://packagecontrol.io/installation

3. Install a Python Build System: 
   - Sublime Text comes with built-in support for various programming languages, including Python. 
   - However, you may need to configure a Python build system to execute your Python scripts directly from Sublime Text.

4. Create a Python Script: 
   - Write your Python code in Sublime Text and save it with a ".py" extension.

5. Configure Build System: 
   - Go to "Tools" > "Build System" and select "Python" as the build system. 
   - If you don't see the "Python" option, you may need to create a custom build system or install a package that provides it.

6. Run the Script: 
   - Once you've selected the Python build system, you can run your Python script by pressing `Ctrl + B` (`Cmd + B` on macOS) or by selecting "Tools" > "Build" from the menu.

7. View Output: 
   - Sublime Text will execute your Python script and display the output in the Sublime Text console at the bottom of the window.

Go back to [Contents](#contents).



#### Running Python code using other text editors

Running Python code using various text editors involves similar principles across different platforms. 

Here's a general guide on how to run Python code using some popular text editors:

1. [Vim](https://www.vim.org/):
   - Open your Python script in Vim.
   - Press ":" to enter command mode, then type "w" to save the file.
   - Use ":!" followed by "python" and the name of your script to execute it. For example: `:!python script.py`

2. [Vi](https://www.redhat.com/sysadmin/introduction-vi-editor):
   - Open your Python script in Vi.
   - Press "Esc" to exit insert mode.
   - Type ":w" to save the file.
   - Use ":!" followed by "python" and the name of your script to execute it. For example: `:!python script.py`

3. [Nano](https://www.nano-editor.org/):
   - Open your Python script in Nano.
   - Press "Ctrl + O" to save the file.
   - Press "Ctrl + X" to exit Nano.
   - Use the terminal to run the script. 
   - Navigate to the directory containing the script and run `python script.py`

For any text editor:
   - Create a Python script.
   - Save the file.
   - Use the terminal to navigate to the directory containing the script.
   - Run `python script.py` to execute the script.

Remember, these are general steps, and the actual commands may vary slightly depending on your operating system and configuration. 

Additionally, you'll need to have Python installed on your system to execute Python scripts.

Go back to [Contents](#contents).



#### Running Python code using Visual Studio Code

1. Install [Visual Studio Code (VSCode)](https://code.visualstudio.com/):
   - Download and install Visual Studio Code from the official website: https://code.visualstudio.com/

2. Install Python Extension:
   - Open VSCode, go to Extensions (sidebar), and search for the Python extension. 
   - Install the extension by Microsoft.

3. Open or Create a Python File:
   - Open an existing Python file or create a new one and save it with the `.py` extension.

4. Select Python Interpreter:
   - Click on the Python version in the bottom-right corner of the window, or use the command palette (`Ctrl+Shift+P` on Windows/Linux, `Cmd+Shift+P` on macOS) and type `Python: Select Interpreter`. 
   - Choose the appropriate Python interpreter if you have multiple versions installed.

5. Run the Code:
   - You can run the script by clicking the green play button in the top-right corner of the editor window.
   - Alternatively, you can right-click in the editor and select "Run Python File in Terminal".

Go back to [Contents](#contents).



#### Running Python code using PyCharm

1. Install PyCharm:
   - Download and install [PyCharm](https://www.jetbrains.com/pycharm/) from the JetBrains website. 
   - Both a community (free) and a professional (paid) version are available.

2. Create or Open a Project:
   - Open PyCharm and either create a new project or open an existing one.

3. Configure Python Interpreter:
   - Go to `File` > `Settings` (or `PyCharm` > `Preferences` on macOS), then `Project` > `Project Interpreter`. 
   - Select the Python interpreter you would like to use from the list, or add a new one.

4. Run the Code:
   - Open a Python file in the project. Right-click in the editor and choose Run 'filename' to run the script.
   - Alternatively, use the green play button in the top-right corner of the editor window.

Go back to [Contents](#contents).



#### Running Python code using Google Colab

To run Python code using [Google Colab](https://colab.google/), follow these steps:

1. Open Google Colab:
   - Go to https://colab.research.google.com/ to access Google Colab.

2. Create or Open a Notebook:
   - You can either create a new notebook by clicking on "File" > "New notebook" or open an existing notebook by uploading it or selecting it from Google Drive.

3. Write or Paste Python Code:
   - In a code cell, write or paste your Python code.

4. Run Code Cells:
   - To execute a code cell, click on the "Play" button next to the cell, or press "Shift + Enter" after selecting the cell. 
   - Alternatively, you can run all cells in the notebook by clicking on "Runtime" > "Run all" or pressing "Ctrl + F9".

5. View Output:
   - Output, including print statements, plots, and error messages, will appear below the corresponding code cell.

6. Interact with Code:
   - You can edit and rerun code cells as needed. 
   - Colab notebooks allow for interactive coding and data analysis.

7. Save and Share:
   - Save your changes by clicking on "File" > "Save" or pressing "Ctrl + S".
   - You can share the notebook with others by clicking on "Share" in the top right corner and providing the appropriate permissions.

Google Colab provides a free and convenient environment for running Python code, especially for data analysis, machine learning, and collaborative projects.

Go back to [Contents](#contents).



#### Running Python code using Jupiter Notebook

To run Python code using [Jupiter Notebook](https://jupyter.org/), follow these steps:

1. Launch Jupyter Notebook:
   - Open your terminal (Command Prompt on Windows or Terminal on macOS/Linux).
   - Type `jupyter notebook` and press Enter.
   - This will launch the Jupyter Notebook interface in your default web browser.

2. Create a New Notebook:
   - In the Jupyter Notebook interface, click on the "New" button in the top-right corner.
   - Select "Python" under the "Notebook" section to create a new Python notebook.

3. Write or Paste Python Code:
   - In the first cell of the notebook, write or paste your Python code.
   - You can add new cells by clicking on the "+" button in the toolbar or by pressing "Esc" followed by "B" on your keyboard.

4. Run Code Cells:
   - To execute a code cell, select the cell by clicking on it, then press "Shift + Enter" on your keyboard.
   - Alternatively, you can click on the "Run" button in the toolbar or select "Cell" > "Run Cells" from the menu.

5. View Output:
   - Output, including print statements, plots, and error messages, will appear below the corresponding code cell.

6. Interact with Code:
   - You can edit and rerun code cells as needed. 
   - Jupyter Notebooks allow for interactive coding and data analysis.

7. Save and Export:
   - Save your changes by clicking on "File" > "Save and Checkpoint" or pressing "Ctrl + S".
   - You can export the notebook to various formats, such as HTML, PDF, or Python script, by selecting "File" > "Download as" from the menu.

In addition to Jupyter Notebook and JupyterLab, Anaconda provides several other tools that you can use to run your Python code effectively. 

Here are some of the key tools:

- **Spyder:**
  - Spyder is an integrated development environment (IDE) designed specifically for scientific computing and data analysis. 
  - It provides a powerful code editor, interactive console, and variable explorer, making it suitable for tasks ranging from simple scripting to complex data manipulation.

- QtConsole:
  - QtConsole is an enhanced interactive Python shell that is part of the IPython project. 
  - It features syntax highlighting, tab completion, and inline plotting capabilities, making it a versatile tool for exploring and testing code interactively.

- Anaconda Prompt (Windows) / Terminal (macOS and Linux):
  - Anaconda Prompt (or Terminal on macOS and Linux) is a command-line interface that allows you to manage Python environments and packages using conda and `pip` commands. 
  - You can create, activate, and deactivate virtual environments, install packages, and run Python scripts directly from the command line.

- Navigator:
  - Anaconda Navigator is a graphical user interface (GUI) that provides a convenient way to manage your Python environments, packages, and applications. 
  - It allows you to launch various tools and applications, such as Jupyter Notebook, Spyder, and QtConsole, as well as manage your environments and packages with ease.

- VS Code with Anaconda Extension:
  - Visual Studio Code (VS Code) is a popular code editor that supports various programming languages, including Python. 
  - With the Anaconda Extension installed, you can access features such as IntelliSense code completion, linting, debugging, and Jupyter Notebooks directly within VS Code, providing a seamless development experience.

- PyCharm with Anaconda Plugin:
  - PyCharm is a powerful IDE for Python development that offers features such as code analysis, debugging, version control integration, and support for web development frameworks. 

By installing the Anaconda plugin, you can seamlessly integrate Anaconda environments and packages into PyCharm, enhancing your development workflow.

By leveraging these tools available within Anaconda, you can choose the one that best suits your workflow and preferences to effectively run and manage your Python code projects. 

Each tool offers unique features and capabilities tailored to different use cases, ensuring a smooth and efficient development experience.

Go back to [Contents](#contents).



#### Running Python code using Anaconda

To run Python code using [Anaconda](https://www.anaconda.com/), you can follow these steps:

1. Launch Anaconda Navigator:
   - Open Anaconda Navigator from your system's applications or by searching for it in the Start menu (Windows) or Spotlight search (macOS).

2. Open a Python Environment:
   - Once Anaconda Navigator opens, you'll see a list of environments on the left sidebar.
   - Select the Python environment in which you want to run your code. 
   - If you don't have a specific environment, you can use the "base" environment.

3. Launch Jupyter Notebook or JupyterLab:
   - With your chosen environment selected, click on the "Launch" button next to Jupyter Notebook or JupyterLab.
   - This will open a new tab in your default web browser with the Jupyter interface.

4. Navigate to Your Working Directory:
   - In the Jupyter interface, navigate to the directory where your Python code is located. 
   - You can use the file browser on the left side.

5. Create a New Notebook or Open an Existing One:
   - If you want to create a new notebook, click on the "New" button and select "Python 3" under the "Notebook" section.
   - If you already have a notebook containing your Python code, click on it to open it.

6. Run Python Code Cells:
   - In the notebook, you'll see code cells where you can write or paste your Python code.
   - To execute a code cell, select it by clicking on it, then press "Shift + Enter" on your keyboard. 
   - Alternatively, you can click the "Run" button in the toolbar.
   - Output, including print statements and any visualizations, will appear below the code cell.

7. Interact with Code:
   - You can edit and rerun code cells as needed. 
   - Jupyter notebooks allow for interactive coding and data analysis.

8. Save and Export:
   - Save your changes by clicking on "File" > "Save and Checkpoint" in the notebook interface.
   - You can export the notebook to various formats, such as HTML, PDF, or Python script, by selecting "File" > "Download as" from the menu.

By following these steps, you can easily run Python code using Anaconda and Jupyter Notebook or JupyterLab, which provides an interactive environment for data exploration, visualization, and analysis.

Go back to [Contents](#contents).



### Debugging the Python Code

Debugging is the process of identifying and removing errors, or "bugs," from software code. 

It involves finding the cause of unexpected behavior or crashes in your program and fixing these issues to make the code run correctly and efficiently.

Debugging is a crucial part of the development process. 
- Tools provided by VSCode and PyCharm greatly simplify the debugging process by providing a user-friendly interface to step through code, inspect variables, and evaluate expressions. 
- These capabilities are invaluable for both identifying and solving problems in your code.

Go back to [Contents](#contents).



#### Importance of Debugging the Code

1. **Correctness:** 
   - Ensuring that the code works as intended and produces the correct output.

2. **Quality and Reliability:** 
   - Debugged code is more reliable and less likely to cause crashes or incorrect results.

3. **Performance:** 
   - Debugging can help identify and fix performance bottlenecks, making the code faster and more efficient.

4. **Maintainability:** 
   - Well-debugged code is generally cleaner and easier to understand, which makes future maintenance easier.

5. **Learning Opportunity:** 
   - The debugging process can be a learning experience, helping developers understand their code better and improving their coding skills.

Go back to [Contents](#contents).



#### Debugging Code in Visual Studio Code

1. **Set Up a Python Environment:** 
   - Ensure you have Python and the Python extension for VSCode installed.

2. **Open Your Python File:** 
   - Open the Python file you want to debug.

3. **Set Breakpoints:** 
   - Click on the left margin (or use `F9`) on the line where you want the debugger to pause execution. 
   - Breakpoints are spots in the code where you suspect a bug might be present.

4. **Configure the Debugger:** 
   - Click on the "Run and Debug" icon on the sidebar or use the `Ctrl+Shift+D` shortcut. 
   - If you haven't already configured the debugger, VSCode will prompt you to select the environment.

5. **Start Debugging:** 
   - Click the green play button in the debug panel or press `F5` to start the debugging session. 
   - The debugger will run the program and pause at the first breakpoint.

6. **Inspect Variables and Step Through the Code:** 
   - When the debugger pauses, you can hover over variables to inspect their values, use the debug console, or use the step over (`F10`), step into (`F11`), and continue (`F5`) commands to control the execution flow.

7. **Watch Expressions and Call Stack:** 
   - You can add expressions to watch their values and see the call stack to understand the sequence of function calls.

Go back to [Contents](#contents).



#### Debugging Code in PyCharm

1. **Set Up Your Project:** 
   - Open your project in PyCharm and ensure the correct interpreter is selected.

2. **Set Breakpoints:** 
   - Like in VSCode, you can set breakpoints by clicking on the left margin next to the line numbers.

3. **Start a Debug Session:** 
   - Click on the bug icon or press `Shift+F9` to start debugging. 
   - PyCharm will run your code and pause at the first breakpoint.

4. **Use the Debug Tool Window:** 
   - PyCharm provides a debug tool window with several tabs for variables, watches, frames, and more. 
   - You can use these to inspect and modify the state of your program.

5. **Step Through the Code:** 
   - Utilize the step over, step into, step out, and run to cursor features to control the execution flow and analyze your code's behavior at each step.

6. **Evaluate Expressions:** 
   - PyCharm allows you to evaluate expressions on-the-fly to see what certain parts of your code are returning.

7. **Analyze the Stack Trace:** 
   - Use the stack trace to see the order of function calls that led to each breakpoint.

Go back to [Contents](#contents).



#### Python Debugger tool - pdb

The [Python Debugger](https://docs.python.org/3/library/pdb.html), often abbreviated as `pdb`, is a built-in debugging tool in Python that allows developers to interactively debug their code. 

It provides a convenient way to pause execution, inspect variables, and step through code line by line to identify and fix errors.

Key features of pdb include:
- **Breakpoints:** Developers can insert breakpoints into their code to pause execution at specific lines or functions.
- **Interactive Debugging:** Once execution is paused, developers can interactively explore the state of their program, inspect variables, and evaluate expressions.
- **Step-by-Step Execution:** `pdb` allows developers to execute code line by line, stepping into functions or skipping over them as needed.
- **Stack Traces:** Developers can examine the call stack to understand the sequence of function calls that led to the current point of execution.
- **Variable Inspection:** `pdb` provides commands to inspect the values of variables and expressions at runtime, helping developers diagnose issues in their code.
- **Conditional Breakpoints:** Developers can set breakpoints with conditions, allowing them to pause execution only when certain conditions are met.

Popular integrated development environments (IDEs) for Python, such as VSCode and PyCharm, leverage the Python Debugger (`pdb`) for debugging code. They provide user-friendly interfaces and additional features to enhance the debugging experience.

Here's how you can debug your Python code using the `pdb` (Python Debugger) tool.

1. **Insert Debugger Statement:** 
    - In your Python script, insert the following line at the point where you want to start debugging:

```python
import pdb; pdb.set_trace()
```

This line tells Python to pause execution and enter the debugger mode when it encounters this statement during runtime.

2. **Run Your Script:** 
   - Execute your Python script as you normally would.

3. **Enter Debugger Mode:** 
   - When Python encounters the `pdb.set_trace()` statement, it will pause execution and enter the debugger mode. 
   - You'll see a debugger prompt that looks like this:

```shell
(Pdb)
```

4. **Debug Your Code:** 
    - Once in debugger mode, you can interactively debug your code using various commands. 

Here are some commonly used commands:

- `h` or `help`: Display a list of available debugger commands and their descriptions.
- `n` or `next`: Execute the current line of code and move to the next line.
- `s` or `step`: Step into the function call on the current line.
- `c` or `continue`: Continue execution until the next breakpoint or the end of the script.
- `l` or `list`: Show the current line of code and a few lines of surrounding context.
- `p` or `print`: Print the value of a variable or expression.
- `q` or `quit`: Quit the debugger and terminate the script.

5. **Inspect Variables:** 
   - While in debugger mode, you can inspect the values of variables, evaluate expressions, and interact with your code as needed. For example, you can type the name of a variable and press Enter to see its current value.

6. **Continue Execution:** 
   - Use the continue command to resume normal execution of your script. The debugger will remain active until either the script completes or you explicitly quit the debugger using the quit command.

Here's an example of how you might use pdb to debug a Python script:

```python
import pdb

def add(a, b):
    pdb.set_trace()  # Insert debugger statement
    result = a + b
    return result

x = 5
y = 10
z = add(x, y)
print("Result:", z)
```

Go back to [Contents](#contents).



## Python Basics

Go back to [Contents](#contents).

### Keywords

Python keywords are reserved words that cannot be used as identifiers (variable names, function names, class names, etc.) because they are part of the syntax of the language and are used to define its structure and operations.

Here's a Python code that attempts to incorporate as many Python keywords as possible in a meaningful way. This script includes concepts such as function definition, class definition, control flow, exception handling, and more.

```python
# This Python code aims to use as many Python keywords as possible in a meaningful context.

# Define a class
class Example:
    def __init__(self, value):
        self.value = value

    # Use of the 'property' decorator to create a getter
    @property
    def value(self):
        return self._value

    # Use of the 'property' setter to set a value
    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError("Value must be non-negative")
        self._value = val

# Function definition using def
def my_func():
    # try-except-else-finally for exception handling
    try:
        example = Example(10)
        
        # if-elif-else for conditional statements
        if example.value > 0:
            print("Positive value")
        elif example.value == 0:
            print("Zero")
        else:
            print("Negative value")  # This won't actually print due to the ValueError in the setter
        
        # for loop and the 'in' keyword
        for i in range(3):
            print(i)
        
        # while loop with 'break' and 'continue'
        count = 0
        while True:
            if count > 2:
                break
            elif count == 1:
                count += 1
                continue
            print(f"Count: {count}")
            count += 1
        
        # Use of 'assert' for a simple assertion
        assert example.value == 10, "example.value should be 10"
        
    except ValueError as e:
        print(e)
    else:
        # 'pass' is used here as a placeholder for future code
        pass
    finally:
        print("Cleanup can go here")

# Global scope
if __name__ == "__main__":
    # 'del' keyword usage for deleting an object reference
    obj = Example(5)
    del obj
    
    # Use of 'global' keyword
    global_var = 10
    
    def modify_global():
        global global_var
        global_var += 1
    
    modify_global()
    
    # Use of 'nonlocal' within nested function
    def outer():
        x = "local"
        def inner():
            nonlocal x
            x = "nonlocal"
            print(x)
        inner()
    outer()
    
    # Use of 'with' statement for context management
    with open("test.txt", "w") as f:
        f.write("Hello, world!")
    
    # Use of 'import' and 'from' keywords
    import math
    from sys import version
    
    # Use of 'as' for aliasing
    import datetime as dt
    
    # Use of 'lambda' for anonymous function
    square = lambda x: x ** 2
    
    # Use of 'return' in the context of the lambda
    print(square(5))
    
    from collections.abc import Generator

    # Use of 'yield' in a generator
    def simple_gen():
        for i in range(3):
            print(i)
            yield i
    
    if isinstance(simple_gen(), Generator):
        print("It's a generator!")
    
    # Calling the my_func function
    my_func()
```

The Python code provided uses a variety of keywords, each serving a specific purpose within the language. 

Here's a list of the keywords used and a brief description of their role in the code:

- `class`: Used to define a new class.
- `def`: Used for function and method definition.
- `try`: Begins a block of code that will be attempted, which may lead to an exception.
- `except`: Specifies an exception handler or types of exceptions to catch after a try block.
- `else`: Defines a block of code to be executed if no exceptions were raised in the try block.
- `finally`: Defines a block of code to be executed at the end of a try block, regardless of whether an exception was raised or not.
- `if`: Used for conditional execution.
- `elif`: Used for additional conditions in an if...else block.
- `for`: Begins a for loop.
- `in`: Used to check if a value is present in a sequence or to iterate over a sequence in a for loop.
- `while`: Begins a while loop.
- `break`: Exits the closest enclosing loop.
- `continue`: Skips the rest of the code inside the loop for the current iteration and goes to the next iteration of the loop.
- `assert`: Used for debugging purposes to check if a condition is true.
- `pass`: A null statement, a placeholder for future code.
- `del`: Deletes an object.
- `global`: Declares a variable as global.
- `nonlocal`: Declares a variable as not local, used to work with variables inside nested functions.
- `with`: Used to wrap the execution of a block of code within methods defined by the context manager.
- `import`: Imports a module.
- `from`: Used to import specific attributes or functions from a module.
- `as`: Used to create an alias while importing a module.
- `lambda`: Creates an anonymous function.
- `return`: Exits a function and returns a value.
- `yield`: Used by a generator function to return a value and pause its execution.
- `is`: Tests for object identity.

Go back to [Contents](#contents).

### Identifiers

Identifiers are names given to variables, functions, classes, etc.

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

### Python type annotations

Python type annotations are a way to explicitly indicate the types of variables, function parameters, return values, and more. Introduced in Python 3.5 through PEP 484, type annotations offer a way to use Python as a statically-typed language, though they do not enforce type checking at runtime. Instead, they can be used by third-party tools, IDEs, and linters to perform static type checking, improve code readability, and catch certain types of errors before runtime.

Go back to [Contents](#contents).

#### Python type annotations - Basic syntax

The basic syntax for type annotations in Python involves adding a colon (:) followed by the type after variable names or function parameters, and for function return types, an arrow (->) followed by the type just before the colon that ends the function definition.

Go back to [Contents](#contents).

#### Python type annotations examples

1. **Variable Annotations:**

```python
age: int = 25
name: str = "Alice"
is_student: bool = True
```

Go back to [Contents](#contents).

2. **Function Annotations:**

Annotations for function arguments and the return type:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Go back to [Contents](#contents).

3. **List, Set, Dict, and Other Collections:**

With the `typing` module, you can specify types for collections:

```python
from typing import List, Set, Dict

names: List[str] = ["Alice", "Bob", "Charlie"]
unique_ids: Set[int] = {1, 2, 3}
student_scores: Dict[str, int] = {"Alice": 85, "Bob": 90}
```

Go back to [Contents](#contents).

4. **Optional Types:**

Use `Optional` when a variable could be `None`:

```python
from typing import Optional

def find_student(name: str) -> Optional[Dict]:
    # Imagine a function that returns a student record as a dictionary if found,
    # or None if not found.
    pass
```

Go back to [Contents](#contents).

5. **Type Aliases:**

You can create aliases for types to make complex annotations easier to read:

```python
from typing import Dict, List

Student = Dict[str, str]
Classroom = List[Student]

def list_students(classroom: Classroom) -> None:
    for student in classroom:
        print(student['name'])
```

Go back to [Contents](#contents).

6. **Type Checking:**

To actually enforce these types, you would need to use a static type checker like [mypy](https://mypy-lang.org/). 

Running a type checker is a separate step from running your Python code:

```shell
mypy script.py
```

This checks `script.py` for type consistency according to its annotations.

Type annotations are entirely optional and are not enforced at runtime, but they are highly useful for larger projects, enabling better code completion, error detection, and documentation.

Go back to [Contents](#contents).

### Operators

In Python, operators are special symbols that are used to perform operations on variables and values. 

Here's an explanation of each type of operator:

Go back to [Contents](#contents).

#### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

- `+` (Addition): Adds two operands
- `-` (Subtraction): Subtracts the second operand from the first
- `*` (Multiplication): Multiplies two operands
- `/` (Division): Divides the first operand by the second
- `%` (Modulus): Returns the remainder when the first operand is divided by the second
- `**` (Exponentiation): Raises the first operand to the power of the second
- `//` (Floor Division): Divides the first operand by the second and rounds down to the nearest whole number

Go back to [Contents](#contents).

#### Assignment Operators

Assignment operators are used to assign values to variables.

- `=`: Assigns a value to a variable
- `+=`: Adds the right operand to the left operand and assigns the result to the left operand
- `-=`: Subtracts the right operand from the left operand and assigns the result to the left operand
- `*=`: Multiplies the left operand by the right operand and assigns the result to the left operand
- `/=`: Divides the left operand by the right operand and assigns the result to the left operand
- `%=`: Takes modulus using two operands and assigns the result to the left operand
- `**=`: Performs exponential (power) calculation on operators and assigns the value to the left operand
- `//=`: Performs floor division on operators and assigns the value to the left operand

Go back to [Contents](#contents).

#### Comparison Operators

Comparison operators are used to compare two values.

- `==`: Equal to - True if both operands are equal
- `!=`: Not equal to - True if operands are not equal
- `>`: Greater than - True if the left operand is greater than the right
- `<`: Less than - True if the left operand is less than the right
- `>=`: Greater than or equal to - True if the left operand is greater than or equal to the right
- `<=`: Less than or equal to - True if the left operand is less than or equal to the right

Go back to [Contents](#contents).

#### Logical Operators

Logical operators are used to combine conditional statements.

- `and`: Returns True if both statements are true
- `or`: Returns True if one of the statements is true
- `not`: Reverse the result, returns False if the result is true

Go back to [Contents](#contents).

#### Identity Operators

Identity operators are used to compare the memory locations of two objects.

- `is`: True if both operands refer to the same object
- `is not`: True if operands refer to different objects

Go back to [Contents](#contents).

#### Membership Operators

Membership operators are used to test whether a sequence is presented in an object.

- `in`: `True` if the sequence with the specified value is present in the object
- `not in`: `True` if the sequence with the specified value is not present in the object

Go back to [Contents](#contents).

#### Bitwise Operators

Bitwise operators are used to perform bitwise calculations on integers.

- `&`: AND - Sets each bit to 1 if both bits are 1
- `|`: OR - Sets each bit to 1 if one of two bits is 1
- `^`: XOR - Sets each bit to 1 if only one of two bits is 1
- `~`: NOT - Inverts all the bits
- `<<`: Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off
- `>>`: Signed right shift - Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

Go back to [Contents](#contents).

#### Examples for each type of operator in Python

Each type of operator serves a different purpose and is used in different contexts depending on what you are trying to achieve in your Python code.

Arithmetic Operators:

- `+` (Addition): `3 + 2` will give `5`
- `-` (Subtraction): `3 - 2` will give `1`
- `*` (Multiplication): `3 * 2` will give `6`
- `/` (Division): `3 / 2` will give `1.5`
- `%` (Modulus): `3 % 2` will give `1` (remainder of the division)
- `**` (Exponentiation): `3 ** 2` will give `9` (3 squared)
- `//` (Floor Division): `3 // 2` will give `1` (division without remainder)

Go back to [Contents](#contents).

Assignment Operators:

- `=`: `x = 5` will assign the value `5` to `x`
- `+=`: `x += 3` is equivalent to `x = x + 3`
- `-=`: `x -= 3` is equivalent to `x = x - 3`
- `*=`: `x *= 3` is equivalent to `x = x * 3`
- `/=`: `x /= 3` is equivalent to `x = x / 3`
- `%=`: `x %= 3` is equivalent to `x = x % 3`
- `**=`: `x **= 3` is equivalent to `x = x ** 3`
- `//=`: `x //= 3` is equivalent to `x = x // 3`

Go back to [Contents](#contents).

Comparison Operators:

- `==`: `5 == 5` will return `True`
- `!=`: `5 != 3` will return `True`
- `>`: `5 > 3` will return `True`
- `<`: `5 < 3` will return `False`
- `>=`: `5 >= 5` will return `True`
- `<=`: `5 <= 5` will return `True`

Go back to [Contents](#contents).

Logical Operators:

- `and`: `(5 > 3) and (5 > 4)` will return `True`
- `or`: `(5 > 3) or (5 < 4)` will return `True`
- `not`: `not(5 > 3)` will return `False`

Go back to [Contents](#contents).

Identity Operators:

- `is`: `a = [1,2,3]`; `b = [1,2,3]`; `a is b` will return `False` (different objects in memory)
- `is not`: `a is not b` will return `True`

Go back to [Contents](#contents).

Membership Operators:

- `in`: `'a' in 'cat'` will return `True`
- `not in`: `'b' not in 'cat'` will return `True`

Go back to [Contents](#contents).

Bitwise Operators:

- `&`: `5 & 3` will return `1` (binary `0101 & 0011` is `0001`)
- `|`: `5 | 3` will return `7` (binary `0101 | 0011` is `0111`)
- `^`: `5 ^ 3` will return `6` (binary `0101 ^ 0011` is `0110`)
- `~`: `~5` will return `-6` (inverts the bits of `0101`, resulting in `1010` in two's complement which is `-6`)
- `<<`: `5 << 1` will return `10` (shifts the bits of `0101` left by `1`, resulting in `1010`)
- `>>`: `5 >> 1` will return `2` (shifts the bits of `0101` right by `1`, resulting in `0010`)

Go back to [Contents](#contents).

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

#### The print function

The `print()` function in Python is quite versatile and can be used in various ways to format and display output. 

Below are several examples showcasing different uses and features of the `print()` function:

Go back to [Contents](#contents).

1. Printing Simple Messages

The most straightforward use is to print a simple message or variable:

```python
print("Hello, Python!")
```

Go back to [Contents](#contents).

2. Printing Multiple Arguments

You can print multiple items separated by commas. Python will automatically insert spaces between items:

```python
x = 5
print("The value of x is", x, "and its double is", x * 2)
```

Go back to [Contents](#contents).

3. Using String Concatenation

You can concatenate strings using the `+` operator before printing:

```python
name = "Alice"
print("Hello, " + name + "!")
```

Go back to [Contents](#contents).

4. Using String Formatting

a. f-strings (Python 3.6+)

```python
name = "Alice"
age = 30
print(f"{name} is {age} years old.")
```

b. str.format()

```python
name = "Alice"
age = 30
print("{} is {} years old.".format(name, age))
```

c. % formatting (older method)

```python
name = "Alice"
age = 30
print("%s is %d years old." % (name, age))
```

Go back to [Contents](#contents).

5. Printing Without a Newline

By default, `print()` adds a newline character (`\n`) after each call, but you can change this behavior using the end parameter:

```python
print("Hello, ", end="")
print("world!")
```

This prints Hello, world! on the same line.

Go back to [Contents](#contents).

6. Printing With a Custom Separator

The `sep` parameter changes the separator between items from a space to a string of your choice:

```python
print("2024", "02", "14", sep="-")
```

Go back to [Contents](#contents).

7. Printing To a File

Instead of printing to the standard output, you can redirect the output to a file using the file parameter:

```python
with open("output.txt", "w") as file:
    print("Hello, file!", file=file)
```

This writes Hello, file! into output.txt.

Go back to [Contents](#contents).

8. Printing in a Loop

`print()` can be used inside loops to display sequences or to format output in a structured manner:

```python
for i in range(3):
    print(i, end=" ")  # Prints: 0 1 2
```

Go back to [Contents](#contents).

9. Flushing the Output Buffer

The flush parameter forces Python to "flush" the output buffer, ensuring that output is immediately visible:

```python
import time

print("Starting...", end="", flush=True)
time.sleep(2)  # Wait for 2 seconds.
print("done.")
```
Go back to [Contents](#contents).

These examples demonstrate the flexibility of the `print()` function for displaying output in Python scripts, allowing you to easily format and control how information is presented to users.

Go back to [Contents](#contents).

#### The input function

The `input()` function in Python is used to capture user input from the standard input, typically the keyboard. 

Here are various ways to use the `input()` function to read different types of data, handle user inputs more effectively, and make your programs interactive:

Go back to [Contents](#contents).

1. Basic String Input

The simplest use case is to prompt the user for some text input:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

Go back to [Contents](#contents).

2. Converting Input Types

By default, input() returns a string. To work with different data types, you need to convert the input accordingly:

Integer Input:

```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

Floating Point Input:

```python
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters.")
```

Go back to [Contents](#contents).

3. Multiline Input

For reading multiline input from the user, you can loop until a specific condition is met, for example, an empty string:

```python
print("Enter your address (leave a blank line to finish):")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
address = "\n".join(lines)
print("Your address is:")
print(address)
```

Go back to [Contents](#contents).

4. Password Input (Hiding the Input)

For sensitive information like passwords, you might not want the input to be visible. Use the `getpass` module instead of `input()`:

```python
import getpass

password = getpass.getpass("Enter your password: ")
print("Password entered! (but not shown)")
```

Note: `getpass` might not work as expected in some IDEs or Jupyter notebooks.

Go back to [Contents](#contents).

5. Command-line Arguments (Alternative to `input()`)

For scripting or when you want to process input parameters at the start, you can use command-line arguments instead of interactive input:

```python
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("No name provided.")
```

Run this script from the command line with an argument to see the effect.

Go back to [Contents](#contents).

6. Reading a List of Items

You can ask the user to input a list of items separated by a specific delimiter, and then use string methods to handle the input:

```python
items_input = input("Enter items separated by commas: ")
items = items_input.split(',')
print("You entered:", items)
```

Go back to [Contents](#contents).

7. Using eval() for Dynamic Type Input

Use eval() carefully to automatically determine the type of user input. This can be useful but poses a security risk if the input is not controlled:

```python
expression = eval(input("Enter an expression: "))
print("Result:", expression)
```

Be cautious with `eval()` as it can execute arbitrary code. It's typically best to avoid it unless you're sure of the input's safety.

Go back to [Contents](#contents).

These examples demonstrate the versatility of the `input()` function in Python for interacting with users and processing their input in various formats. Always validate and sanitize user input to ensure your program behaves as expected and securely.

Go back to [Contents](#contents).



### The Python main function

In Python, the concept of a "main" function is not required in the same way it is in some other programming languages like C or Java. 

However, it is a common practice to use a main function as the entry point for a program. This is done for code organization, readability, and maintainability. 

The main function in Python is typically defined by the user, and it encapsulates the primary functionality of the script.

Here's how you can define and use a main function in Python:

1. **Define the main function:** You simply define a function named `main()` that contains the code you wish to execute.
2. **Call the main function:** To ensure that your `main()` function runs only when your script is executed directly (and not when imported as a module in another script), you use the `if __name__ == "__main__":` idiom at the bottom of your script to call the main() function.

Example:

```python
def main():
    # Your main code here
    print("Hello, world!")

if __name__ == "__main__":
    main()
```

Go back to [Contents](#contents).


#### When to Use It

- **Organization:**
  - When your script starts to get complex, having a main function helps keep your code organized and readable. It serves as the entry point and makes it clear where execution begins.
- **Reusability:** 
  - If your script is also intended to be imported as a module in other scripts, using a main function prevents the script's code from running immediately upon import. Only the code within the main function runs when the script is executed directly.
- **Testing:** 
  - Separating your code into functions, including a main function, makes it easier to test individual parts of your code.

Go back to [Contents](#contents).


#### Do You Need to Use It

While it's not a strict requirement in Python to define and use a main function, it is considered good practice, especially for larger or more complex scripts. 
- It helps with code organization and ensures that your script can be both run directly and safely imported by other scripts without unintended side effects.

In summary, you should use a main function when your script grows in complexity and you need to maintain clarity and reusability. 
- For very simple or short scripts, it might be overkill and not strictly necessary.

Go back to [Contents](#contents).



## Conditional Statements

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



## Loops

Python provides two types of loops - `for` and `while`. 

A `for` loop is used for iterating over a sequence like a list, tuple, string, or range. 

Meanwhile, a `while` loop repeats as long as a certain boolean condition is met.

Go back to [Contents](#contents).

#### The for loop

Use a `for` loop when:

- **You know the exact number of iterations in advance**
  - This is the most common scenario for using for loops, such as iterating over a sequence (like a list, tuple, dictionary, set, or string) or when you have a fixed number of iterations.
- **You are iterating over a collection of items**
  - `for` loops are inherently designed to iterate over items of a collection directly, making the code more readable and concise.
- **You are using generators or iterators**
  - When dealing with generators or iterators, including those returned by built-in functions like `range()`, `enumerate()`, or `zip()`, `for` loops are the way to go.

Here are Python code examples for each of the scenarios where a `for` loop is commonly used:

1. Iterating over a sequence with a known number of iterations

```python
# Iterating over a range of numbers
for i in range(5):  # Known number of iterations
    print(i)
```

2. Iterating over a collection of items

```python
# Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Iterating over a dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
    print(f"{key}: {value}")
```

3. Using generators or iterators

```python
# Using a generator expression
squares = (x*x for x in range(5))
for square in squares:
    print(square)

# Using the enumerate function to get index-value pairs
names = ['Alice', 'Bob', 'Charlie']
for index, name in enumerate(names):
    print(index, name)

# Using the zip function to iterate over two lists in parallel
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 30, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

Each of these examples demonstrates the versatility and readability of for loops in scenarios where you have a clear iteration pattern, whether it's over a sequence, a collection of items, or through the use of iterators and generators.

Go back to [Contents](#contents).

#### The while loop

Use a `while` loop when:

- **The number of iterations is not known in advance**
  - If you're looping until a certain condition changes and you cannot determine in advance how many iterations it will take, a while loop is appropriate.

- **You want to maintain state between iterations**
  - While you can maintain state between iterations in a for loop as well, a while loop might be more intuitive if the state significantly affects the continuation of the loop.

- **The loop condition is based on something other than iterating over a sequence**
  - When your loop continues until a specific condition changes (regardless of how many iterations it takes), a while loop can directly express this logic.

Here are Python code examples for each of the scenarios where a `while` loop is commonly used:

1. The number of iterations is not known in advance

```python
# A loop that continues until a user inputs a specific word

input_word = ""

while input_word.lower() != "stop":
    input_word = input("Enter a word (type 'stop' to exit): ")
    print(f"You entered: {input_word}")
```

2. Maintaining state between iterations

```python
# A guessing game where the user has to guess a number

import random

target_number = random.randint(1, 100)  # Random number between 1 and 100
guess = None
tries = 0

while guess != target_number:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")

print(f"Congratulations! You guessed the number in {tries} tries.")
```

3. Loop condition based on something other than iterating over a sequence

```python
# A loop that runs until a certain condition is met, e.g., achieving a balance goal

balance = 1000  # Starting balance
goal = 1500  # Target balance
interest_rate = 0.05  # Interest rate per period
periods = 0

while balance < goal:
    balance += balance * interest_rate  # Apply interest
    periods += 1

print(f"Your balance reached {balance:.2f} after {periods} periods.")
```

Go back to [Contents](#contents).

Each of these examples demonstrates the use of `while` loops in situations where the number of iterations is not predetermined, where maintaining and updating state is crucial, and where the loop's continuation is based on dynamic conditions rather than a pre-defined sequence or collection.

#### Loop statements - break  - continue - pass

Furthermore, loops can be controlled with 'break', 'continue', and 'pass' statements. 

* 'break' exits the loop
* 'continue' skips to the next iteration
* 'pass' does nothing and is generally used as a placeholder

For example:

1. `break` - exits the loop

```python
# Example: Find the first number divisible by 5 in a list

numbers = [2, 3, 7, 11, 15, 18, 20, 22]

for number in numbers:
    if number % 5 == 0:
        print(f"The first number divisible by 5 is {number}.")
        break  # Exit the loop
```

2. `continue` - skips to the next iteration

```python
# Example: Print only odd numbers from a list, skipping even numbers

numbers = range(1, 10)  # Numbers from 1 to 9

for number in numbers:
    if number % 2 == 0:
        continue  # Skip this iteration and proceed with the next one
    print(number)  # This will print only odd numbers
```

3. `pass` - does nothing

```python
# Example: Iterate over numbers but only print a message for a specific condition, do nothing otherwise

numbers = range(1, 5)  # Numbers from 1 to 4
for number in numbers:
    if number == 3:
        print("Number is three")
    else:
        pass  # Do nothing, but the loop continues
```

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

* **Lists** 
  * Lists are mutable sequences of elements.
* **Tuples**
  * Tuples are immutable sequences, similar to lists, but their contents cannot be changed.
* **Dictionaries**
  * Dictionaries contain key-value pairs.
* **Sets** 
  * Sets are unordered collections of unique elements.

Go back to [Contents](#contents).



### The length function for data structures

In Python, you can find the length of lists, tuples, dictionaries using the built-in `len()` function.


- **List Length:**

```python
my_list = [10, 20, 30, 40, 50]
print(len(my_list))  # Output: 5
```

Go back to [Contents](#contents).


- **Tuple Length:**

```python
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # Output: 5
```

Go back to [Contents](#contents).


- **Dictionary Length:**

Note: For Dictionary, the `len()` function returns the number of pairs (i.e., keys).

```python
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(len(my_dict))  # Output: 4
```

Go back to [Contents](#contents).


- **Set Length:**

```python
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5
```

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



### Python Collections Module

The Python collections module is an integral part of Python that offers specialized container datatypes. These containers are not just about holding objects, but they are about improving your data manipulation capabilities, and making your code more efficient, and readable.

There are various types of collections in Python, including `namedtuple`, `deque`, `ChainMap`, `Counter`, `OrderedDict`, `defaultdict`, `UserDict`, `UserList`, and `UserString`. Each of these plays a crucial role in handling data in more sophisticated ways than the basic built-ins like lists, dictionaries, and tuples.

Go back to [Contents](#contents).



#### namedtuple

The `namedtuple` is a factory function for creating subclass of tuples with named fields. 
- These named fields make code more readable and self-documenting. 
- They can be accessed through named attributes as well as being indexable and iterable like regular tuples.

For example:

```python
from collections import namedtuple

# Creating a namedtuple for a point in 2D space
Point = namedtuple('Point', ['x', 'y'])
pt = Point(11, 22)

print(pt.x, pt.y)  # Accessing by name
print(pt[0], pt[1])  # Accessing by index
```

Go back to [Contents](#contents).



##### More 10 namedtuple examples

Here are 10 examples demonstrating various use cases and features of `namedtuple`.

Go back to [Contents](#contents).


**Example 1:** Basic Usage

Defining a simple `Point` namedtuple for representing coordinates in a 2D space.

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(p1.x, p1.y)  # Output: 10 20
```

Go back to [Contents](#contents).


**Example 2:** Accessing Values

Accessing values using field names and also by index.

```python
from collections import namedtuple

Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])
circle = Circle(0, 0, 5)

print(circle.center_x)  # Access by name
print(circle[1])  # Access by index, output: 0
```

Go back to [Contents](#contents).


**Example 3:** Default Values

Using` _make()` to create a new instance from an iterable, and `_asdict()` to convert a namedtuple instance into an `OrderedDict`.

```python
from collections import namedtuple

Employee = namedtuple('Employee', 'name position salary')
emp = Employee._make(['John Doe', 'Manager', 50000])

print(emp._asdict())  # Output: OrderedDict([('name', 'John Doe'), ('position', 'Manager'), ('salary', 50000)])
```

Go back to [Contents](#contents).


**Example 4:** Unpacking

Unpacking a namedtuple into variables.

```python
from collections import namedtuple

Color = namedtuple('Color', 'red green blue')
color = Color(55, 155, 255)

r, g, b = color
print("R:", r, "G:", g, "B:", b) # Output: R: 55 G: 155 B: 255
```

Go back to [Contents](#contents).


**Example 5:** Subclassing

Extending a namedtuple by subclassing.

```python
from collections import namedtuple

Person = namedtuple('Person', 'name age')

class Employee(Person):
    def __str__(self):
        return f'{self.name}, {self.age} years old'

emp = Employee('Jane Doe', 30)
print(emp)  # Output: Jane Doe, 30 years old
```

Go back to [Contents](#contents).


**Example 6:** Field Names from a Single String

Using a single space/comma-delimited string for field names.

```python
from collections import namedtuple

Book = namedtuple('Book', 'title, author, year')
book = Book('1984', 'George Orwell', 1949)

print(book.title)  # Output: 1984
```

Go back to [Contents](#contents).


**Example 7:** Using Replace to Create Modified Instances

Modifying an instance by using the `_replace()` method.

```python
from collections import namedtuple

Stock = namedtuple('Stock', 'symbol current high low')
apple_stock = Stock('AAPL', 150, high=180, low=120)

# Updating the current price
apple_stock = apple_stock._replace(current=155)
print(apple_stock) # Output: Stock(symbol='AAPL', current=155, high=180, low=120)
```

Go back to [Contents](#contents).


**Example 8:** Optional/Default Values

Specifying default values for some fields using the defaults argument.

```python
from collections import namedtuple

Account = namedtuple('Account', 'owner balance type', defaults=[0, 'savings'])
acc = Account('John')
print(acc)  # Output: Account(owner='John', balance=0, type='savings')
```

Go back to [Contents](#contents).


**Example 9:** Namedtuple as a Dictionary Key

Using namedtuples as keys in dictionaries, benefiting from their hashability.

```python
from collections import namedtuple

Location = namedtuple('Location', 'latitude longitude')
visits = {Location(34.0522, -118.2437): 'Los Angeles',
          Location(40.7128, -74.0060): 'New York'}

print(visits[Location(34.0522, -118.2437)])  # Output: Los Angeles
```

Go back to [Contents](#contents).


**Example 10:** Converting a Dictionary to a Namedtuple

Converting a dictionary to a namedtuple using the double-star operator.

```python
from collections import namedtuple

Person = namedtuple('Person', 'name age')
person_info = {'name': 'Alice', 'age': 30}

alice = Person(**person_info)
print(alice)  # Output: Person(name='Alice', age=30)
```

Go back to [Contents](#contents).


#### deque

The `deque` stands for "double-ended queue". 
- It supports thread-safe, memory-efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
- O(1) denotes constant time complexity. This term is used to describe an algorithm or operation whose execution time does not change with the size of the input data set.

For example:

```python
from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.append(6)  # Add to the right
dq.appendleft(0)  # Add to the left
print(dq) # Output: deque([0, 1, 2, 3, 4, 5, 6])

dq.pop()  # Remove from the right
dq.popleft()  # Remove from the left
print(dq) # Output: deque([1, 2, 3, 4, 5])
```

Go back to [Contents](#contents).



##### More 10 deque examples](#more-10-deque-examples)

Here are 10 examples demonstrating various use cases and features of `deque`.

Go back to [Contents](#contents).


**Example 1:** Basic Usage

Creating a `deque` and appending items to the right (the default behavior).

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)  # Add to the right
print(dq)  # Output: deque([1, 2, 3, 4])
```

Go back to [Contents](#contents).


**Example 2:** Appending to the Left

Appending items to the left side.

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)  # Add to the right
dq.appendleft(0)  # Add to the left
print(dq)  # Output: deque([0, 1, 2, 3, 4])
```

Go back to [Contents](#contents).


**Example 3:** Popping Items

Popping items from both ends.

```python
from collections import deque

dq = deque([0, 1, 2, 3, 4])
dq.pop()  # Remove from the right
dq.popleft()  # Remove from the left
print(dq)  # Output: deque([1, 2, 3])
```

Go back to [Contents](#contents).


**Example 4:** Extending the Deque

Extending the deque with multiple elements at once.

```python
from collections import deque

dq = deque([1, 2, 3, 4])
dq.extend([4, 5, 6])
dq.extendleft([0, -1, -2])  # Note: the iterable is added in reverse order
print(dq)  # Output: deque([-2, -1, 0, 1, 2, 3, 4, 5, 6])
```

Go back to [Contents](#contents).


**Example 5:** Rotating the Deque

Rotating the deque n steps to the right (n > 0) or left (n < 0).

```python
from collections import deque

dq = deque([-2, -1, 0, 1, 2, 3, 4, 5, 6])
dq.rotate(3)  # Rotate right by 3
print(dq)  # Output: deque([4, 5, 6, -2, -1, 0, 1, 2, 3])
dq.rotate(-2)  # Rotate left by 2
print(dq)  # Output: deque([6, -2, -1, 0, 1, 2, 3, 4, 5])
```

Go back to [Contents](#contents).


**Example 6:** Clearing the Deque

Removing all elements from the deque.

```python
from collections import deque

dq = deque([-2, -1, 0, 1, 2, 3, 4, 5, 6])

dq.clear()
print(dq)  # Output: deque([])
```

Go back to [Contents](#contents).


**Example 7:** Working with Fixed-Size Deques

Creating a fixed-size deque to limit the number of items and automatically discard oldest items when new ones are added.

```python
from collections import deque

fixed_dq = deque(maxlen=3)
for i in range(5):
    fixed_dq.append(i)
    print(fixed_dq)  # Observe how older items are discarded
```

Go back to [Contents](#contents).


**Example 8:** Counting Elements

Counting the occurrences of an element.

```python
from collections import deque

dq = deque([1, 2, 3, 4, 2, 2, 3])
print(dq.count(2))  # Output: 3
```

Go back to [Contents](#contents).


**Example 9:** Inserting Elements

Inserting an element at a specific position.

```python
from collections import deque

dq = deque([1, 2, 4, 5])
dq.insert(2, 3)  # Insert 3 at index 2
print(dq)  # Output: deque([1, 2, 3, 4, 5])
```

Go back to [Contents](#contents).


**Example 10:** Reversing the Deque

Reversing the elements in the deque in-place.

```python
from collections import deque

dq = deque([1, 2, 3, 4, 5])
dq.reverse()
print(dq)  # Output: deque([5, 4, 3, 2, 1])
```

Go back to [Contents](#contents).


#### ChainMap

The `ChainMap` is used to combine multiple dictionaries or mappings into a single view. 
- If you update the `ChainMap`, only the first mapping gets updated. 
- It is especially useful in scenarios where you want to avoid physically merging dictionaries together.

For example:

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)

print(chain['a'])  # Output from dict1 -> Output: 1
print(chain['b'])  # Output from dict1, because it's the first dictionary -> Output: 2
```

Go back to [Contents](#contents).



##### More 10 ChainMap examples

Here are 10 examples demonstrating various uses and features of `ChainMap`.

Go back to [Contents](#contents).


**Example 1:** Basic Usage

Combining two dictionaries into a single `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
chain = ChainMap(dict1, dict2)
print(chain['a'])  # Output: 1 (values from the first dictionary have precedence)
```

Go back to [Contents](#contents).


**Example 2:** Accessing Keys and Values

Iterating over keys, values, and items.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
chain = ChainMap(dict1, dict2)

for key in chain.keys():
    print(key, end=' ')  # Output: a b c (unique keys from all dictionaries)

for value in chain.values():
    print(value, end=' ')  # Output: 1 2 3 (values corresponding to the keys)

for item in chain.items():
    print(item, end=' ')  # Output: ('a', 1) ('b', 2) ('c', 3)
```

Go back to [Contents](#contents).


**Example 3:** Updating Values

Updating values in the original dictionaries affects the `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
chain = ChainMap(dict1, dict2)

dict1['a'] = 5
print(chain['a'])  # Output: 5
```

Go back to [Contents](#contents).


**Example 4:** Adding a New Dictionary

Adding a new dictionary to the `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
chain = ChainMap(dict1, dict2)

dict3 = {'d': 4, 'e': 5}
chain_new = chain.new_child(dict3)  # Adds dict3 as the new first dictionary
print(chain_new)  # ChainMap({'d': 4, 'e': 5}, {'a': 5, 'b': 2}, {'c': 3, 'a': 4})
```

Go back to [Contents](#contents).


**Example 5:** Reversing the ChainMap

Creating a reversed view of the `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
dict3 = {'d': 4, 'e': 5}

# Original ChainMap with dict1, dict2, and then adding dict3
chain = ChainMap(dict1, dict2)
chain_new = chain.new_child(dict3)  # Adds dict3 as the new first dictionary

# To reverse the ChainMap, reverse the order of maps manually
reversed_chain = ChainMap(*chain_new.maps[::-1])

# Print original and reversed ChainMap for comparison
print("Original ChainMap:")
print(chain_new) # Output: ChainMap({'d': 4, 'e': 5}, {'a': 1, 'b': 2}, {'c': 3, 'a': 4})
print("\nReversed ChainMap:")
print(reversed_chain) # Output: ChainMap({'c': 3, 'a': 4}, {'a': 1, 'b': 2}, {'d': 4, 'e': 5})
```

Go back to [Contents](#contents).


**Example 6:** Finding a Key in the ChainMap

Checking if a key exists in any of the dictionaries in the `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}

chain = ChainMap(dict1, dict2)

print('c' in chain)  # Output: True
```

Go back to [Contents](#contents).


**Example 7:** Removing a Dictionary

Removing a dictionary from the `ChainMap` by creating a new one without it.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}
dict3 = {'d': 4, 'e': 5}

# Original ChainMap with dict1, dict2, and then adding dict3
chain = ChainMap(dict1, dict2)
print(chain) # Output: ChainMap({'a': 1, 'b': 2}, {'c': 3, 'a': 4})

chain_new = chain.new_child(dict3)  # Adds dict3 as the new first dictionary
print(chain_new) # Output: ChainMap({'d': 4, 'e': 5}, {'a': 1, 'b': 2}, {'c': 3, 'a': 4})

reduced_chain = chain_new.parents  # Removes the last added dict
print(reduced_chain)  # Output: ChainMap({'a': 1, 'b': 2}, {'c': 3, 'a': 4})
```

Go back to [Contents](#contents).


**Example 8:** Maps Property

Accessing the list of mappings in the `ChainMap`.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}

chain = ChainMap(dict1, dict2)

print(chain.maps)  # Output: [{'a': 1, 'b': 2}, {'c': 3, 'a': 4}]
```

Go back to [Contents](#contents).


**Example 9:** Direct Modifications

Directly modifying the `ChainMap` does not create new mappings but updates the first mapping.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}

chain = ChainMap(dict1, dict2)

chain['b'] = 3
print(dict1)  # Output: {'a': 1, 'b': 3}
```

Go back to [Contents](#contents).


**Example 10:** Creating a Single Combined Dictionary

Creating a single dictionary that combines all the dictionaries in the ChainMap.

```python
from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'a': 4}

chain = ChainMap(dict1, dict2)

combined_dict = dict(chain)
print(combined_dict)  # Output: {'c': 3, 'a': 1, 'b': 2}
```


#### Counter

The `Counter` is a subclass of dictionary that is used to count hashable objects. 
- It provides a way to count objects
- It can return elements in the order of their counts, from the most common to the least.

For example:

```python
from collections import Counter

cnt = Counter('abracadabra')
print(cnt.most_common(3))  # Three most common characters -> Output: [('a', 5), ('b', 2), ('r', 2)]
```

Go back to [Contents](#contents).



##### More 10 Counter examples

Here are 10 examples demonstrating different ways to use `Counter`.

Go back to [Contents](#contents).


**Example 1:** Basic Counting

Counting occurrences of elements in a list.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})
```

Go back to [Contents](#contents).


**Example 2:** Update Counts

Updating the count for existing items and adding new items.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})

more_colors = ['red', 'yellow', 'green', 'blue']
color_count.update(more_colors)
print(color_count)  # Updated counts -> Output: Counter({'blue': 4, 'red': 3, 'yellow': 2, 'green': 1})
```

Go back to [Contents](#contents).


**Example 3:** Most Common Elements

Finding the most common elements.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count)  # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})

more_colors = ['red', 'yellow', 'green', 'blue']
color_count.update(more_colors)
print(color_count)  # Updated counts -> Output: Counter({'blue': 4, 'red': 3, 'yellow': 2, 'green': 1})

print(color_count.most_common(2))  # Output: [('blue', 4), ('red', 3)]
```

Go back to [Contents](#contents).


**Example 4:** Subtract Counts

Subtracting counts of elements from another iterable.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count) # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})

subtract_colors = ['red', 'blue']
print("subtract_colors = ['red', 'blue']") # Output: subtract_colors = ['red', 'blue']

color_count.subtract(subtract_colors)
print(color_count)  # Subtracted counts - Output: Counter({'blue': 2, 'red': 1, 'yellow': 1})
```

Go back to [Contents](#contents).


**Example 5:** Count Characters in a String

Counting characters in a string.

```python
from collections import Counter

char_count = Counter("abracadabra")
print(char_count)  # Output: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

Go back to [Contents](#contents).


**Example 6:** Counter Arithmetic

Performing arithmetic operations with `Counter` objects.


```python
from collections import Counter

counter_a = Counter(['a', 'b', 'c', 'a', 'b'])
counter_b = Counter(['a', 'b', 'c', 'b', 'd'])

print('counter_a', counter_a)
print('counter_b', counter_b)

print('counter_a + counter_b', counter_a + counter_b)  # Combine counts
print('counter_a - counter_b', counter_a - counter_b)  # Subtract counts
print('counter_a & counter_b', counter_a & counter_b)  # Intersection: min(c1[x], c2[x])
print('counter_a | counter_b', counter_a | counter_b)  # Union: max(c1[x], c2[x])

# Output:
# counter_a Counter({'a': 2, 'b': 2, 'c': 1})
# counter_b Counter({'b': 2, 'a': 1, 'c': 1, 'd': 1})
# counter_a + counter_b Counter({'b': 4, 'a': 3, 'c': 2, 'd': 1})
# counter_a - counter_b Counter({'a': 1})
# counter_a & counter_b Counter({'b': 2, 'a': 1, 'c': 1})
# counter_a | counter_b Counter({'a': 2, 'b': 2, 'c': 1, 'd': 1})
```

Go back to [Contents](#contents).


**Example 7:** Elements Method

Getting all elements in the `Counter`.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count) # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})

# List all elements based on their counts
print(list(color_count.elements())) # Output: ['blue', 'blue', 'blue', 'red', 'red', 'yellow']
```

Go back to [Contents](#contents).


**Example 8:** Set Operations with Counters

Treating `Counter` objects like multisets for set operations.

```python
from collections import Counter

c1 = Counter('abracadabra')
c2 = Counter('alacazam')

print(c1)
print(c2)

print('c1 - c2:', c1 - c2)  # Elements in c1 but not in c2
print('c1 | c2:', c1 | c2)  # Maximum of c1 and c2 counts
print('c1 & c2:', c1 & c2)  # Minimum of c1 and c2 counts

# Output
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
# Counter({'a': 4, 'l': 1, 'c': 1, 'z': 1, 'm': 1})
# c1 - c2: Counter({'b': 2, 'r': 2, 'a': 1, 'd': 1})
# c1 | c2: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1, 'l': 1, 'z': 1, 'm': 1})
# c1 & c2: Counter({'a': 4, 'c': 1})
```

Go back to [Contents](#contents).


**Example 9:** Total Count

Getting the total count of all elements.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count) # Output: Counter({'blue': 3, 'red': 2, 'yellow': 1})

total_colors = sum(color_count.values())

# Total number of counted colors
print(total_colors) # Output: 6
```

Go back to [Contents](#contents).


**Example 10:** Resetting Counts

Resetting or clearing all counts in a `Counter`.

```python
from collections import Counter

colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)

color_count.clear()
print(color_count)  # Output: Counter()
```


#### OrderedDict

The `OrderedDict` remembers the order in which entries were added. 
- Even though regular dictionaries now maintain insertion order (Python 3.7), `OrderedDict` is still useful for its additional functionality, such as reversing the order.
- Starting from Python 3.7, the standard dictionary implementation in Python maintains insertion order as part of the language specification. 
  - This means that when you insert items into a dictionary, the order in which you insert them is preserved when iterating over the dictionary, reflecting the order of addition.
  - This change was a result of the implementation detail of CPython 3.6 becoming a language feature in Python 3.7 and onwards.
  - Prior to Python 3.6, dictionaries did not guarantee order preservation, and the order could appear random and change with every new insertion.

For example:

```python
from collections import OrderedDict

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od['d'] = 4
od.move_to_end('b', last=False)  # Move 'b' to the beginning
print(od) # Output: OrderedDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
```

Go back to [Contents](#contents).



##### More 10 OrderedDict examples

Here are 10 examples of using `OrderedDict`.

Go back to [Contents](#contents).


**Example 1:** Basic Usage

Creating an `OrderedDict` and adding items.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
print(ordered_dict)  # Output: OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

Go back to [Contents](#contents).


**Example 2:** Maintaining Insertion Order

Demonstrating that the `OrderedDict` maintains insertion order.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

for key, value in ordered_dict.items():
    print(key, value)
# Output: 
# a 1
# b 2
# c 3
```

Go back to [Contents](#contents).


**Example 3:** Reversing the Order

Reversing the order of an `OrderedDict`.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

reversed_ordered_dict = OrderedDict(reversed(ordered_dict.items()))
print(reversed_ordered_dict)  # Output: OrderedDict([('c', 3), ('b', 2), ('a', 1)])
```

Go back to [Contents](#contents).


**Example 4:** Equality Test

`OrderedDict` compares both the order and the contents for equality.

```python
from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
print(od1 == od2)  # Output: False, because the order of items is different
```

Go back to [Contents](#contents).


**Example 5:** Updating Values

Updating the value of an existing key.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

ordered_dict['a'] = 5
print(ordered_dict)  # OrderedDict([('a', 5), ('b', 2), ('c', 3)])
```

Go back to [Contents](#contents).


**Example 6:** Pop Items

Popping the last item from the `OrderedDict`.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

ordered_dict.popitem()
print(ordered_dict)  # Removes ('c', 3) -> Output: OrderedDict({'a': 1, 'b': 2})
```

Go back to [Contents](#contents).


**Example 7:** Pop Items (Last=False)

Popping the first item by specifying `last=False`.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

ordered_dict.popitem(last=False)
print(ordered_dict)  # Removes ('a', 1)
```

Go back to [Contents](#contents).


**Example 8:** Move to End

Moving an existing key to the end.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Moves 'b' to the end
ordered_dict.move_to_end('b')
print(ordered_dict) # Output: OrderedDict([('a', 1), ('c', 3), ('b', 2)])  # Moves 'b' to the end
```

Go back to [Contents](#contents).


**Example 9:** Move to Beginning

Moving an existing key to the beginning.

```python
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Moves 'b' to the beginning
ordered_dict.move_to_end('b', last=False)
print(ordered_dict) # Output: OrderedDict([('b', 2), ('a', 1), ('c', 3)])
```

Go back to [Contents](#contents).


**Example 10:** Creating from a Regular Dict

Creating an OrderedDict from a regular dict (order of the regular dict is preserved as of Python 3.7+).

```python
from collections import OrderedDict

regular_dict = {'one': 1, 'two': 2, 'three': 3}
ordered_dict_from_regular = OrderedDict(regular_dict)
# Output order is the same as the input dict
print(ordered_dict_from_regular)  # Output: OrderedDict([('one', 1), ('two', 2), ('three', 3)])
```


#### defaultdict

The `defaultdict` is a subclass of `dict` that calls a factory function to supply missing values, simplifying the code as there is no need to check if a key is present.

For example:

```python
from collections import defaultdict

dd = defaultdict(int)  # default factory is int, which defaults to 0
dd['a'] += 1
print(dd['a'])  # Output: 1
```

Go back to [Contents](#contents).



##### More 10 defaultdict examples

Go back to [Contents](#contents).


**Example 1:** Integer Default

Creating a `defaultdict` with default type `int`, useful for counting.

```python
from collections import defaultdict

int_default = defaultdict(int)  # Default value of 0 for new keys
int_default['a'] += 1
int_default['b'] += 2
print(int_default)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 2})
```

Go back to [Contents](#contents).


**Example 2:** List Default

Using `list` as the default factory, which is great for grouping.

```python
from collections import defaultdict

list_default = defaultdict(list)
list_default['key1'].append(1)
list_default['key1'].append(2)
list_default['key2'].append(3)
print(list_default)  # Output: defaultdict(<class 'list'>, {'key1': [1, 2], 'key2': [3]})
```

Go back to [Contents](#contents).


**Example 3:** Set Default

Using `set` as the default factory for storing unique elements.

```python
from collections import defaultdict

set_default = defaultdict(set)
set_default['a'].add(1)
set_default['a'].add(2)
set_default['a'].add(1)  # Duplicate, won't be added
print(set_default)  # Output: defaultdict(<class 'set'>, {'a': {1, 2}})
```

Go back to [Contents](#contents).


**Example 4:** Dictionary Default

Creating a `defaultdict` of dictionaries.

```python
from collections import defaultdict

dict_default = defaultdict(dict)
dict_default['a']['inner_key'] = 'value'
print(dict_default)  # Output: defaultdict(<class 'dict'>, {'a': {'inner_key': 'value'}})
```

Go back to [Contents](#contents).


**Example 5:** Default Value with lambda

Using `lambda` to provide a custom default value.

```python
from collections import defaultdict

lambda_default = defaultdict(lambda: 'default value')
print(lambda_default['a'])  # Output: default value
```

Go back to [Contents](#contents).


**Example 6:** Counting Items in a List

Counting items in a list by combining `defaultdict` with `int`.

```python
from collections import defaultdict

words = ['apple', 'banana', 'apple', 'pear', 'banana', 'orange']
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print(word_count)  # Count of each word
```

Go back to [Contents](#contents).


**Example 7:** Grouping Items

Grouping items based on a property.

```python
from collections import defaultdict

names = ['Alan', 'Alena', 'Bob', 'Alice']
grouped_by_first_letter = defaultdict(list)

for name in names:
    grouped_by_first_letter[name[0]].append(name)

# Names grouped by the first letter
print(grouped_by_first_letter) # Output: defaultdict(<class 'list'>, {'A': ['Alan', 'Alena', 'Alice'], 'B': ['Bob']})
```

Go back to [Contents](#contents).


**Example 8:** Summarizing Data

Summarizing data, for example, calculating total sales by product.

```python
from collections import defaultdict

sales_data = [('apple', 2), ('banana', 3), ('apple', 5), ('banana', 2)]

total_sales = defaultdict(int)

for product, units in sales_data:
    total_sales[product] += units

print(total_sales)  # Total units sold per product
```

Go back to [Contents](#contents).


**Example 9:** Building a Graph Representation

Using `defaultdict` to build a simple graph representation.

```python
from collections import defaultdict

edges = [('a', 'b'), ('b', 'c'), ('a', 'c'), ('c', 'd')]

graph = defaultdict(list)

for start, end in edges:
    graph[start].append(end)
    
print(graph)  # Adjacency list representation of the graph
```

Go back to [Contents](#contents).


**Example 10:** Default Factory with Function

Using a function as a default factory to create complex defaults.

```python
from collections import defaultdict

def default_factory():
    return 'Undefined'

custom_default = defaultdict(default_factory)
print(custom_default['a'])  # Output: Undefined
```


#### UserDict

The `UserDict` is a wrapper around dictionary objects that makes it easier to create subclasses of dictionaries by providing standard methods and adding a few of its own.

For example:

```python
from collections import UserDict

class MyDict(UserDict):
    # Custom behavior can be added here
    pass
```

Go back to [Contents](#contents).



##### More 10 UserDict examples

Here are 10 examples demonstrating various uses of `UserDict`.

Go back to [Contents](#contents).


**Example 1:** Basic Custom Dictionary

Creating a basic custom dictionary that inherits from `UserDict`.

```python
from collections import UserDict

class MyDict(UserDict):
    pass

my_dict = MyDict()
my_dict['key'] = 'value'
print(my_dict)  # Output: {'key': 'value'}
```

Go back to [Contents](#contents).


**Example 2:** Initializing with Default Values

A custom dictionary that initializes with default values.

```python
from collections import UserDict

class DefaultDict(UserDict):
    def __init__(self, defaults=None):
        super().__init__()
        if defaults:
            self.data.update(defaults)

default_values = {'a': 1, 'b': 2}
my_default_dict = DefaultDict(default_values)
print(my_default_dict)  # Output: {'a': 1, 'b': 2}
```

Go back to [Contents](#contents).


**Example 3:** Overriding setitem

Customizing set behavior to only accept integer values.

```python
from collections import UserDict

class IntDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        super().__setitem__(key, value)

int_dict = IntDict()
int_dict['number'] = 5
print(int_dict)  # Output: {'number': 5}
# int_dict['number'] = 'five'  # Raises ValueError
```

Go back to [Contents](#contents).


**Example 4:** Logging Accesses

Logging every time a key is accessed.

```python
from collections import UserDict

class LoggingDict(UserDict):
    def __getitem__(self, key):
        print(f"Accessing: {key}")
        return super().__getitem__(key)

log_dict = LoggingDict({'a': 1, 'b': 2})
print(log_dict['a'])  # Output: Accessing: a \n 1
```

Go back to [Contents](#contents).


**Example 5:** Counting Key Accesses

Counting how many times each key is accessed.

```python
from collections import UserDict, defaultdict

class CountingDict(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.access_count = defaultdict(int)

    def __getitem__(self, key):
        self.access_count[key] += 1
        return super().__getitem__(key)

count_dict = CountingDict({'a': 1})
_ = count_dict['a']
_ = count_dict['a']
print(count_dict.access_count)  # Output: defaultdict(<class 'int'>, {'a': 2})
```

Go back to [Contents](#contents).


**Example 6:** Read-Only Dictionary

Creating a read-only dictionary where values cannot be changed after being set.

```python
from collections import UserDict

class ReadOnlyDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            raise ValueError("Cannot modify existing value")
        super().__setitem__(key, value)

readonly_dict = ReadOnlyDict({'a': 1})
# readonly_dict['a'] = 2  # Raises ValueError
```

Go back to [Contents](#contents).


**Example 7:** Key Validation

Ensuring only strings are used as keys.

```python
from collections import UserDict

class StringKeysDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        super().__setitem__(key, value)

str_keys_dict = StringKeysDict()
str_keys_dict['key'] = 'value'
# str_keys_dict[1] = 'value'  # Raises ValueError
```

Go back to [Contents](#contents).


**Example 8:** Value Transformation

Automatically transforming values to uppercase when set.

```python
from collections import UserDict

class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value.upper())

upper_dict = UpperCaseDict()
upper_dict['greeting'] = 'hello'
print(upper_dict)  # Output: {'greeting': 'HELLO'}
```

Go back to [Contents](#contents).


**Example 9:** Default Values

Returning a default value for missing keys.

```python
from collections import UserDict

class DefaultUserDict(UserDict):
    def __getitem__(self, key):
        return self.data.get(key, 'default')

default_user_dict = DefaultUserDict()
print(default_user_dict['missing'])  # Output: default
```

Go back to [Contents](#contents).


**Example 10:** Combining Dictionaries

A class that combines multiple dictionaries into a single view.

```python
from collections import UserDict

class MultiDict(UserDict):
    def add_dict(self, other_dict):
        for key, value in other_dict.items():
            self.data[key] = value

multi_dict = MultiDict({'a': 1})
multi_dict.add_dict({'b': 2, 'c': 3})
print(multi_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
```


#### UserList

The `UserList` is a wrapper around list objects. It's designed for creating subclasses of lists with more specialized behavior than the standard `list`.

For example:

```python
from collections import UserList

class MyList(UserList):
    # Custom behavior can be added here
    pass
```

Go back to [Contents](#contents).



##### More 10 UserList examples

Here are 10 examples illustrating various ways UserList can be extended and utilized to meet specific requirements.

Go back to [Contents](#contents).


**Example 1:** BoundedList

Limits the list to a maximum number of elements.

```python
from collections import UserList

class BoundedList(UserList):
    def __init__(self, *args, max_length=10, **kwargs):
        self.max_length = max_length
        super().__init__(*args, **kwargs)

    def append(self, item):
        if len(self.data) < self.max_length:
            super().append(item)
        else:
            raise ValueError("List has reached its maximum length")

bounded_list = BoundedList(max_length=2)
bounded_list.append(1)
bounded_list.append(2)

print(bounded_list) # Output: [1, 2]

# bounded_list.append(3)  # This would raise a ValueError
```

Go back to [Contents](#contents).


**Example 2:** UniqueList

Ensures all elements in the list are unique.

```python
from collections import UserList

class UniqueList(UserList):
    def append(self, item):
        if item not in self.data:
            super().append(item)
        else:
            raise ValueError("Item already exists in the list")

unique_list = UniqueList()
unique_list.append(1)
unique_list.append(2)
# unique_list.append(1)  # This would raise a ValueError
```

Go back to [Contents](#contents).


**Example 3:** SortedList

Automatically keeps the list sorted.

```python
from collections import UserList

class SortedList(UserList):
    def append(self, item):
        super().append(item)
        self.data.sort()

sorted_list = SortedList()
sorted_list.append(3)
sorted_list.append(1)
sorted_list.append(2)
print(sorted_list)  # Output: [1, 2, 3]
```

Go back to [Contents](#contents).


**Example 4:** Typed List

Enforces that all elements in the list are of a specific type.

```python
from collections import UserList

class TypedList(UserList):
    def __init__(self, type_, *args, **kwargs):
        self.type_ = type_
        super().__init__(*args, **kwargs)

    def append(self, item):
        if not isinstance(item, self.type_):
            raise TypeError(f"Item must be of type {self.type_.__name__}")
        super().append(item)

typed_list = TypedList(int)
typed_list.append(1)

print(typed_list) # Output: [1]

# typed_list.append('string')  # This would raise a TypeError
```

Go back to [Contents](#contents).


**Example 5:** LoggingList

Logs every addition to the list.

```python
from collections import UserList

class LoggingList(UserList):
    def append(self, item):
        print(f"Appending {item}")
        super().append(item)

logging_list = LoggingList()
logging_list.append("item")  # Output: Appending item
```

Go back to [Contents](#contents).


**Example 6:** PrependList

Adds a method to prepend items to the list.

```python
from collections import UserList

class PrependList(UserList):
    def prepend(self, item):
        self.data.insert(0, item)

prepend_list = PrependList()
prepend_list.prepend(1)
prepend_list.append(2)
print(prepend_list)  # Output: [1, 2]
```

Go back to [Contents](#contents).


**Example 7:** CallbackList

Executes a callback function every time an item is added.

```python
from collections import UserList

class CallbackList(UserList):
    def __init__(self, *args, callback=None, **kwargs):
        self.callback = callback
        super().__init__(*args, **kwargs)

    def append(self, item):
        if callable(self.callback):
            self.callback(item)
        super().append(item)

callback_list = CallbackList(callback=lambda x: print(f"Added {x}"))
callback_list.append(1)  # Output: Added 1
```

Go back to [Contents](#contents).


**Example 8:** SquaringList

Automatically squares numbers when they are added.

```python
from collections import UserList

class SquaringList(UserList):
    def append(self, item):
        if isinstance(item, int):
            item = item ** 2
        super().append(item)

squaring_list = SquaringList()
squaring_list.append(3)
print(squaring_list)  # Output: [9]
```

Go back to [Contents](#contents).


**Example 9:** FilteredList

Only appends items that satisfy a certain condition.

```python
from collections import UserList

class FilteredList(UserList):
    def append(self, item):
        if item > 0:
            super().append(item)

filtered_list = FilteredList()
filtered_list.append(-1)
filtered_list.append(2)
print(filtered_list)  # Output: [2]
```

Go back to [Contents](#contents).


**Example 10:** MultiAppendList

Appends multiple items at once.

```python
from collections import UserList

class MultiAppendList(UserList):
    def extend(self, items):
        for item in items:
            if item not in self.data:
                super().append(item)

multi_append_list = MultiAppendList()
multi_append_list.extend([1, 2, 3, 2])
print(multi_append_list)  # Output: [1, 2, 3]
```



#### UserString

The `UserString` acts as a wrapper around string objects, facilitating the subclassing of strings to alter or extend their behavior.

For example:

```python
from collections import UserString

class MyString(UserString):
    # Custom behavior can be added here
    pass
```

Go back to [Contents](#contents).



##### More 10 UserString examples

Here is the complete Python code that demonstrates the 10 examples using UserString along with how to use them.

Go back to [Contents](#contents).

```python
from collections import UserString

# Example 1: AppendSuffixString
class AppendSuffixString(UserString):
    def __init__(self, seq, suffix):
        super().__init__(seq)
        self.suffix = suffix

    def __add__(self, other):
        return AppendSuffixString(super().__add__(other), self.suffix) + self.suffix

# Example 2: PrependString
class PrependString(UserString):
    def __init__(self, seq, prefix):
        super().__init__(prefix + seq)

# Example 3: UpperCaseString
class UpperCaseString(UserString):
    def __init__(self, seq):
        super().__init__(seq.upper())

# Example 4: MaskString
class MaskString(UserString):
    def __init__(self, seq, mask_char='*'):
        masked = mask_char * len(seq)
        super().__init__(masked)

# Example 5: RepeatString
class RepeatString(UserString):
    def __init__(self, seq, times):
        repeated = seq * times
        super().__init__(repeated)

# Example 6: ReverseString
class ReverseString(UserString):
    def __init__(self, seq):
        reversed_seq = seq[::-1]
        super().__init__(reversed_seq)

# Example 7: ReplaceVowelsString
class ReplaceVowelsString(UserString):
    def __init__(self, seq, replacement='*'):
        replaced = ''.join([replacement if c in 'aeiouAEIOU' else c for c in seq])
        super().__init__(replaced)

# Example 8: CamelCaseString
class CamelCaseString(UserString):
    def __init__(self, seq):
        camel_case = ''.join(word.capitalize() for word in seq.split('_'))
        super().__init__(camel_case)

# Example 9: ConcatenateString
class ConcatenateString(UserString):
    def __add__(self, other):
        return ConcatenateString(super().__add__(other))

# Example 10: NumericString
class NumericString(UserString):
    def __init__(self, seq):
        numeric = ''.join(filter(str.isdigit, seq))
        super().__init__(numeric)

# Using the classes
if __name__ == "__main__":
    # AppendSuffixString usage
    append_suffix_instance = AppendSuffixString("Hello", "World")
    print(append_suffix_instance)  # Output: Hello

    # PrependString usage
    prepend_instance = PrependString("Hello", "World")
    print(prepend_instance)  # Output: WorldHello

    # UpperCaseString usage
    upper_case_instance = UpperCaseString("hello")
    print(upper_case_instance)  # Output: HELLO

    # MaskString usage
    mask_instance = MaskString("password")
    print(mask_instance)  # Output: ********

    # RepeatString usage
    repeat_instance = RepeatString("ha", 3)
    print(repeat_instance)  # Output: hahaha

    # ReverseString usage
    reverse_instance = ReverseString("hello")
    print(reverse_instance)  # Output: olleh

    # ReplaceVowelsString usage
    replace_vowels_instance = ReplaceVowelsString("hello")
    print(replace_vowels_instance)  # Output: h*ll*

    # CamelCaseString usage
    camel_case_instance = CamelCaseString("hello_world")
    print(camel_case_instance)  # Output: HelloWorld

    # ConcatenateString usage
    concatenate_instance = ConcatenateString("Hello") + " World"
    print(concatenate_instance)  # Output: Hello World

    # NumericString usage
    numeric_instance = NumericString("a1b2c3")
    print(numeric_instance)  # Output: 123
```



## Strings

In Python, a string is a sequence of characters enclosed within quotes. 
- Characters can be anything: letters, numbers, symbols, or whitespace characters (like spaces or tabs), and they are treated as text. 
- Python supports both single (`'...'`), double (`"..."`), and triple (`'''...'''` or `"""..."""`) quotes to denote string literals, allowing for flexibility in handling strings that contain quote characters or span multiple lines.

Strings in Python are immutable, meaning once a string is created, the characters within it cannot be changed. 
- Any operation that modifies a string actually creates a new string, rather than altering the original one. 
- This immutability has implications for performance and safety, as it prevents accidental modification of strings.

Python provides a rich set of operations and methods for working with strings. These include concatenation (joining strings together), slicing (extracting parts of strings), and a wide variety of methods for manipulation (like converting to uppercase or lowercase, trimming whitespace, and finding substrings).

Go back to [Contents](#contents).



### The length function for Strings

Strings are sequences of characters. The `len()` function returns the number of characters in the string.

For example:

```python
my_string = "Hello"
print(len(my_string))  # Output: 5
```

Go back to [Contents](#contents).



### String Methods

Here are examples using different Python string methods to demonstrate their versatility and utility. 

Go back to [Contents](#contents).

1. **capitalize()** - Converts the first character of the string to uppercase and the rest to lowercase.

```python
text = "python programming."
print(text.capitalize())  # Python programming.
```

Go back to [Contents](#contents).

2. **casefold()** - Converts the string to lowercase, designed for caseless matching.

```python
text = "PYTHON PROGRAMMING"
print(text.casefold())  # python programming
```

Go back to [Contents](#contents).

3. **center(width, [fillchar])** - Centers the string within a specified width, optionally filling in with a specified character.

```python
text = "python"
print(text.center(20, '-'))  # -------python-------
```

Go back to [Contents](#contents).

4. **count(sub, [start, [end]])** - Returns the number of occurrences of a substring in the string, optionally within a specified range.

```python
text = "banana"
print(text.count('a'))  # 3
```

Go back to [Contents](#contents).

5. **encode(encoding='utf-8', errors='strict')** - Encodes the string using the specified encoding scheme.

```python
text = "pythön!"
print(text.encode('ascii', 'ignore'))  # b'pythn!'
```

Go back to [Contents](#contents).

6. **endswith(suffix, [start, [end]])** - Returns True if the string ends with the specified suffix, optionally within a specified range.

```python
text = "python.py"
print(text.endswith('.py'))  # True
```

Go back to [Contents](#contents).

7. **expandtabs(tabsize=8)** - Replaces tabs in the string with the specified number of space characters.

```python
text = "python\tprogramming"
print(text.expandtabs(4))  # python  programming
```

Go back to [Contents](#contents).

8. **find(sub, [start, [end]])** - Searches the string for a specified substring and returns the lowest index where it begins or -1 if not found.

```python
text = "hello world"
print(text.find('world'))  # 6
```

Go back to [Contents](#contents).

9. ****format(*args, kwargs)** - Formats the string using the specified values.

```python
text = "Name: {}, Age: {}"
print(text.format("Alice", 30))  # Name: Alice, Age: 30
```

Go back to [Contents](#contents).

10. **format_map(mapping)** - Formats the string using a dictionary of values.

```python
text = "Name: {name}, Age: {age}"
data = {'name': 'Alice', 'age': 30}
print(text.format_map(data))  # Name: Alice, Age: 30
```

Go back to [Contents](#contents).

11. **index(sub, [start, [end]])** - Like find(), but raises ValueError when the substring is not found.

```python
text = "hello world"
print(text.index('world'))  # 6
```

Go back to [Contents](#contents).

12. **isalnum()** - Returns True if all characters in the string are alphanumeric (letters and numbers only).

```python
text = "Python3"
print(text.isalnum())  # True
```

Go back to [Contents](#contents).

13. **isalpha()** - Returns True if all characters in the string are alphabetic.

```python
text = "Python"
print(text.isalpha())  # True
```

Go back to [Contents](#contents).

14. **isascii()** - Returns True if all characters in the string are ASCII.

```python
text = "Python"
print(text.isascii())  # True
```

Go back to [Contents](#contents).

15. **isdecimal()** - Returns True if all characters in the string are decimal characters. 

- Decimal characters are those that can be used to form numbers in base 10, which means they include the numbers 0 through 9 and a subset of Unicode characters that represent decimal numbers. 
- This method does not consider characters that represent numbers in other bases or numeric forms that aren't used in decimal number representation (such as fractions, subscripts, superscripts, Roman numerals, and other numeral systems) as decimal characters.

```python
text = "1234567890"
print(text.isdecimal())  # True
```

Example returning `False`.

```python
text = "\u00B2"  # Superscript two ('²')
print(text.isdecimal())  # False
```

Go back to [Contents](#contents).

16. **isdigit()** - Returns True if all characters in the string are digits.

- This includes all characters that the Unicode standard identifies as "digit," which not only includes decimal characters (0-9) but also digits from other numeral systems (like the superscript two '²', Arabic-Indic digits, and more).
- Essentially, `text.isdigit()` is broader in scope than text.isdecimal(), as it accepts more characters, including those that are considered numeric but not strictly decimal.

```python
text = "1234567890"
print(text.isdigit())  # True
```

Example where it also returns True, differing from `isdecimal()`:

```python
text = "\u00B2"  # Superscript two ('²')
print(text.isdigit())  # True
```

Go back to [Contents](#contents).

17. **isidentifier()** - Returns True if the string is a valid identifier according to Python syntax.

```python
text = "variable_name"
print(text.isidentifier())  # True
```

Go back to [Contents](#contents).

18. **islower()** - Returns True if all cased characters in the string are lowercase.

```python
text = "python"
print(text.islower())  # True
```

Go back to [Contents](#contents).

19. **isnumeric()** - Returns True if all characters in the string are numeric characters.

```python
text = "12345"
print(text.isnumeric())  # True
```

Go back to [Contents](#contents).

20. **isprintable()** - Returns True if all characters in the string are printable or the string is empty.

```python
text = "Python 3.8"
print(text.isprintable())  # True
```

Go back to [Contents](#contents).

21. **isspace()** - Returns True if all characters in the string are whitespace characters.

```python
text = "   "
print(text.isspace())  # True
```

Go back to [Contents](#contents).

22. **istitle()** - Returns True if the string is titled (first character of each word is uppercase, others are lowercase).

```python
text = "Hello World"
print(text.istitle())  # True
```

Go back to [Contents](#contents).

23. **isupper()** - Returns True if all cased characters in the string are uppercase.

```python
words = ["Python", "Programming"]
print(" ".join(words))  # Python Programming
```

Go back to [Contents](#contents).

24. **join(iterable)** - Concatenates the strings in the provided iterable, separating them by the string providing this method.

```python
text = "python"
print(text.ljust(10, '-'))  # python----
```

Go back to [Contents](#contents).

25. **ljust(width, [fillchar])** - Returns the string left-justified in a string of specified width.

```python
text = "python"
print(text.ljust(10, '-'))  # python----
```

Go back to [Contents](#contents).

26. **lower()** - Converts all characters in the string to lowercase.

```python
text = "PYTHON"
print(text.lower())  # python
```

Go back to [Contents](#contents).

27. **lstrip([chars])** - Returns a copy of the string with leading characters removed.

```python
text = "   python"
print(text.lstrip())  # 'python'
```

Go back to [Contents](#contents).

28. **maketrans(intab, outtab)** - Creates a translation table to be used in translations.

```python
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
text = "python programming"
print(text.translate(trantab))  # pyth4n pr4gr1mm1ng
```

Go back to [Contents](#contents).

29. **partition(sep)** - Splits the string at the first occurrence of sep, and returns a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.

```python
text = "hello world python"
print(text.partition('world'))  # ('hello ', 'world', ' python')
```

Go back to [Contents](#contents).

30. **replace(old, new[, count])** - Returns a string where all occurrences of the old substring are replaced by the new one.

```python
text = "hello world"
print(text.replace('world', 'Python'))  # hello Python
```

Go back to [Contents](#contents).

31. **rfind(sub, [start, [end]])** - Searches the string for a specified substring and returns the highest index where it begins or -1 if not found.

```python
text = "hello world world"
print(text.rfind('world'))  # 12
```

Go back to [Contents](#contents).

32. **rindex(sub, [start, [end]])** - Like rfind(), but raises ValueError when the substring is not found.

```python
text = "hello world world"
print(text.rindex('world'))  # 12
```

Go back to [Contents](#contents).

33. **rjust(width, [fillchar])** - Returns the string right-justified in a string of specified width.

```python
text = "python"
print(text.rjust(10, '-'))  # ----python
```

Go back to [Contents](#contents).

34. **rpartition(sep)** - Splits the string at the last occurrence of sep, and returns a 3-tuple containing the part before the separator, the separator itself, and the part after the separator.

```python
text = "hello world python"
print(text.rpartition('world'))  # ('hello ', 'world', ' python')
```

Go back to [Contents](#contents).

35. **rsplit(sep=None, maxsplit=-1)** - Splits the string at the specified separator and returns a list. If maxsplit is specified, splits at most maxsplit times.

```python
text = "hello world python programming"
print(text.rsplit(' ', 2))  # ['hello world', 'python', 'programming']
```

Go back to [Contents](#contents).

36. **rstrip([chars])** - Returns a copy of the string with trailing characters removed.

```python
text = "python   "
print(text.rstrip())  # 'python'
```

Go back to [Contents](#contents).

37. **split(sep=None, maxsplit=-1)** - Splits the string at the specified separator and returns a list. If maxsplit is specified, splits at most maxsplit times.

```python
text = "hello world python"
print(text.split())  # ['hello', 'world', 'python']
```

Go back to [Contents](#contents).

38. **splitlines([keepends])** - Splits the string at line breaks and returns a list.

```python
text = "hello\nworld"
print(text.splitlines())  # ['hello', 'world']
```

Go back to [Contents](#contents).

39. **startswith(prefix, [start, [end]])** - Returns True if the string starts with the specified prefix, optionally within a specified range.

```python
text = "python programming"
print(text.startswith('python'))  # True
```

Go back to [Contents](#contents).

40. **strip([chars])** - Returns a copy of the string with leading and trailing characters removed.

```python
text = "   python   "
print(text.strip())  # 'python'
```

Go back to [Contents](#contents).

41. **swapcase()** - Converts uppercase characters to lowercase and vice versa.

```python
text = "Python Programming"
print(text.swapcase())  # pYTHON pROGRAMMING
```

Go back to [Contents](#contents).

42. **title()** - Converts the first character of each word to uppercase and the rest to lowercase.

```python
text = "python programming"
print(text.title())  # Python Programming
```

Go back to [Contents](#contents).

43. **translate(table)** - Translates the string according to the translation table specified by maketrans().

```python
text = "hello world"
trantab = str.maketrans('aeiou', '12345')
print(text.translate(trantab))  # h2ll4 w4rld
```

Go back to [Contents](#contents).

44. **upper()** - Converts all characters in the string to uppercase.

```python
text = "hello world"
trantab = str.maketrans('aeiou', '12345')
print(text.translate(trantab))  # h2ll4 w4rld
```

Go back to [Contents](#contents).

45. **zfill(width)** - Pads the string on the left with zeros until it reaches the specified width.

```python
text = "42"
print(text.zfill(5))  # 00042
```

Go back to [Contents](#contents).



## Slicing

Slicing in Python is a technique that allows you to extract a part of a collection or string. It works by specifying a start index and an optional end index, along with an optional step.

The basic syntax for slicing is `[start:end:step]`, where:

- `start` is the index at which the slice starts (inclusive).
- `end` is the index at which the slice ends (exclusive).
- `step` is the interval between each index for slicing.

If `step` is not provided, it defaults to 1. If `start` or `end` are omitted, they default to the start or end of the sequence, respectively.

Go back to [Contents](#contents).



### List Slicing

Here are 10 examples of slicing lists in Python, demonstrating various combinations of start, end, and step values.

These examples demonstrate the flexibility of list slicing in Python, allowing for efficient and concise data manipulation.

Go back to [Contents](#contents).



1. Basic Slicing - Get the first 3 elements of a list.

```python
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[0:3])  # Output: [0, 1, 2]
```

Go back to [Contents](#contents).

2. Omitting Start Index - Slice from the beginning until a specific index.

```python
print(my_list[:4])  # Output: [0, 1, 2, 3]
```

Go back to [Contents](#contents).

3. Omitting End Index - Slice from a specific index to the end.

```python
print(my_list[3:])  # Output: [3, 4, 5]
```

Go back to [Contents](#contents).

4. Negative Start Index - Use a negative index to start the slice.

```python
print(my_list[-4:])  # Output: [2, 3, 4, 5]
```

Go back to [Contents](#contents).

5. Negative End Index - Use a negative index to end the slice.

```python
print(my_list[:-2])  # Output: [0, 1, 2, 3]
```

Go back to [Contents](#contents).

6. Step Value - Use a step value to skip elements in the slice.

```python
print(my_list[0:6:2])  # Output: [0, 2, 4]
```

Go back to [Contents](#contents).

7. Negative Step Value - Reverse the list or part of it.

```python
print(my_list[::-1])  # Output: [5, 4, 3, 2, 1, 0]
```

Go back to [Contents](#contents).

8. Slicing with All Parameters - Combine start, end, and step.

```python
print(my_list[1:5:2])  # Output: [1, 3]
```

Go back to [Contents](#contents).

9. Omitting All Indices - Duplicate the list with slicing.

```python
print(my_list[:])  # Output: [0, 1, 2, 3, 4, 5]
```

Go back to [Contents](#contents).

10. Using Only Step Value - Get every second element of the list.

```python
print(my_list[::2])  # Output: [0, 2, 4]
```

Go back to [Contents](#contents).



### Tuple Slicing


Here are 10 examples to illustrate different slicing techniques for tuples. 

These examples showcase how slicing can be used with tuples in Python to access specific portions or patterns within the tuple, similar to how it's done with lists.

Go back to [Contents](#contents).



1. Basic Slicing - Get the first 3 elements of a tuple.

```python
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[0:3])  # Output: (0, 1, 2)
```

Go back to [Contents](#contents).

2. Omitting Start Index - Slice from the beginning until a specific index.

```python
print(my_tuple[:4])  # Output: (0, 1, 2, 3)
```

Go back to [Contents](#contents).

3. Omitting End Index - Slice from a specific index to the end.

```python
print(my_tuple[3:])  # Output: (3, 4, 5)
```

Go back to [Contents](#contents).

4. Negative Start Index - Use a negative index to start the slice.

```python
print(my_tuple[-4:])  # Output: (2, 3, 4, 5)
```

Go back to [Contents](#contents).

5. Negative End Index - Use a negative index to end the slice.

```python
print(my_tuple[:-2])  # Output: (0, 1, 2, 3)
```

Go back to [Contents](#contents).

6. Step Value - Use a step value to skip elements in the slice.

```python
print(my_tuple[0:6:2])  # Output: (0, 2, 4)
```

Go back to [Contents](#contents).

7. Negative Step Value - Reverse the tuple or part of it.

```python
print(my_tuple[::-1])  # Output: (5, 4, 3, 2, 1, 0)
```

Go back to [Contents](#contents).

8. Slicing with All Parameters - Combine start, end, and step.

```python
print(my_tuple[1:5:2])  # Output: (1, 3)
```

Go back to [Contents](#contents).

9. Omitting All Indices - Create a copy of the tuple with slicing.

```python
print(my_tuple[:])  # Output: (0, 1, 2, 3, 4, 5)
```

Go back to [Contents](#contents).

10. Using Only Step Value - Get every second element of the tuple.

```python
print(my_tuple[::2])  # Output: (0, 2, 4)
```

Go back to [Contents](#contents).



### String Slicing

Slicing strings in Python is very similar to slicing lists and tuples. 

Here are 10 examples to demonstrate different slicing techniques for strings.

These examples demonstrate how slicing can be applied to strings in Python, enabling you to extract substrings, reverse strings, and skip characters in flexible ways.

Go back to [Contents](#contents).



1. Basic Slicing - Get the first 5 characters of a string.

```python
my_string = "Hello, World!"
print(my_string[0:5])  # Output: Hello
```

Go back to [Contents](#contents).

2. Omitting Start Index - Slice from the beginning until a specific index.

```python
print(my_string[:7])  # Output: Hello,
```

Go back to [Contents](#contents).

3. Omitting End Index - Slice from a specific index to the end.

```python
print(my_string[7:])  # Output: World!
```

Go back to [Contents](#contents).

4. Negative Start Index - Use a negative index to start the slice.

```python
print(my_string[-6:])  # Output: World!
```

Go back to [Contents](#contents).

5. Negative End Index - Use a negative index to end the slice.

```python
print(my_string[:-1])  # Output: Hello, World
```

Go back to [Contents](#contents).

6. Step Value - Use a step value to skip characters in the slice.

```python
print(my_string[::2])  # Output: Hlo ol!
```

Go back to [Contents](#contents).

7. Negative Step Value - Reverse the string.

```python
print(my_string[::-1])  # Output: !dlroW ,olleH
```

Go back to [Contents](#contents).

8. Slicing with All Parameters - Combine start, end, and step.

```python
print(my_string[1:10:2])  # Output: el,Wo
```

Go back to [Contents](#contents).

9. Omitting All Indices with Step - Use step value to get every character, reversing the string.

```python
print(my_string[::-2])  # Output: !lo olH
```

Go back to [Contents](#contents).

10. Using Only Step Value - Get every character using a positive step.

```python
print(my_string[::1])  # Output: Hello, World!
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



## Comprehensions

Comprehensions in Python provide a concise, readable way to create lists, dictionaries, and sets. They offer a simpler syntax when you want to create a new collection based on the values of an existing collection.

Go back to [Contents](#contents).

### List Comprehensions

List Comprehensions are a beautiful way to create new lists by applying an expression to each element of an existing iterable. 

For example, let’s say we want to square each number in a list. Here’s how you can do it with a list comprehension:

```python
numbers = [1, 2, 3, 4, 5]
squared = [number ** 2 for number in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]
```

This one-line (`squared = [number ** 2 for number in numbers]`) replaces multiple lines of a traditional `for` loop, making your code compact and readable.

Go back to [Contents](#contents).

### Dictionary Comprehensions

Moving on to Dictionary Comprehensions, which are similar, but they create dictionaries instead of lists. You can transform and filter data into key-value pairs. 

For example, creating a dictionary where keys are numbers and values are their squares:

```python
numbers = [1, 2, 3, 4, 5]
squared_dict = {number: number ** 2 for number in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Go back to [Contents](#contents).

### Set Comprehensions

Set Comprehensions work similarly, but are used for creating sets. The syntax is almost identical to list comprehensions, but with curly braces. 

An example can be creating a set of even numbers:

```python
numbers = [1, 2, 3, 4, 5, 2, 3, 4]
evens = {number for number in numbers if number % 2 == 0}
print(evens)  # Output: {2, 4}
```

Notice how duplicates are automatically removed, which is a characteristic of sets.

Go back to [Contents](#contents).

### Some Comprehensions examples

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



## Lambda Functions

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

### Lambda Function Example

Lambda functions are often used in situations where you need a simple function for a short period and don’t want to formally define it using the standard `def` keyword.

For example, consider a simple lambda function that adds two numbers:

```python
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

In this example, `lambda x, y: x + y` is an anonymous function that takes two arguments and returns their sum. This code assign this lambda function to the variable `add`, and then we can use it just like any other function.

Go back to [Contents](#contents).

### Lambda Functions Usage

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

### Some Lambda Functions examples

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



## Map and Filter

Next, let's explore two of Python's built-in functions that incorporate functional programming: `map` and `filter`. 

These functions provide elegant, concise ways to perform operations on iterable collections like lists, tuples, or even strings.

Notes: 

- `map` and `filter` are incredibly useful for handling iterable collections in Python. 
- They enable you to write cleaner, more readable code by abstracting the loop mechanism, making your code more in line with the functional programming paradigm.

Go back to [Contents](#contents).

### The map function

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

### The filter function

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

### Some Map and Filter examples

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



## Working with Files

File operations are a fundamental part of programming, particularly when it comes to storing and retrieving data. 

Go back to [Contents](#contents).

### File Operations

Python makes reading from and writing to files very straightforward. 

When you want to read from or write to a file, you first need to open it using the `open()` function. 
- This function returns a file object, which provides methods and attributes to interact with the file content.

For example, to read from a file:

```python
file = open('example.txt', 'r')
content = file.read()
file.close()
print(content)
```

To write to a file, you should open it in write mode ('w'), which creates the file if it doesn’t exist or overwrites it if it does:

```python
file = open('example.txt', 'w')
file.write('Hello, Python!')
file.close()
```

Go back to [Contents](#contents).

### File Handling Modes

The mode in which you open a file determines what actions you can perform on it. 

Common modes include 'r' for read-only, 'w' for write (which overwrites the file), 'a' for append (which adds to the end of the file), and 'r+' for both reading and writing.

Go back to [Contents](#contents).

### Context Managers

A context manager in Python is used for resource management and helps you to automatically manage resources like file streams. 

Using the `with` statement, you can ensure that resources are properly acquired and released. 

When you use a context manager to open a file, it ensures that the file is closed automatically after the block of code is executed, even if an exception occurs.

Here’s how you use a context manager to work with files:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # The file is automatically closed after this block
```

Go back to [Contents](#contents).

### Some examples of how to work with Files in Python

Go back to [Contents](#contents).

**Problem 1:** Read a File

Read the entire content of a file.

Solution: 

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

Go back to [Contents](#contents).

**Problem 2:** Write to a File

Write a string to a file.

Solution: 

```python
with open('example.txt', 'w') as file:
    file.write("Hello, Python!")
```

Go back to [Contents](#contents).

**Problem 3:** Append to a File

Append a string to the end of a file.

Solution: 

```python
with open('example.txt', 'a') as file:
    file.write("\nAppending a new line.")   
```

Go back to [Contents](#contents).

**Problem 4:** Read a File Line by Line

Read a file line by line and print each line.

Solution: 

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')
```

Go back to [Contents](#contents).

**Problem 5:** Write Multiple Lines to a File

Write multiple lines to a file.

Solution: 

```python
lines = ["First line", "Second line", "Third line"]
with open('example.txt', 'w') as file:
    for line in lines:
        file.write(line + "\n")
```

Go back to [Contents](#contents).

**Problem 6:** Check if File Exists

Check if a file exists before trying to read it.

Solution: 

```python
import os

if os.path.exists('example.txt'):
    with open('example.txt', 'r') as file:
        print(file.read())
else:
    print("File does not exist.")
```

Go back to [Contents](#contents).

**Problem 7:** Copy Contents of One File to Another

Copy the contents of one file to another.

Solution: 

```python
with open('source.txt', 'r') as source_file:
    content = source_file.read()

with open('destination.txt', 'w') as dest_file:
    dest_file.write(content)
```

Go back to [Contents](#contents).

**Problem 8:** Read a File in Reverse Order

Read and print a file's content in reverse order.

Solution: 

```python
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in reversed(lines):
        print(line, end='')
```

Go back to [Contents](#contents).

**Problem 9:** Read a Specific Number of Characters

Read the first 10 characters of a file.

Solution: 

```python
with open('example.txt', 'r') as file:
    content = file.read(10)
    print(content)
```

Go back to [Contents](#contents).

**Problem 10:** Writing Data from a List to a File

Write data from a list to a file, each element on a new line.

Solution: 

```python
data = ["Line 1", "Line 2", "Line 3"]
with open('example.txt', 'w') as file:
    for item in data:
        file.write(f"{item}\n")
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

#### Example 1:

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

#### Example 2:

Python strings are implemented using object-oriented programming (OOP) principles. In Python, everything is an object, including strings.
* The Python string class, known as `str`, provides a rich set of methods that allow you to perform a wide variety of operations on string objects, such as case conversion, trimming, splitting, joining, searching, and much more.
* The `str` class defines how string objects are created and manipulated in Python. 
* It encapsulates the data (the sequence of characters) and the behaviors (methods) that can operate on this data. 
  * This is a fundamental concept of OOP, where data and functions are bundled together into objects.

Let's create our own version of a String class, similar to the Python `string`.
- Creating a simple version of the Python string class from scratch can be an instructive exercise in understanding object-oriented programming (OOP) and how strings work internally. 
- We'll implement a basic `MyString` class with a few common string methods. 
- Note that Python's built-in string class is highly optimized and includes many more features than we'll cover here.

The example is divided into three steps:

**Step 1:** Define the MyString Class
- We'll start by defining the class and its initialization method. 
- Our class will need to store the string data, so we'll do that in the constructor.

**Step 2:** Implement Basic Methods
- We'll implement a few basic methods to mimic the functionality of Python's string class, such as `__len__` (to get the length of the string), `__str__` (to return the string representation), and some custom methods like `to_upper` and `to_lower` (to convert the string to uppercase and lowercase, respectively).

**Step 3:** Demonstrate Usage
- Finally, we'll demonstrate how to use the implemented class and its methods.

Next is the `MyString` class implementation.

```python
class MyString:
    def __init__(self, content=""):
        self.content = content

    def __str__(self):
        return self.content

    def __len__(self):
        return len(self.content)
    
    def to_upper(self):
        return MyString(self.content.upper())
    
    def to_lower(self):
        return MyString(self.content.lower())

    def find(self, sub):
        return self.content.find(sub)
    
    def replace(self, old, new):
        return MyString(self.content.replace(old, new))
```

This class definition includes an initializer, methods to get the string's length, its string representation, convert to uppercase and lowercase, find a substring, and replace parts of the string.

Now, let's see how to use the `MyString` class:

```python
# Creating an instance of MyString
my_string = MyString("Hello, World!")

# Printing the string
print(my_string)  # Hello, World!

# Getting the length of the string
print(len(my_string))  # 13

# Converting to uppercase
print(my_string.to_upper())  # HELLO, WORLD!

# Converting to lowercase
print(my_string.to_lower())  # hello, world!

# Finding a substring
print(my_string.find("World"))  # 7

# Replacing a substring
print(my_string.replace("World", "Python"))  # Hello, Python!
```

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

This part is all about organizing and reusing code effectively. 

Python, known for its emphasis on readability and efficiency, provides an excellent mechanism for code reuse through modules and packages.

Go back to [Contents](#contents).

### Modules

In Python, a module is simply a file containing Python definitions and statements. 
- The file name is the module name with the suffix `.py` added. 

Modules can define functions, classes, and variables, and can also include runnable code. 
- They help in breaking down large programs into small manageable and organized namespaces. 

Here's how you create and use a simple module:

Suppose you have a file named `mymodule.py` with the following content:

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

You can use this module in another file as follows:

```python
# main.py
import mymodule

print(mymodule.greet("Alice"))  # Output: Hello, Alice!
```

Go back to [Contents](#contents).

### Packages

Packages are a way of structuring Python’s module namespace by using “dotted module names”. 
- A package can contain one or more modules in it. 
- Creating a package is as simple as putting several modules into a directory and adding a special `__init__.py` file to that directory. 
- Packages allow for a hierarchical structuring of the module namespace and are a great way to organize larger collections of modules.

Go back to [Contents](#contents).

### Import Statements

Python provides several ways to import modules and packages into your programs. You can import a specific attribute from a module, import a module into the current namespace, or even rename a module during import. 

Here are some examples:

* To import a specific function:

```python
from mymodule import greet
print(greet("Bob"))  # Output: Hello, Bob!
```

* To import an entire module:

```python
import mymodule
print(mymodule.greet("Charlie"))  # Output: Hello, Charlie!
```

* To rename a module on import:

```python
import mymodule as mm
print(mm.greet("Dave"))  # Output: Hello, Dave!
```

Go back to [Contents](#contents).

### Why use Modules and Packages

Modules and packages are essential for writing maintainable, scalable, and organized code in Python.
- They not only help in breaking down complex programs but also make code reuse across different programs easier. 
- With `import` statements, you can access the functionality of modules and packages, making your coding process more efficient and modular.

Go back to [Contents](#contents).

### Some Modules and Packages examples

Go back to [Contents](#contents).

**Problem 1:** Create a Simple Module and Use It

Create a module with a function and use it in another file.

Solution: 

* Module Creation (`mymodule.py`):

```python
# mymodule.py
def hello_world():
    return "Hello, World!"
```

* Using the Module (`main.py`):

```python
# main.py
import mymodule
print(mymodule.hello_world())  # Output: Hello, World!
```

Go back to [Contents](#contents).

**Problem 2:** Import Specific Function from a Module

Import a specific function from a module.

Solution: 

* Using a Specific Function:

```python
from mymodule import hello_world
print(hello_world())  # Output: Hello, World!
```

Go back to [Contents](#contents).

**Problem 3:** Create a Package with Multiple Modules

Solution: 

* Package structure:

```markdown
mypackage/
├── __init__.py
├── module1.py
└── module2.py
```

* module1.py:

```python
# module1.py
def function1():
    return "Function 1"
```

* module2.py:

```python
# module2.py
def function2():
    return "Function 2"
```

Go back to [Contents](#contents).

**Problem 4:** Import All Functions from a Module

Use the `*` symbol to import all functions from a module.

Solution:

* Import All Functions:

```python
from mymodule import *
print(hello_world())  # Assuming hello_world is defined in mymodule
```

Go back to [Contents](#contents).

**Problem 5:** Rename Imported Module

Import a module and rename it for ease of use.

Solution: 

* Renaming a Module on Import:

```python
import mymodule as mm
print(mm.hello_world())
```

Go back to [Contents](#contents).

**Problem 6:** Importing a Module from a Package

Import a specific module from a created package.

Solution: 

* Importing from Package:

```python
from mypackage import module1
print(module1.function1())  # Output: Function 1
```

Go back to [Contents](#contents).

**Problem 7:** Import Specific Function from a Package Module

Solution: 

```python
from mypackage.module1 import function1
print(function1())  # Output: Function 1
```

Go back to [Contents](#contents).

**Problem 8:** Nested Packages

Create a nested package and import a module from it.

Solution: 

* Nested package structure:

```markdown
parentpackage/
├── __init__.py
└── childpackage/
    ├── __init__.py
    └── module.py
```

* module.py:

```python
# module.py
def nested_function():
    return "Nested Function"
```

* Importing from Nested Package:

```python
from parentpackage.childpackage import module
print(module.nested_function())  # Output: Nested Function
```

Go back to [Contents](#contents).

**Problem 9:** Conditional Import inside a Function

Perform an import within a function.

Solution: 

* Conditional Import:

```python
def conditional_import():
    import math
    return math.sqrt(16)  # Output: 4.0
print(conditional_import())
```

Go back to [Contents](#contents).

**Problem 10:** Importing a Class from a Module

Define a class in a module and import it.

Solution: 

* Module with Class (`myclassmodule.py`):

```python
# myclassmodule.py
class MyClass:
    def greet(self):
        return "Hello from MyClass"
```

* Importing and Using the Class:

```python
from myclassmodule import MyClass
obj = MyClass()
print(obj.greet())  # Output: Hello from MyClass
```

Go back to [Contents](#contents).



## Unit Tests in Python

Unit testing is a powerful tool to ensure the correctness of your code. 
- Python comes with a built-in module called `unittest` for unit testing. 
- The `unittest` module in Python provides all the necessary functionality to write and run tests, helping you catch bugs early and maintain code quality. 
- A good unit test should be isolated, repeatable, and check a single aspect of the function under test.

Creating unit tests in Python is essential for ensuring that your code behaves as expected and for catching bugs early in the development process. 

Go back to [Contents](#contents).


Here’s how you can create unit tests in Python:


**Step 1:** Import the unittest Module

The `unittest` module provides a set of tools for constructing and running tests. 

To use it, start by importing it in your test file:

```python
import unittest
```

Go back to [Contents](#contents).



**Step 2:** Write a Test Case

A test case is a class that inherits from `unittest.TestCase`. 

This class includes methods to set up, tear down, and define the tests.

Here's an example of a simple test case:

```python
import unittest

def my_function(x, y):
    return x + y

class TestMyFunction(unittest.TestCase):

    def test_addition(self):
        result = my_function(1, 2)
        self.assertEqual(result, 3)
```

In this example, `test_addition` is a method that tests the functionality of my_function. 

The `assertEqual` method is used to check that the result of `my_function(1, 2)` is equal to 3.

Go back to [Contents](#contents).



**Step 3:** SetUp and TearDown

For more complex tests, you might need to set up some initial conditions. 

The `setUp` and `tearDown` methods allow you to define instructions that will be executed before and after each test method, respectively.

```python
import unittest

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        # Code to set up test environment
        pass

    def tearDown(self):
        # Code to clean up after the test
        pass

    def test_addition(self):
        # Test code
        pass
```

Go back to [Contents](#contents).



**Step 4:** Writing Multiple Test Methods

A single test case class can contain multiple test methods. 

Each method should test a specific aspect of your function's behavior.

```python
import unittest

class TestMyFunction(unittest.TestCase):

    def test_addition(self):
        # Test addition
        pass

    def test_subtraction(self):
        # Test subtraction
        pass
```

Go back to [Contents](#contents).



**Step 5:** Running the Tests

You can run your tests in several ways:

* **Running from the Command Line:** 

Navigate to the directory containing your test file and run:

```bash
python -m unittest test_file.py
```

* **Using** `if __name__ == '__main__'`:

If you include the following code at the end of your test file, you can run the test file directly:

```python
import unittest

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).



**Step 6:** Additional Assertions

The `unittest` module provides a variety of assertion methods such as `assertEqual`, `assertTrue`, `assertFalse`, `assertRaises`, etc., to check for various conditions.

Go back to [Contents](#contents).


**Step 7:** Organizing Test Suites

For larger projects, organize your tests into test suites:

```python
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMyFunction('test_addition'))
    suite.addTest(TestMyFunction('test_subtraction'))
    return suite
```

Go back to [Contents](#contents).



### unittest

Here are 10 examples of Python unit tests using the unittest framework. Each example demonstrates testing a different aspect of code functionality.

Go back to [Contents](#contents).



**Example 1:** Testing Equality

```python
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 2:** Testing Equality

```python
import unittest

def subtract(a, b):
    return a - b

class TestMathOperations(unittest.TestCase):
    def test_subtract(self):
        self.assertNotEqual(subtract(5, 3), 1)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 3:** Testing for True

```python
import unittest

def is_even(number):
    return number % 2 == 0

class TestNumber(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 4:** Testing for False

```python
import unittest

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

class TestNumber(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(4))

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 5:** Testing for Exceptions

```python
import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Can not divide by zero")
    return a / b

class TestMathOperations(unittest.TestCase):
    def test_divide_throws_exception(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 6:** Testing with a SetUp Method

```python
import unittest

class TestListMethods(unittest.TestCase):

    def setUp(self):
        self.sample_list = [1, 2, 3]

    def test_append(self):
        self.sample_list.append(4)
        self.assertEqual(self.sample_list, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 7:** Testing Instance Types

```python
import unittest

class MyObject:
    pass

class TestMyObject(unittest.TestCase):
    def test_instance(self):
        obj = MyObject()
        self.assertIsInstance(obj, MyObject)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 8:** Testing String Contains

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def test_string_contains(self):
        self.assertIn("hello", "hello world")

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 9:** Testing List Length

```python
import unittest

class TestListMethods(unittest.TestCase):
    def test_list_length(self):
        sample_list = [1, 2, 3]
        self.assertEqual(len(sample_list), 3)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).


**Example 10:** Testing Dictionary Keys

```python
import unittest

class TestDictionaryMethods(unittest.TestCase):
    def test_key_in_dictionary(self):
        sample_dict = {"name": "John", "age": 30}
        self.assertIn("name", sample_dict)

if __name__ == '__main__':
    unittest.main()
```

Go back to [Contents](#contents).

### pytest

The `pytest` is a popular testing framework for Python that offers a more _pythonic_ way of writing tests compared to the built-in `unittest` framework.
- The pytest official website: https://docs.pytest.org/en/8.0.x/

It is known for its simplicity, scalability, and ability to handle complex test suites. Here's how you can create unit tests using pytest:

Go back to [Contents](#contents).


**Step 1:** Install pytest

First, you need to install `pytest`. You can do this using pip:

```bash
pip install pytest
```

Go back to [Contents](#contents).



**Step 2:** Writing pytest Test Cases

The `pytest` test cases are usually simpler than unittest cases. 
- You don't need to create a class that inherits from anything; 
- simply write functions that start with test_.

Here's a basic example:

```python
# test_example.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) != 3
```

Go back to [Contents](#contents).



**Step 3:** Running Tests with pytest

To run your tests, simply navigate to the directory that contains your test file and run pytest from the command line:

```bash
pytest
```

The `pytest` will automatically discover and run all files of the format `test_*.py` or `*_test.py` in the current directory and its subdirectories.


Go back to [Contents](#contents).


- Parameterized Tests

The `pytest` allows you to easily test different input values using the `@pytest.mark.parametrize` decorator:

```python
import pytest

@pytest.mark.parametrize("input1, input2, expected", [(3, 5, 8), (2, 4, 6)])
def test_add(input1, input2, expected):
    assert add(input1, input2) == expected
```

Go back to [Contents](#contents).



- Fixtures

Fixtures in pytest are a way of providing data, test doubles, or state setup to your tests. Fixtures are created using the @pytest.fixture decorator:

```python
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5
```

Go back to [Contents](#contents).



- Handling Exceptions

To test exceptions with `pytest`, you can use `pytest.raises`:

```python
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
```

Go back to [Contents](#contents).



**Step 4:** Viewing Test Results

When you run tests with pytest, it gives you a detailed report on which tests passed and which failed, along with the reason for the failures.

Here are 10 examples of unit tests using the pytest library in Python. Each example tests a specific function or behavior:

Go back to [Contents](#contents).



#### More pytest Examples

Here are 10 examples of unit tests using the pytest library in Python. 

Each example tests a specific function or behavior.

Go back to [Contents](#contents).


**Example 1:** Testing a Simple Addition Function

```python
# Function to test
def add(a, b):
    return a + b

# Test function
def test_add():
    assert add(3, 4) == 7
```

Go back to [Contents](#contents).


**Example 2:** Testing String Concatenation

```python
def concat_strings(a, b):
    return a + b

def test_concat_strings():
    assert concat_strings("Hello", "World") == "HelloWorld"
```

Go back to [Contents](#contents).


**Example 3:** Testing for an Exception

```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_exception():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Go back to [Contents](#contents).


**Example 4:** Testing a Function That Reverses a List

```python
def reverse_list(lst):
    return lst[::-1]

def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
```

Go back to [Contents](#contents).


**Example 5:** Parameterized Test for Multiplication

```python
import pytest

def multiply(a, b):
    return a * b

@pytest.mark.parametrize("a, b, expected", [(2, 3, 6), (4, 5, 20), (6, 7, 42)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
```

Go back to [Contents](#contents).


**Example 6:** Testing a Dictionary Lookup Function

```python
def get_by_key(dct, key):
    return dct.get(key)

def test_get_by_key():
    assert get_by_key({"a": 1, "b": 2}, "a") == 1
    assert get_by_key({"a": 1, "b": 2}, "c") is None
```

Go back to [Contents](#contents).


**Example 7:** Testing a Function That Checks for Even Numbers

```python
def is_even(num):
    return num % 2 == 0

def test_is_even():
    assert is_even(4)
    assert not is_even(5)
```

Go back to [Contents](#contents).


**Example 8:** Testing for Membership in a List

```python
def test_membership():
    lst = [1, 2, 3, 4]
    assert 3 in lst
    assert 5 not in lst
```

Go back to [Contents](#contents).


**Example 9:** Testing a Function That Capitalizes a Word

```python
def capitalize(word):
    return word.capitalize()

def test_capitalize():
    assert capitalize("python") == "Python"
```

Go back to [Contents](#contents).


**Example 10:** Testing the Length of a String Returned by a Function

```python
def get_greeting(name):
    return f"Hello, {name}"

def test_get_greeting_length():
    assert len(get_greeting("Python")) == 12
```

Go back to [Contents](#contents).



## Python Scripting and Programming

Let's explore the nuances of scripting versus programming and delve into how Python can be used for automating everyday tasks, making life easier and more productive.

Go back to [Contents](#contents).

### Scripting vs Programming

While the terms **Scripting** and **Programming** are often used interchangeably, they do have distinct meanings. 

- Programming is generally considered the process of creating more complex and structured software applications, which often involves writing code that is compiled before it’s run. 
- Scripting, on the other hand, is more about writing small programs, or 'scripts', that are meant to automate simple tasks. 
  - These scripts are usually interpreted rather than compiled.

Python excels in scripting due to its straightforward syntax and powerful built-in libraries. 
- It allows you to write scripts quickly and run them directly, making it an ideal tool for automating routine tasks.

Go back to [Contents](#contents).

### Automating Tasks

Python is an incredibly versatile tool that can automate numerous mundane tasks like file manipulation, data scraping, or even sending emails. 

Its readability and simplicity make it accessible for writing scripts that can save time on a daily basis. 

Let's look at a simple example of a Python script that renames multiple files in a directory:

```python
import os

def rename_files(directory, extension, new_name):
    for count, filename in enumerate(os.listdir(directory)):
        if filename.endswith(extension):
            dst = f"{new_name}_{count}{extension}"
            src = f"{directory}/{filename}"
            dst = f"{directory}/{dst}"
            
            os.rename(src, dst)
    print("Files renamed successfully.")

rename_files('path/to/directory', '.txt', 'new_name')
```

In this script, we define a function `rename_files` that takes a `directory`, a file `extension`, and a `new_name` as parameters. 
- It then renames all files with the specified extension in the given directory. 

Such automation scripts can significantly streamline your workflow.

Go back to [Contents](#contents).

### Some Python Scripting examples

**Problem 1:** Rename Files in a Directory

Rename all .txt files in a directory to include a sequential number.

Solution: 

```python
import os

def rename_files(directory):
    for count, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.txt'):
            os.rename(os.path.join(directory, filename),
                      os.path.join(directory, f"file_{count}.txt"))

rename_files('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 2:** Batch Image Resizing

Resize all images in a directory to a specific size using the PIL library.

Solution: 

```python
from PIL import Image
import os

def resize_images(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size)
            img.save(os.path.join(directory, filename))

resize_images('path/to/images', (100, 100))
```

Go back to [Contents](#contents).

**Problem 3:** Extracting Text from Multiple Files

Read text from multiple .txt files and print their contents.

Solution: 

```python
def read_multiple_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            with open(os.path.join(directory, filename), 'r') as file:
                print(file.read())

read_multiple_files('path/to/text_files')
```

Go back to [Contents](#contents).

**Problem 4:** Create a Daily Backup Script

Create a script to copy a specific file as a daily backup.

Solution: 

```python
import shutil
from datetime import datetime

def daily_backup(file_path, backup_dir):
    backup_file = f"{backup_dir}/{datetime.now().strftime('%Y%m%d')}_backup.txt"
    shutil.copyfile(file_path, backup_file)

daily_backup('path/to/file.txt', 'path/to/backup')
```

Go back to [Contents](#contents).

**Problem 5:** Bulk File Conversion

Convert all .txt files in a directory to .md (Markdown) files.

Solution: 

```python
import os

def convert_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            base = os.path.splitext(filename)[0]
            os.rename(os.path.join(directory, filename),
                      os.path.join(directory, base + '.md'))

convert_files('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 6:** Generating a Report from Logs

Read a log file and generate a report of error counts.

Solution: 

```python
def generate_error_report(log_file):
    with open(log_file, 'r') as file:
        log_content = file.readlines()

    error_count = sum("ERROR" in line for line in log_content)
    print(f"Total Errors: {error_count}")

generate_error_report('path/to/logfile.log')
```

Go back to [Contents](#contents).

**Problem 7:** Deleting Temporary Files

Delete all files with a `.tmp` extension in a directory.

Solution: 

```python
import os

def delete_temp_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.tmp'):
            os.remove(os.path.join(directory, filename))

delete_temp_files('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 8:** Automating Email Sending

Send an email using Python's `smtplib`.

Solution: 

```python
import smtplib

def send_email(subject, message, from_addr, to_addr, smtp_server, port):
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(from_addr, to_addr, f"Subject: {subject}\n{message}")

send_email("Test Subject", "Hello, this is a test.", "sender@example.com", "receiver@example.com", "smtp.example.com", 587)
```

Go back to [Contents](#contents).

**Problem 9:** Monitoring File Changes

Monitor a directory for any changes to files.

Solution: 

```python
import time
import os

def monitor_changes(directory, interval=60):
    initial_snapshot = os.listdir(directory)
    while True:
        time.sleep(interval)
        current_snapshot = os.listdir(directory)
        if current_snapshot != initial_snapshot:
            print("Changes detected in directory.")
            initial_snapshot = current_snapshot

monitor_changes('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 10:** Parsing and Analyzing CSV Data

Read a CSV file and calculate the average of values in a column.

Solution: 

```python
import csv

def calculate_average(csv_file, column):
    total, count = 0, 0
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row[column])
            count += 1
    return total / count if count else 0

print(calculate_average('data.csv', 'price'))
```

Go back to [Contents](#contents).

**Problem 11:** Counting Word Frequency in a Text File

Read a text file and count the frequency of each word.

```python
from collections import Counter

def word_frequency(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    return Counter(words)

print(word_frequency('path/to/textfile.txt'))
```

Go back to [Contents](#contents).

**Problem 12:** Combining Multiple Text Files into One

Combine the content of all `.txt` files in a directory into one file.

```python
import os

def combine_files(directory, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r') as infile:
                    outfile.write(infile.read() + "\n")

combine_files('path/to/directory', 'combined_output.txt')
```

Go back to [Contents](#contents).

**Problem 13:** Renaming Image Files with Date

Rename image files in a directory to include the current date.

```python
import os
from datetime import datetime

def rename_image_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            new_name = datetime.now().strftime('%Y%m%d') + "_" + filename
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

rename_image_files('path/to/images')
```

Go back to [Contents](#contents).

**Problem 14:** Extract Email Addresses from a Text File

Extract and print all email addresses found in a text file.

```python
import re

def extract_emails(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

print(extract_emails('path/to/textfile.txt'))
```

Go back to [Contents](#contents).

**Problem 15:** Convert JSON to CSV

Read a JSON file and convert its content to a CSV file.

```python
import json
import csv

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data[0].keys())  # column headers
        for row in data:
            writer.writerow(row.values())

json_to_csv('data.json', 'output.csv')
```

Go back to [Contents](#contents).

**Problem 16:** Automate Downloading Files from the Web

Download a file from a given URL.

```python
import requests

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

download_file('http://example.com/file.txt', 'downloaded_file.txt')
```

Go back to [Contents](#contents).

**Problem 17:** Batch Resize Images and Change Format

Resize all `.jpg` images in a directory and save them as `.png`.

```python
from PIL import Image
import os

def resize_and_convert_images(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size)
            new_filename = os.path.splitext(filename)[0] + '.png'
            img.save(os.path.join(directory, new_filename))

resize_and_convert_images('path/to/images', (128, 128))
```

Go back to [Contents](#contents).

**Problem 18:** Create a Directory Tree Snapshot

Create a text file that lists all files and directories under a given directory.

```python
import os

def create_directory_tree(directory, output_file):
    with open(output_file, 'w') as file:
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * level
            file.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = ' ' * 4 * (level + 1)
            for f in files:
                file.write(f'{subindent}{f}\n')

create_directory_tree('path/to/directory', 'directory_tree.txt')
```

Go back to [Contents](#contents).

**Problem 19:** Automating System Health Checks

Script to check disk usage and free space.

```python
import shutil

def check_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    print(f"Total: {total / (2**30):.2f} GB")
    print(f"Used: {used / (2**30):.2f} GB")
    print(f"Free: {free / (2**30):.2f} GB")

check_disk_usage('/')
```

Go back to [Contents](#contents).

**Problem 20:** Parsing and Summing Numeric Data from a File

Sum all numbers found in a text file.

```python
import re

def sum_numbers_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    numbers = map(int, re.findall(r'\b\d+\b', content))
    return sum(numbers)

print(sum_numbers_in_file('path/to/numbers.txt'))
```

Go back to [Contents](#contents).

**Problem 21:** Cleaning Up Log Files

Delete log files older than 7 days.

```python
import os
import time

def cleanup_logs(directory, days=7):
    cutoff = time.time() - days * 86400
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff:
            os.remove(file_path)
            print(f"Deleted {filename}")

cleanup_logs('path/to/logs')
```

Go back to [Contents](#contents).

**Problem 22:** Batch File Renaming with Date Stamp

Add a current date stamp to the beginning of each file name.

```python
import os
from datetime import datetime

def add_date_stamp(directory):
    for filename in os.listdir(directory):
        new_name = datetime.now().strftime("%Y%m%d_") + filename
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

add_date_stamp('path/to/files')
```

Go back to [Contents](#contents).

**Problem 23:** Generating a Simple HTML File from Text

Convert a text file into a basic HTML file.

```python
def text_to_html(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write('<html><body>\n')
        for line in infile:
            outfile.write(f"<p>{line.rstrip()}</p>\n")
        outfile.write('</body></html>')

text_to_html('example.txt', 'example.html')
```

Go back to [Contents](#contents).

**Problem 24:** Listing All Python Files in a Directory

Create a list of all Python files (`*.py`) in a directory and its subdirectories.

```python
import os

def list_python_files(directory):
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    return py_files

print(list_python_files('path/to/directory'))
```

Go back to [Contents](#contents).

**Problem 25:** Extracting URLs from a Text File

Find and print all URLs in a text file.

```python
import re

def extract_urls(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    urls = re.findall(r'http[s]?://\S+', content)
    return urls

print(extract_urls('path/to/textfile.txt'))
```

Go back to [Contents](#contents).

**Problem 26:** Checking for Broken Links in a File

Verify if URLs in a text file are reachable (HTTP status 200).

```python
import requests
import re

def check_broken_links(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    urls = re.findall(r'http[s]?://\S+', content)
    for url in urls:
        try:
            response = requests.head(url)
            if response.status_code != 200:
                print(f"Broken link found: {url}")
        except requests.exceptions.RequestException:
            print(f"Error checking URL: {url}")

check_broken_links('path/to/urls.txt')
```

Go back to [Contents](#contents).

**Problem 27:** Counting Lines, Words, and Characters in a Text File

Implement a Python script that mimics the `wc` (word count) command.

```python
def word_count(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        words = [word for line in lines for word in line.split()]
        characters = [char for line in lines for char in line]
    return len(lines), len(words), len(characters)

print(word_count('path/to/file.txt'))
```

Go back to [Contents](#contents).

**Problem 28:** Creating a Directory Only If It Doesn't Exist

Write a script to create a directory but only if it doesn't already exist.

```python
import os

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")
    else:
        print(f"Directory already exists: {directory}")

create_directory_if_not_exists('path/to/new_directory')
```

Go back to [Contents](#contents).

**Problem 29:** Automatically Backing Up a Folder

Create a script to compress and back up an entire folder.

```python
import shutil

def backup_folder(source_folder, backup_folder):
    shutil.make_archive(backup_folder, 'zip', source_folder)
    print(f"Folder {source_folder} backed up as {backup_folder}.zip")

backup_folder('path/to/source_folder', 'path/to/backup_folder')
```

Go back to [Contents](#contents).

**Problem 30:** Merging Multiple CSV Files into One

Combine multiple CSV files into one CSV file.

```python
import pandas as pd
import os

def merge_csv_files(directory, output_file):
    csv_files = [os.path.join(directory, file)
```

Go back to [Contents](#contents).

**Problem 31:** Monitoring CPU and Memory Usage

Script to monitor and print the CPU and memory usage of the system.

```python
import psutil

def system_usage():
    print("CPU Usage:", psutil.cpu_percent(1), "%")
    print("Memory Usage:", psutil.virtual_memory().percent, "%")

system_usage()
```

Go back to [Contents](#contents).

**Problem 32:** Converting PDF to Text

Extract text from a PDF file.

```python
import PyPDF2

def pdf_to_text(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
    return text

print(pdf_to_text('path/to/pdf_file.pdf'))
```

Go back to [Contents](#contents).

**Problem 33:** Sending SMS Alerts

Use Twilio API to send an SMS alert.

```python
from twilio.rest import Client

def send_sms(alert_message, twilio_number, recipient_number):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=alert_message,
        from_=twilio_number,
        to=recipient_number
    )
    print(f"Message sent: {message.sid}")

send_sms("Hello from Python!", '+1234567890', '+0987654321')
```

Go back to [Contents](#contents).

**Problem 34:** Encrypting and Decrypting Text

Encrypt and decrypt a string using the `cryptography` package.

```python
from cryptography.fernet import Fernet

def encrypt_decrypt(text):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    # Encrypt
    encrypted_text = cipher_suite.encrypt(text.encode())
    print("Encrypted:", encrypted_text)

    # Decrypt
    decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
    print("Decrypted:", decrypted_text)

encrypt_decrypt("Hello, Python!")
```

Go back to [Contents](#contents).

**Problem 35:** Scraping Web Data

Scrape data from a webpage using `requests` and BeautifulSoup.

```python
import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.title.text

print(scrape_data('http://example.com'))
```

Go back to [Contents](#contents).

**Problem 36:** Checking Internet Speed

Test and print the internet download and upload speeds.

```python
import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    print(f"Download Speed: {st.results.download / 1024 / 1024:.2f} Mbps")
    print(f"Upload Speed: {st.results.upload / 1024 / 1024:.2f} Mbps")

test_internet_speed()
```

Go back to [Contents](#contents).

**Problem 37:** Automating Browser Actions

Open a website and perform a search using Selenium.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def automate_search(query):
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

automate_search("Python programming")
```

Go back to [Contents](#contents).

**Problem 38:** Creating a Simple HTTP Server

Set up a basic HTTP server using Python.

```python
import http.server
import socketserver

def run_server(port):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()

run_server(8000)
```

Go back to [Contents](#contents).

**Problem 39:** Compressing Files into a ZIP Archive

Compress multiple files into a ZIP archive.

```python
import zipfile

def compress_files(zip_file, files):
    with zipfile.ZipFile(zip_file, 'w') as zipf:
        for file in files:
            zipf.write(file)

compress_files('compressed.zip', ['file1.txt', 'file2.txt'])
```

Go back to [Contents](#contents).

**Problem 40:** Checking for Palindromes

Create a script to check if a word is a palindrome.

```python
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))  # True
print(is_palindrome("python"))  # False
```

Go back to [Contents](#contents).

**Problem 41:** Renaming Image Files Based on EXIF Date

Rename image files in a directory based on their EXIF creation date.

```python
from PIL import Image
import os
from datetime import datetime

def rename_images_by_date(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            exif_data = img._getexif()
            creation_time = datetime.fromtimestamp(os.path.getmtime(img_path))
            if exif_data:
                # Extracting the creation date (tag 36867)
                creation_time = datetime.strptime(exif_data[36867], '%Y:%m:%d %H:%M:%S')
            new_filename = creation_time.strftime('%Y%m%d_%H%M%S') + os.path.splitext(filename)[1]
            os.rename(img_path, os.path.join(directory, new_filename))

rename_images_by_date('path/to/images')
```

Go back to [Contents](#contents).

**Problem 42:** Generating Random Passwords

Create a script to generate a random password.

```python
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

print(generate_password(12))
```

Go back to [Contents](#contents).

**Problem 43:** Checking Disk Space and Alerting

Alert if the disk space is below a certain threshold.

```python
import shutil

def check_disk_space(threshold=20):
    total, used, free = shutil.disk_usage("/")
    percent_free = (free / total) * 100
    if percent_free < threshold:
        print(f"Warning: Low disk space. Only {percent_free:.2f}% remaining.")

check_disk_space()
```

Go back to [Contents](#contents).

**Problem 44:** Converting XML to JSON

Convert an XML file to JSON format.

```python
import xml.etree.ElementTree as ET
import json

def xml_to_json(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    return json.dumps({root.tag: {child.tag: child.text for child in root}})

print(xml_to_json('data.xml'))
```

**Problem 45:** Batch Resizing and Watermarking Images

Resize images in a directory and add a watermark.

```python
from PIL import Image, ImageDraw, ImageFont

def watermark_images(directory, watermark_text, size):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size, Image.ANTIALIAS)

            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            textsize = draw.textsize(watermark_text, font)
            draw.text((size[0] - textsize[0], size[1] - textsize[1]), watermark_text, font=font)

            img.save(os.path.join(directory, filename))

watermark_images('path/to/images', 'Watermark', (800, 600))
```

Go back to [Contents](#contents).

**Problem 46:** Create a To-Do List CLI Application

A command-line to-do list application.

```python
import sys

def todo_list():
    tasks = []
    while True:
        task = input("Enter a task or 'exit': ")
        if task == 'exit':
            break
        tasks.append(task)

    print("\nYour To-Do List:")
    for task in tasks:
        print(f" - {task}")

if __name__ == "__main__":
    todo_list()
```

Go back to [Contents](#contents).

**Problem 47:** Parsing Command Line Arguments

Script to parse and print command line arguments.

```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == "__main__":
    parse_arguments()
```

Go back to [Contents](#contents).

**Problem 48:** Creating a Simple Web Scraper

Scrape and print the headlines from a news website.

```python
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for headline in soup.find_all('h2'):
        print(headline.text.strip())

scrape_headlines('https://news.ycombinator.com/')
```

Go back to [Contents](#contents).

**Problem 49:** Monitoring a Web Page for Changes

Monitor a web page and alert if the content changes.

```python
import requests
import time
import hashlib

def monitor_webpage(url, check_interval=60):
    page_content = requests.get(url).text
    current_hash = hashlib.md5(page_content.encode()).hexdigest()

    while True:
        time.sleep(check_interval)
        new_page_content = requests.get(url).text
        new_hash = hashlib.md5(new_page_content.encode()).hexdigest()

        if new_hash != current_hash:
            print("Webpage has changed!")
            break

monitor_webpage('http://example.com')
```

Go back to [Contents](#contents).

**Problem 50:** Automating Database Backups

Automate the backup of a SQL database.

```python
import os
import subprocess
from datetime import datetime

def backup_database(db_name, backup_path):
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(backup_path, f"{db_name}_{date_str}.sql")
    command = f"mysqldump -u username -p'password' {db_name} > {filename}"
    subprocess.run(command, shell=True)

backup_database('my_database', '/path/to/backup')
```

Go back to [Contents](#contents).

**Problem 51:** Automate File Encryption and Decryption

Encrypt and decrypt files using the cryptography package.

```python
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    encrypted_data = Fernet(key).encrypt(data)
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = Fernet(key).decrypt(encrypted_data)
    with open(encrypted_file_path.replace('.encrypted', ''), 'wb') as file:
        file.write(decrypted_data)

# Generate a key or load from a secure location
key = Fernet.generate_key()
encrypt_file('path/to/file.txt', key)
decrypt_file('path/to/file.txt.encrypted', key)
```

Go back to [Contents](#contents).

**Problem 52:** Batch Image Format Conversion

Convert all images in a directory from PNG to JPEG.

```python
from PIL import Image
import os

def convert_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            img = Image.open(os.path.join(directory, filename))
            new_filename = os.path.splitext(filename)[0] + '.jpg'
            img.convert('RGB').save(os.path.join(directory, new_filename))

convert_images('path/to/images')
```

Go back to [Contents](#contents).

**Problem 53:** Extracting ZIP Archives

Unzip all ZIP files in a given directory.

```python
import zipfile
import os

def extract_zip_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
                zip_ref.extractall(directory)

extract_zip_files('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 54:** Creating a CSV File from User Input

Take user input and write it to a CSV file.

```python
import csv

def write_to_csv(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        while True:
            row = input("Enter data separated by commas (or 'exit' to quit): ")
            if row.lower() == 'exit':
                break
            writer.writerow(row.split(','))

write_to_csv('output.csv')
```

Go back to [Contents](#contents).

**Problem 55:** Checking Website Availability

Monitor the availability of a list of websites.

```python
import requests

def check_websites(websites):
    for website in websites:
        try:
            response = requests.get(website)
            if response.status_code == 200:
                print(f"{website} is up!")
            else:
                print(f"{website} is down. Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"{website} is down. Error: {e}")

check_websites(['http://example.com', 'http://nonexistentwebsite.com'])
```

Go back to [Contents](#contents).

**Problem 56:** Converting Text to Speech

Convert a given text to an audio file using gTTS (Google Text-to-Speech).

```python
from gtts import gTTS

def text_to_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

text_to_speech("Hello, this is a test.", "output.mp3")
```

Go back to [Contents](#contents).

**Problem 57:** Bulk Resizing and Rotating Images

Resize and rotate all images in a directory.

```python
from PIL import Image
import os

def resize_and_rotate_images(directory, size, angle):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            img = Image.open(os.path.join(directory, filename))
            img = img.resize(size)
            img = img.rotate(angle)
            img.save(os.path.join(directory, filename))

resize_and_rotate_images('path/to/images', (300, 300), 90)
```

Go back to [Contents](#contents).

**Problem 58:** Automatically Organizing Downloads Folder

Sort files in the Downloads folder into subfolders based on file types.

```python
import os
import shutil

def organize_downloads(directory):
    file_types = {
        'Documents': ['.pdf', '.docx', '.txt'],
        'Images': ['.jpg', '.jpeg', '.png'],
        'Videos': ['.mp4', '.mov', '.avi']
    }
    for filename in os.listdir(directory):
        for category, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category_path = os.path.join(directory, category)
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                shutil.move(os.path.join(directory, filename), category_path)
                break

organize_downloads('/path/to/downloads')
```

Go back to [Contents](#contents).

**Problem 59:** Validating Email Addresses in a List

Check if email addresses in a list are valid based on a simple pattern.

```python
import re

def validate_emails(emails):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return [email for email in emails if re.match(pattern, email)]

email_list = ["test@example.com", "invalid-email", "hello@world.net"]
print(validate_emails(email_list))
```

Go back to [Contents](#contents).

**Problem 60:** Creating a Simple Event Reminder

Set a reminder for an event and alert when the time is up.

```python
import time
from datetime import datetime, timedelta

def set_reminder(event, event_time):
    print(f"Reminder set for {event} at {event_time}")
    while datetime.now() < event_time:
        time.sleep(10)  # Check every 10 seconds
    print(f"Reminder: {event} is happening now!")

event_date = datetime.now() + timedelta(minutes=1)  # Reminder for 1 minute from now
set_reminder("Meeting with Bob", event_date)
```

Go back to [Contents](#contents).

**Problem 61:** Generating a Report from a Database Query

Execute a database query and write the results to a CSV file.

```python
import sqlite3
import csv

def export_query_results_to_csv(db_file, query, output_csv):
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    cursor.execute(query)

    with open(output_csv, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([i[0] for i in cursor.description])  # column headers
        csv_writer.writerows(cursor)

    cursor.close()
    connection.close()

export_query_results_to_csv('database.db', 'SELECT * FROM table_name', 'output.csv')
```

Go back to [Contents](#contents).

**Problem 62:** Plotting Data from a CSV File

Read data from a CSV file and plot using Matplotlib.

```python
import matplotlib.pyplot as plt
import csv

def plot_csv_data(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = list(reader)

    x = [row[0] for row in data]
    y = [int(row[1]) for row in data]

    plt.plot(x, y)
    plt.show()

plot_csv_data('data.csv')
```

Go back to [Contents](#contents).

**Problem 63:** Monitoring a Directory for New Files

Notify when a new file is added to a directory.

```python
import os
import time

def monitor_new_files(directory):
    known_files = set(os.listdir(directory))
    while True:
        current_files = set(os.listdir(directory))
        new_files = current_files - known_files
        if new_files:
            print(f"New file(s) detected: {new_files}")
            known_files = current_files
        time.sleep(5)  # Check every 5 seconds

monitor_new_files('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 64:** Creating an Interactive Command Line Menu

Build an interactive command line menu for user input.

```python
def show_menu():
    menu = """
    1. Option One
    2. Option Two
    3. Exit
    """
    while True:
        print(menu)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("Option One selected")
        elif choice == "2":
            print("Option Two selected")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

show_menu()
```

Go back to [Contents](#contents).

**Problem 65:** Extracting Specific Data from JSON

Parse a JSON file and extract specific data.

```python
import json

def extract_data_from_json(json_file, key):
    with open(json_file, 'r') as file:
        data = json.load(file)
        return data.get(key, "Key not found")

print(extract_data_from_json('data.json', 'target_key'))
```

Go back to [Contents](#contents).

**Problem 66:** Generating QR Codes

Create a QR code for a given URL or text.

```python
import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)

generate_qr_code('https://www.example.com', 'qrcode.png')
```

Go back to [Contents](#contents).

**Problem 67:** Sending Automated Keyboard Inputs

Automate keyboard inputs for repetitive tasks using PyAutoGUI.

```python
import pyautogui
import time

def automate_keyboard_input(text):
    time.sleep(5)  # Wait 5 seconds to switch to the input window
    pyautogui.typewrite(text)
    pyautogui.press("enter")

automate_keyboard_input("Hello, automated world!")
```

Go back to [Contents](#contents).

**Problem 68:** Creating a Countdown Timer

Make a countdown timer that prints the time remaining.

```python
import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown_timer(60)
```

Go back to [Contents](#contents).

**Problem 69:** Scraping and Saving Images from a Web Page

Download all images from a given webpage.

```python
import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')
    
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    for i, img in enumerate(images, start=1):
        img_url = img.get('src')
        img_data = requests.get(img_url).content
        with open(os.path.join(folder, f'image_{i}.jpg'), 'wb') as file:
            file.write(img_data)

download_images('http://example.com', 'downloaded_images')
```

Go back to [Contents](#contents).

**Problem 70:** Parsing Command Line Arguments and Executing Functions

Script that parses command line arguments to execute specific functions.

```python
import argparse

def greet(name):
    print(f"Hello, {name}!")

def farewell(name):
    print(f"Goodbye, {name}!")

def main():
    parser = argparse.ArgumentParser(description="Greet or bid farewell.")
    parser.add_argument('name', type=str, help="Name of the person.")
    parser.add_argument('--farewell', action='store_true', help="Bid farewell instead of greeting.")

    args = parser.parse_args()
    if args.farewell:
        farewell(args.name)
    else:
        greet(args.name)

if __name__ == "__main__":
    main()
```

Go back to [Contents](#contents).

**Problem 71:** Batch Renaming Files with Regular Expressions

Rename files in a directory based on a regular expression pattern.

```python
import os
import re

def rename_files_regex(directory, pattern, replacement):
    for filename in os.listdir(directory):
        new_name = re.sub(pattern, replacement, filename)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

rename_files_regex('path/to/files', r'\s+', '_')
```

Go back to [Contents](#contents).

**Problem 72:** Finding Prime Numbers in a Range

Generate a list of prime numbers within a specified range.

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

print(find_primes(10, 50))
```

Go back to [Contents](#contents).

**Problem 73:** Automated Data Backup to a ZIP File

Compress and back up a directory to a ZIP file with a timestamp.

```python
import zipfile
import os
from datetime import datetime

def backup_to_zip(directory):
    zip_filename = os.path.basename(directory) + '_' + datetime.now().strftime('%Y%m%d%H%M%S') + '.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file))
    print(f"Backup created: {zip_filename}")

backup_to_zip('path/to/directory')
```

Go back to [Contents](#contents).

**Problem 74:** Checking for Active Internet Connection

Verify if the system is connected to the internet.

```python
import socket

def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.create_connection((host, port), timeout=timeout)
        return True
    except socket.error:
        return False

print("Connected" if check_internet_connection() else "No Internet Connection")
```

Go back to [Contents](#contents).

**Problem 75:** Converting CSV Data to a Dictionary

Read a CSV file and convert it into a list of dictionaries.

```python
import csv

def csv_to_dict(csv_file):
    with open(csv_file, mode='r') as infile:
        reader = csv.DictReader(infile)
        return list(reader)

data = csv_to_dict('data.csv')
print(data)
```

Go back to [Contents](#contents).

**Problem 76:** Parsing and Processing JSON from a URL

Fetch and process JSON data from a web URL.

```python
import requests

def fetch_process_json(url):
    response = requests.get(url)
    data = response.json()
    # Process data
    return data

json_data = fetch_process_json('https://api.example.com/data')
print(json_data)
```

Go back to [Contents](#contents).

**Problem 77:** Automating File Compression for Upload

Compress a file for easier upload.

```python
import gzip
import shutil

def compress_file_for_upload(file_path):
    with open(file_path, 'rb') as f_in:
        with gzip.open(file_path + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Compressed file created: {file_path}.gz")

compress_file_for_upload('path/to/large_file.txt')
```

Go back to [Contents](#contents).

**Problem 78:** Creating a Markdown Table from CSV Data

Convert CSV data into a Markdown table format.

```python
import csv

def csv_to_markdown_table(csv_file):
    table = ""
    with open(csv_file, mode='r') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        table = "| " + " | ".join(headers) + " |\n"
        table += "| " + " | ".join(['---']*len(headers)) + " |\n"
        for row in reader:
            table += "| " + " | ".join(row) + " |\n"
    return table

markdown_table = csv_to_markdown_table('data.csv')
print(markdown_table)
```

Go back to [Contents](#contents).

**Problem 79:** Automating HTML Template Generation

Generate an HTML file from a template with placeholders.

```python
def generate_html(template, data, output_file):
    with open(template, 'r') as file:
        html_content = file.read()

    for key, value in data.items():
        html_content = html_content.replace(f"{{{{ {key} }}}}", value)

    with open(output_file, 'w') as file:
        file.write(html_content)

data = {'title': 'My Page', 'header': 'Welcome to My Page', 'body': 'This is content.'}
generate_html('template.html', data, 'output.html')
```

Go back to [Contents](#contents).

**Problem 80:** Creating a Network Packet Sniffer

Build a simple packet sniffer to capture network traffic.

```python
import socket
import struct

def sniff_packets():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = s.recvfrom(65536)
        dest_mac, src_mac, eth_proto, data = struct.unpack('! 6s 6s H', raw_data[:14])
        print(f"Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}")

sniff_packets()
```

Go back to [Contents](#contents).

**Problem 81:** Tracking Cryptocurrency Prices

Fetch and display the current price of a cryptocurrency.

```python
import requests

def get_crypto_price(crypto_symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[crypto_symbol]['usd']

print("Bitcoin Price: $", get_crypto_price('bitcoin'))
```

Go back to [Contents](#contents).

**Problem 82:** Validating IP Addresses

Check if a list of IP addresses are valid.

```python
import re

def validate_ip(ip):
    pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
    return bool(re.match(pattern, ip))

ips = ["192.168.0.1", "256.256.256.256"]
for ip in ips:
    print(f"{ip}: {'Valid' if validate_ip(ip) else 'Invalid'}")
```

Go back to [Contents](#contents).

**Problem 83:** Calculating Fibonacci Sequence Using Recursion

Calculate Fibonacci sequence up to N using recursion.

```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
print([fibonacci(i) for i in range(n_terms)])
```

Go back to [Contents](#contents).

**Problem 84:** Bulk Downloading Images from URLs

Download images from a list of URLs.

```python
import requests
import os

def download_images(image_urls, download_folder):
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    for i, url in enumerate(image_urls, start=1):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(download_folder, f'image_{i}.jpg'), 'wb') as file:
                file.write(response.content)

image_urls = ["http://example.com/image1.jpg", "http://example.com/image2.jpg"]
download_images(image_urls, 'downloaded_images')
```

Go back to [Contents](#contents).

**Problem 85:** Sending Desktop Notifications

Send a desktop notification.

```python
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # seconds
    )

send_notification("Reminder", "Take a break!")
```

Go back to [Contents](#contents).

**Problem 86:** Creating a Simple Web Crawler

Crawl a website and print all internal links found.

```python
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def crawl_website(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('/'):
            print(urljoin(base_url, href))

crawl_website('http://example.com')
```

Go back to [Contents](#contents).

**Problem 87:** Generating a Word Cloud from Text

Create a word cloud image from a given text.

```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

text = "Python is a great programming language for data analysis, web development, scripting."
generate_word_cloud(text)
```

Go back to [Contents](#contents).

**Problem 88:** Automating WhatsApp Messages

Send a WhatsApp message at a scheduled time.

```python
import pywhatkit

def send_whatsapp_message(number, message, time_hour, time_minute):
    pywhatkit.sendwhatmsg(number, message, time_hour, time_minute)

send_whatsapp_message('+1234567890', 'Hello, this is an automated message.', 22, 30)
```

Go back to [Contents](#contents).

**Problem 89:** Generating Random Usernames

Create random usernames using a combination of words.

```python
import random

def generate_username(words, length):
    return ''.join(random.choice(words) for _ in range(length))

words = ["cool", "python", "coder", "dev", "program"]
print(generate_username(words, 3))
```

Go back to [Contents](#contents).

**Problem 90:** Converting Speech to Text

Convert spoken words into text using SpeechRecognition.

```python
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, my speech service is down.")

speech_to_text()
```

Go back to [Contents](#contents).

**Problem 91:** Batch Resizing Images to a Fixed Width While Maintaining Aspect Ratio

Resize all images in a directory to a specified width while maintaining aspect ratio.

```python
from PIL import Image
import os

def resize_images_to_width(directory, width):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            w_percent = (width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            img = img.resize((width, h_size), Image.ANTIALIAS)
            img.save(img_path)

resize_images_to_width('path/to/images', 300)
```

Go back to [Contents](#contents).

**Problem 92:** Extracting ZIP Files to a Target Directory

Unzip files in a directory to a specified target directory.

```python
import zipfile
import os

def extract_zip_to_folder(zip_folder, target_folder):
    for filename in os.listdir(zip_folder):
        if filename.endswith('.zip'):
            zip_path = os.path.join(zip_folder, filename)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(target_folder)

extract_zip_to_folder('path/to/zip_files', 'path/to/extracted_files')
```

Go back to [Contents](#contents).

**Problem 93:** Merging PDF Files into One

Combine multiple PDF files in a directory into a single PDF file.

```python
import PyPDF2
import os

def merge_pdfs(directory, output_file):
    merger = PyPDF2.PdfFileMerger()
    for item in os.listdir(directory):
        if item.endswith('.pdf'):
            merger.append(os.path.join(directory, item))
    merger.write(output_file)
    merger.close()

merge_pdfs('path/to/pdf_files', 'merged_output.pdf')
```

Go back to [Contents](#contents).

**Problem 94:** Creating a Countdown Clock in the Terminal

Display a countdown clock in the console for a specified duration.

```python
import time

def countdown_clock(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

countdown_clock(120)  # 120 seconds countdown
```

Go back to [Contents](#contents).

**Problem 95:** Removing Duplicate Lines from a Text File

Read a text file, remove duplicate lines, and save the result.

```python
def remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    unique_lines = set(lines)
    with open(file_path, 'w') as file:
        file.writelines(unique_lines)

remove_duplicates('path/to/textfile.txt')
```

Go back to [Contents](#contents).

**Problem 96:** Creating a Simple Local Server with HTTPServer

Start a basic local HTTP server for serving static files.

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

def start_server(port):
    httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f"Serving HTTP on port {port}...")
    httpd.serve_forever()

start_server(8000)
```

Go back to [Contents](#contents).

**Problem 97:** Listing Files with a Specific Extension in a Directory

Print a list of all files with a certain extension in a directory.

```python
import os

def list_files_with_extension(directory, extension):
    return [file for file in os.listdir(directory) if file.endswith(extension)]

print(list_files_with_extension('path/to/directory', '.txt'))
```

Go back to [Contents](#contents).

**Problem 98:** Encrypting and Decrypting a Text File

Encrypt the contents of a text file and then decrypt it.

```python
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = Fernet(key).encrypt(original)
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = Fernet(key).decrypt(encrypted)
    with open(file_path, 'wb') as file:
        file.write(decrypted)

key = Fernet.generate_key()
encrypt_file('path/to/file.txt', key)
decrypt_file('path/to/file.txt', key)
```

Go back to [Contents](#contents).

**Problem 99:** Automatically Shutting Down the Computer

Schedule a shutdown of the computer after a certain period.

```python
import os
import time

def schedule_shutdown(seconds):
    time.sleep(seconds)
    os.system("shutdown /s /t 1")

schedule_shutdown(3600)  # Shuts down after 1 hour
```

Go back to [Contents](#contents).

**Problem 100:** Parsing HTML and Extracting Data

Extract specific data from an HTML file.

```python
from bs4 import BeautifulSoup

def extract_data_from_html(html_file, tag, class_name):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return [element.get_text() for element in soup.find_all(tag, class_=class_name)]

print(extract_data_from_html('example.html', 'p', 'content'))
```

Go back to [Contents](#contents).



## Python Libraries

A Python library is a collection of modules and packages that offer pre-written code to help with common programming tasks. 

These libraries can include anything from mathematical operations to data visualization, web development, machine learning, and much more.

Why are these libraries so crucial? 
- The primary reason is efficiency. 
- Libraries save time and effort as you don't have to write every single line of code from scratch. 
- They are tried and tested, meaning they reduce the likelihood of errors in your code. 
- Moreover, they can significantly boost productivity by simplifying complex tasks into more manageable ones.

Find, install and publish Python packages with the Python Package Index: https://pypi.org/

Next, let's touch upon some of the most popular Python libraries.

Go back to [Contents](#contents).



### The Python Standard Library

In Python, the standard library provides a wide range of modules that support various aspects of programming, from data manipulation to web development. 

Some of the most commonly used built-in libraries include:

1. **sys:** Provides access to some variables used or maintained by the Python interpreter and functions that interact strongly with the interpreter. Useful for manipulating Python runtime environment.

2. **os:** Offers a way of using operating system-dependent functionality like reading or writing to a file system, managing paths, and executing shell commands.

3. **datetime:** Supplies classes for manipulating dates and times in both simple and complex ways. It's widely used in applications that need to handle date and time information.

4. **math:** Provides access to the mathematical functions defined by the C standard. These include functions for complex mathematical operations like trigonometry, logarithms, and more.

5. **random:** This module implements pseudo-random number generators for various distributions. It's used for anything that requires randomness, from simulations to games.

6. **collections:** Offers alternative container datatypes, such as Counter, OrderedDict, defaultdict, and namedtuple, which are designed for high-performance container operations.

7. **json:** Used for parsing JSON data and converting Python data to JSON. It's extremely useful for web development and working with APIs that communicate using JSON.

8. **re:** Provides regular expression matching operations similar to those found in Perl. It's used for string searching and manipulation.

9. **subprocess:** Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It's crucial for running external commands.

10. **threading:** Enables concurrent programming. It's used to run code in parallel, making it possible to perform tasks that require waiting (like I/O operations) more efficiently.

11. **urllib:** A package that collects several modules for working with URLs, such as urllib.request for opening and reading URLs or urllib.parse for parsing URLs.

12. **socket:** Provides access to the BSD socket interface. It's used for network programming, such as creating client-server applications.

13. **sqlite3:** Implements a SQL interface compliant with the DB-API 2.0 specification described by PEP 249. It's used for applications that require a lightweight disk-based database without the need for a separate server process.

14. **logging:** Offers a flexible logging system for applications to report status, error, and informational messages.

Go back to [Contents](#contents).



#### sys

The `sys` module in Python provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. 

Here are 10 examples of how the `sys` module can be used in Python scripts:

Go back to [Contents](#contents).



**Problem 1:** Accessing command-line arguments:

Solution: 

```python
import sys
# Access command-line arguments
args = sys.argv[1:]
print(args)
```

Go back to [Contents](#contents).



**Problem 2:** Exiting the script with a specific status:

Solution: 

```python
import sys
# Exit the script with status 1
sys.exit(1)
```

Go back to [Contents](#contents).



**Problem 3:** Getting the Python version information:

Solution: 

```python
import sys
# Print Python version information
print(sys.version)
```

Go back to [Contents](#contents).



**Problem 4:** Finding the path of the Python interpreter:

Solution: 

```python
import sys
# Print the path of the Python interpreter binary
print(sys.executable)
```

Go back to [Contents](#contents).



**Problem 5:** Modifying the Python module search path:

Solution: 

```python
import sys
# Add a directory to the module search path
sys.path.append('/path/to/module/directory')
```

Go back to [Contents](#contents).



**Problem 6:** Redirecting output stream:

Solution: 

```python
import sys
# Redirect standard output to a file
with open('output.txt', 'w') as f:
    sys.stdout = f
    print('This will be written to output.txt')
```

Go back to [Contents](#contents).



**Problem 7:** Checking the size of an object (useful for memory management):

Solution: 

```python
import sys
# Check the size of an object in bytes
my_list = [1, 2, 3]
print(sys.getsizeof(my_list))
```

Go back to [Contents](#contents).



**Problem 8:** Listing loaded modules:

Solution: 

```python
import sys
# List all loaded modules
print(sys.modules)
```

Go back to [Contents](#contents).



**Problem 9:** Reading from standard input:

Solution: 

```python
import sys
# Read a line from standard input
line = sys.stdin.readline()
print(f'You entered: {line}')
```

Go back to [Contents](#contents).



**Problem 10:** Checking the platform:

Solution: 

```python
import sys
# Check the platform
if sys.platform == 'win32':
    print('Running on Windows')
elif sys.platform == 'linux':
    print('Running on Linux')
else:
    print(f'Running on {sys.platform}')
```

Go back to [Contents](#contents).



#### os

The `os` module in Python provides a way of using operating system-dependent functionality. 

It includes functions for interacting with the file system, managing processes, and reading or setting the environment. 

Here are 10 examples demonstrating different uses of the os module:

Go back to [Contents](#contents).



**Problem 1:** Getting the current working directory:

Solution: 

```python
import os
cwd = os.getcwd()
print(f'Current working directory: {cwd}')
```

Go back to [Contents](#contents).



**Problem 2:** Changing the current working directory:

Solution: 

```python
import os
os.chdir('/path/to/new/directory')
print(f'Changed to new directory: {os.getcwd()}')
```

Go back to [Contents](#contents).



**Problem 3:** Listing files and directories in a specified path:

Solution: 

```python
import os
entries = os.listdir('/path/to/directory')
for entry in entries:
    print(entry)
```

Go back to [Contents](#contents).



**Problem 4:** Creating a new directory:

Solution: 

```python
import os
os.mkdir('/path/to/new/directory')
```

Go back to [Contents](#contents).



**Problem 5:** Removing a directory:

Solution: 

```python
import os
os.rmdir('/path/to/directory')
```

Go back to [Contents](#contents).



**Problem 6:** Renaming a file or directory:

Solution: 

```python
import os
os.rename('/path/to/old_name', '/path/to/new_name')
```

Go back to [Contents](#contents).



**Problem 7:** Getting environment variables:

Solution: 

```python
import os
home_dir = os.environ.get('HOME')
print(f'Home directory: {home_dir}')
```

Go back to [Contents](#contents).



**Problem 8:** Setting environment variables:

Solution: 

```python
import os
os.environ['MY_VARIABLE'] = 'value'
print(f'My variable: {os.environ.get("MY_VARIABLE")}')
```

Go back to [Contents](#contents).



**Problem 9:** Executing a shell command:

Solution: 

```python
import os
os.system('echo Hello World')
```

Go back to [Contents](#contents).



**Problem 10:** Walking a directory tree

Solution: 

```python
import os
for root, dirs, files in os.walk('/path/to/directory'):
    print(f'Found directory: {root}')
    for file_name in files:
        print(f'\t{file_name}')
```

Go back to [Contents](#contents).



#### time

The `time` module in Python provides various time-related functions. 

Here are 10 examples demonstrating different uses of the time module, from basic time manipulation to more advanced timing and sleep functionalities.

Go back to [Contents](#contents).



**Problem 1:** Getting the Current Time

Solution: 

```python
import time

current_time = time.time()
print(f"Current time since the Epoch: {current_time} seconds")
```

Go back to [Contents](#contents).



**Problem 2:** Converting a Time Tuple to a Timestamp

Solution: 

```python
import time

time_tuple = (2023, 2, 1, 12, 0, 0, 0, 0, 0)  # Year, Month, Day, Hour, Minute, Second, Day of Week, Day of Year, DST
timestamp = time.mktime(time_tuple)
print(f"Timestamp: {timestamp}")
```

Go back to [Contents](#contents).



**Problem 3:** Displaying Readable Time Format (ctime)

Solution: 

```python
import time

readable_time = time.ctime(time.time())
print(f"Readable time: {readable_time}")
```

Go back to [Contents](#contents).



**Problem 4:** Getting Structured Time (localtime and gmtime)

Solution: 

```python
import time

local_time = time.localtime(time.time())
print(f"Local time: {local_time}")

gm_time = time.gmtime(time.time())
print(f"UTC time: {gm_time}")
```

Go back to [Contents](#contents).



**Problem 5:** Formatting Time with strftime

Solution: 

```python
import time

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(f"Formatted time: {formatted_time}")
```

Go back to [Contents](#contents).



**Problem 6:** Parsing a String to Time with strptime

Solution: 

```python
import time

time_string = "2023-02-01 12:00:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed time: {parsed_time}")
```

Go back to [Contents](#contents).



**Problem 7:** Sleeping for a Specific Interval

Solution: 

```python
import time

print("Start of interval")
time.sleep(5)  # Sleep for 5 seconds
print("End of interval")
```

Go back to [Contents](#contents).



**Problem 8:** Measuring Performance Time

Solution: 

```python
import time

start_time = time.perf_counter()
# Some task to measure
time.sleep(2)
end_time = time.perf_counter()
print(f"Time taken: {end_time - start_time} seconds")
```

Go back to [Contents](#contents).



**Problem 9:** Using a Monotonic Clock

Solution: 

```python
import time

start = time.monotonic()
time.sleep(1)
end = time.monotonic()
print(f"Elapsed time: {end - start} seconds")
```

Go back to [Contents](#contents).



**Problem 10:** Handling Time Zones with time

While `time` has limited support for time zones, you can manually calculate time zone offsets or use the `datetime` module for more complex time zone handling. 

Here's a basic example using time:

Solution: 

```python
import time

utc_offset = -5  # Assuming EST (UTC-5)
local_time = time.time() + (utc_offset * 3600)
print(f"Local time (EST): {time.ctime(local_time)}")
```

Go back to [Contents](#contents).



#### datetime

The `datetime` module in Python provides classes for manipulating dates and times in both simple and complex ways. 

Here are 10 examples to showcase different functionalities of the `datetime` module:

Go back to [Contents](#contents).



**Problem 1:** Getting the current date and time:

Solution: 

```python
from datetime import datetime
now = datetime.now()
print(f'Current date and time: {now}')
```

Go back to [Contents](#contents).



**Problem 2:** Creating a specific datetime object:

Solution: 

```python
from datetime import datetime
dt = datetime(2023, 1, 1, 12, 0)
print(f'Specific datetime: {dt}')
```

Go back to [Contents](#contents).



**Problem 3:** Formatting a datetime object as a string

Solution: 

```python
from datetime import datetime
now = datetime.now()
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(f'Formatted datetime: {formatted}')
```

Go back to [Contents](#contents).



**Problem 4:** Parsing a string to a datetime object:

Solution: 

```python
from datetime import datetime
dt_str = '2023-01-01 12:00:00'
dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
print(f'Parsed datetime: {dt}')
```

Go back to [Contents](#contents).



**Problem 5:** Getting the current date:

Solution: 

```python
from datetime import date
today = date.today()
print(f'Today\'s date: {today}')
```

Go back to [Contents](#contents).



**Problem 6:** Calculating the difference between two dates or times:

Solution: 

```python
from datetime import datetime
dt1 = datetime(2023, 1, 1)
dt2 = datetime(2023, 6, 1)
delta = dt2 - dt1
print(f'Difference: {delta.days} days')
```

Go back to [Contents](#contents).



**Problem 7:** Adding or subtracting days from a date:

Solution: 

```python
from datetime import datetime, timedelta
now = datetime.now()
future_date = now + timedelta(days=10)
past_date = now - timedelta(days=10)
print(f'Future date: {future_date}')
print(f'Past date: {past_date}')
```

Go back to [Contents](#contents).



**Problem 8:** Replacing a specific part of a datetime object (e.g., year):

Solution: 

```python
from datetime import datetime
dt = datetime(2023, 1, 1)
dt_replaced = dt.replace(year=2024)
print(f'Datetime with replaced year: {dt_replaced}')
```

Go back to [Contents](#contents).



**Problem 9:** Getting the weekday of a date:

Solution: 

```python
from datetime import datetime
dt = datetime.now()
weekday = dt.weekday()  # Monday is 0 and Sunday is 6
print(f'Weekday: {weekday}')
```

Go back to [Contents](#contents).



**Problem 10:** Working with time zones

Solution: 

```python
from datetime import datetime
from pytz import timezone
dt_utc = datetime.now(timezone('UTC'))
dt_local = dt_utc.astimezone(timezone('America/New_York'))
print(f'UTC time: {dt_utc}')
print(f'Local time (NY): {dt_local}')
```

Go back to [Contents](#contents).


#### math

The `math` module in Python provides access to mathematical functions defined by the C standard. 

These functions include trigonometric functions, representation functions, logarithmic functions, and more. 

Here are 10 examples demonstrating different uses of the math module:

Go back to [Contents](#contents).



**Problem 1:** Calculating the square root:

Solution: 

```python
import math
print(math.sqrt(16))  # Output: 4.0
```

Go back to [Contents](#contents).



**Problem 2:** Rounding up with ceil:

Solution: 

```python
import math
print(math.ceil(3.4))  # Output: 4
```

Go back to [Contents](#contents).



**Problem 3:** Rounding down with floor:

Solution: 

```python
import math
print(math.floor(3.7))  # Output: 3
```

Go back to [Contents](#contents).



**Problem 4:** Calculating the factorial of a number:

Solution: 

```python
import math
print(math.factorial(5))  # Output: 120
```

Go back to [Contents](#contents).



**Problem 5:** Calculating the power of e (Euler's number):

Solution: 

```python
import math
print(math.exp(1))  # Output: 2.718281828459045
```

Go back to [Contents](#contents).



**Problem 6:** Calculating logarithms (default base e, can also specify base):

Solution: 

```python
import math
print(math.log(10))  # Natural logarithm, base e
print(math.log(100, 10))  # Logarithm base 10
```

Go back to [Contents](#contents).



**Problem 7:** Calculating trigonometric functions:

Solution: 

```python
import math
# All trigonometric functions expect input in radians, not degrees
angle = math.radians(45)  # Convert 45 degrees to radians
print(math.sin(angle))  # Output: 0.7071067811865475 (sin of 45 degrees)
print(math.cos(angle))  # Output: 0.7071067811865476 (cos of 45 degrees)
```

Go back to [Contents](#contents).



**Problem 8:** Converting radians to degrees and vice versa:

Solution: 

```python
import math
radians = math.radians(180)  # Convert degrees to radians
degrees = math.degrees(math.pi)  # Convert radians to degrees
print(f"Radians: {radians}, Degrees: {degrees}")
```

Go back to [Contents](#contents).



**Problem 9:** Calculating the greatest common divisor (GCD):

Solution: 

```python
import math
print(math.gcd(48, 180))  # Output: 12
```

Go back to [Contents](#contents).



**Problem 10:** Calculating the hypotenuse of a right-angled triangle:

Solution: 

```python
import math
print(math.hypot(3, 4))  # Output: 5.0
```

Go back to [Contents](#contents).



#### random

The `random` module in Python is used to generate pseudo-random numbers for various distributions. 

Here are 10 examples demonstrating its use for different purposes:

Go back to [Contents](#contents).



**Problem 1:** Generating a random float between 0.0 and 1.0:

Solution: 

```python
import random
print(random.random())
```

Go back to [Contents](#contents).



**Problem 2:** Generating a random integer within a specified range:

Solution: 

```python
import random
print(random.randint(1, 100))  # Includes both end points
```

Go back to [Contents](#contents).



**Problem 3:** Picking a random element from a list

Solution: 

```python
import random
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))
```

Go back to [Contents](#contents).



**Problem 4:** Shuffling a list in place:

Solution: 

```python
import random
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)
```

Go back to [Contents](#contents).



**Problem 5:** Generating a random sample from a list without replacement:

Solution: 

```python
import random
population = ['red', 'blue', 'green', 'yellow', 'black']
print(random.sample(population, 3))
```

Go back to [Contents](#contents).



**Problem 6:** Generating a random floating-point number within a specified range

Solution: 

```python
import random
print(random.uniform(1, 10))  # Float between 1 and 10
```

Go back to [Contents](#contents).



**Problem 7:** Generating a random integer with a step size (similar to range() function):

Solution: 

```python
import random
print(random.randrange(0, 101, 5))  # Random number between 0 and 100, inclusive, counting by 5s
```

Go back to [Contents](#contents).



**Problem 8:** Generating a random boolean value:

Solution: 

```python
import random
print(random.choice([True, False]))
```

Go back to [Contents](#contents).



**Problem 9:** Seeding the random number generator to produce repeatable results:

Solution: 

```python
import random
random.seed(123)
print(random.random())  # This will always print the same number every time the program is run
```

Go back to [Contents](#contents).



**Problem 10:** Generating a random byte string of specified length

Solution: 

```python
import random
print(random.randbytes(5))  # Generates a random byte string of length 5
```

Go back to [Contents](#contents).



#### collections

The `collections` module in Python provides specialized container datatypes, offering alternatives to Python’s general purpose built-in containers: `dict`, `list`, `set`, and `tuple`. 

Here are 10 examples demonstrating different uses of the `collections` module:

Go back to [Contents](#contents).



**Problem 1:** `Counter` for counting hashable objects:

Solution: 

```python
from collections import Counter
colors = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
color_count = Counter(colors)
print(color_count)
```

Go back to [Contents](#contents).



**Problem 2:** `defaultdict` for dictionaries with a default value for missing keys:

Solution: 

```python
from collections import defaultdict
fruit = defaultdict(int)
fruit['apple'] += 1
print(fruit['apple'])  # Outputs 1
print(fruit['banana'])  # Outputs 0, default int value
```

Go back to [Contents](#contents).



**Problem 3:** `OrderedDict` for dictionaries that maintain insertion order:

Solution: 

```python
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['banana'] = 3
ordered_dict['apple'] = 4
ordered_dict['pear'] = 1
print(ordered_dict)
```

Go back to [Contents](#contents).



**Problem 4:** `namedtuple` for creating tuple subclasses with named fields:

Solution: 

```python
from collections import namedtuple
Point = namedtuple('Point', 'x y')
pt = Point(1, -4)
print(pt.x, pt.y)
```

Go back to [Contents](#contents).



**Problem 5:** `deque` for double-ended queue allowing appends and pops from either side efficiently:

Solution: 

```python
from collections import deque
dq = deque(['a', 'b', 'c'])
dq.append('d')  # add to the right
dq.appendleft('e')  # add to the left
print(dq)
```

Go back to [Contents](#contents).



**Problem 6:** `ChainMap` for creating a single view of multiple mappings:

Solution: 

```python
from collections import ChainMap
dict1 = {'apple': 1, 'banana': 2}
dict2 = {'orange': 3, 'banana': 4}
combined = ChainMap(dict1, dict2)
print(combined['banana'])  # Outputs 2 (from dict1)
```

Go back to [Contents](#contents).



**Problem 7:** `UserDict`, `UserList`, and `UserString` for easier creation of your own container types:

Solution: 

```python
from collections import UserDict
class MyDict(UserDict):
    pass
my_dict = MyDict()
my_dict['fruit'] = 'apple'
print(my_dict)
```

Go back to [Contents](#contents).



**Problem 8:** Updating a `Counter` object with another collection of items:

Solution: 

```python
from collections import Counter
c = Counter(cats=4, dogs=8)
c.update(['cats', 'parrots', 'dogs'])
print(c)
```

Go back to [Contents](#contents).



**Problem 9:** Subtracting elements from a `Counter` object:

Solution: 

```python
from collections import Counter
inventory = Counter(apples=30, oranges=12, bananas=15)
sold = Counter(apples=5, oranges=7)
inventory.subtract(sold)
print(inventory)
```

Go back to [Contents](#contents).



**Problem 10:** Rotating elements in a `deque`:

HERE

Solution: 

```python
from collections import deque
dq = deque(range(5))
dq.rotate(2)  # Rotate two steps to the right
print(dq)  # deque([3, 4, 0, 1, 2])
dq.rotate(-2)  # Rotate two steps to the left
print(dq)  # deque([0, 1, 2, 3, 4])
```

Go back to [Contents](#contents).



#### json

The `json` module in Python is used for parsing JSON data (to convert JSON data into Python data structures) and for encoding Python objects into JSON format. 

Here are 10 examples that demonstrate various uses of the `json` module:

Go back to [Contents](#contents).



**Problem 1:** Loading JSON from a string:

Solution: 

```python
import json
data = '{"name": "John", "age": 30, "city": "New York"}'
python_obj = json.loads(data)
print(python_obj)
```

Go back to [Contents](#contents).



**Problem 2:** Dumping Python object to a JSON string:

Solution: 

```python
import json
python_obj = {'name': 'John', 'age': 30, 'city': 'New York'}
json_data = json.dumps(python_obj)
print(json_data)
```

Go back to [Contents](#contents).



**Problem 3:** Pretty printing JSON data:

Solution: 

```python
import json
python_obj = {'name': 'John', 'age': 30, 'city': 'New York', 'hasPets': False, 'titles': ['Engineer', 'Programmer']}
json_data = json.dumps(python_obj, indent=4, sort_keys=True)
print(json_data)
```

Go back to [Contents](#contents).



**Problem 4:** Writing JSON data to a file:

Solution: 

```python
import json
python_obj = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as json_file:
    json.dump(python_obj, json_file)
```

Go back to [Contents](#contents).



**Problem 5:** Reading JSON data from a file:

Solution: 

```python
import json
with open('data.json', 'r') as json_file:
    python_obj = json.load(json_file)
    print(python_obj)
```

Go back to [Contents](#contents).



**Problem 6:** Handling complex objects using json.dumps:

Solution: 

```python
import json
from datetime import datetime
def complex_encoder(obj):
    if isinstance(obj, datetime):
        return obj.__str__()
python_obj = {'name': 'John', 'joined': datetime.now()}
json_data = json.dumps(python_obj, default=complex_encoder)
print(json_data)
```

Go back to [Contents](#contents).



**Problem 7:** Decoding custom JSON object:

Solution: 

```python
import json
def custom_decoder(python_obj):
    if 'datetime' in python_obj:
        return datetime.strptime(python_obj['datetime'], '%Y-%m-%d %H:%M:%S')
    return python_obj
json_data = '{"name": "John", "datetime": "2023-01-01 12:00:00"}'
python_obj = json.loads(json_data, object_hook=custom_decoder)
print(python_obj)
```

Go back to [Contents](#contents).



**Problem 8:** Encoding and decoding a list of data:

Solution: 

```python
import json
python_obj = [{'name': 'John'}, {'name': 'Alice'}, {'name': 'Bob'}]
json_data = json.dumps(python_obj)
new_python_obj = json.loads(json_data)
print(new_python_obj)
```

Go back to [Contents](#contents).



**Problem 9:** Using `json.dumps()` with `separators` and `sort_keys` parameters:

Solution: 

```python
import json
python_obj = {'name': 'John', 'age': 30, 'city': 'New York', 'hasPets': False}
json_data = json.dumps(python_obj, indent=4, separators=(',', ': '), sort_keys=True)
print(json_data)
```

Go back to [Contents](#contents).



**Problem 10:** Filtering keys while encoding Python objects to JSON:

Solution: 

```python
import json
python_obj = {'name': 'John', 'password': '1234', 'age': 30}
def filter_keys(obj):
    return {key: value for key, value in obj.items() if key != 'password'}
json_data = json.dumps(python_obj, default=filter_keys)
print(json_data)
```

Go back to [Contents](#contents).



#### re

The `re` module in Python is used for working with regular expressions. 

It provides a powerful way to search, match, and manipulate text. 

Here are 10 examples demonstrating different uses of the `re` module, from basic pattern matching to more complex text manipulations.

Go back to [Contents](#contents).



**Problem 1:** Matching a Pattern in a String

Checks if the pattern is present in the string.

Solution: 

```python
import re

text = "Hello, world!"
if re.search("world", text):
    print("Found a match!")
```

Go back to [Contents](#contents).



**Problem 2:** Splitting a String

Splits a string by any number of spaces.

Solution: 

```python
import re

text = "Hello,    world! Welcome    to Python."
words = re.split(r"\s+", text)
print(words)
```

Go back to [Contents](#contents).



**Problem 3:** Replacing Text in a String

Replaces occurrences of a pattern with a specified string.

Solution: 

```python
import re

text = "Hello, world! world!"
replaced_text = re.sub("world", "Python", text)
print(replaced_text)
```

Go back to [Contents](#contents).



**Problem 4:** Extracting All Matches

Finds all non-overlapping matches of a pattern.

Solution: 

```python
import re

text = "Email me at email1@example.com and email2@example.net."
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
```

Go back to [Contents](#contents).



**Problem 5:** Ignoring Case Sensitivity

Performs case-insensitive matching.

Solution: 

```python
import re

text = "Hello, World!"
if re.search("world", text, re.IGNORECASE):
    print("Found a match!")
```

Go back to [Contents](#contents).



**Problem 6:** Grouping with Parentheses

Groups part of a pattern to extract specific portions of the matched text.

Solution: 

```python
import re

text = "My phone number is 123-456-7890."
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", text)
if match:
    print("Area code:", match.group(1))
    print("Local number:", match.group(2), match.group(3))
```

Go back to [Contents](#contents).



**Problem 7:** Using finditer for Match Objects

Finds all non-overlapping matches and returns them as an iterator of match objects.

Solution: 

```python
import re

text = "two too."
matches = re.finditer(r"t[wo]o", text, re.IGNORECASE)
for match in matches:
    print(f"'{match.group()}' found at {match.span()}")
```

Go back to [Contents](#contents).



**Problem 8:** Compiling Regular Expressions

Pre-compiles a regular expression pattern for repeated use.

Solution: 

```python
import re

pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
text = "Call me at 123-456-7890 or 098-765-4321."
for match in pattern.finditer(text):
    print("Found phone number:", match.group())
```

Go back to [Contents](#contents).



**Problem 9:** Named Groups

Uses named groups to refer to matched groups.

Solution: 

```python
import re

text = "John Smith <john.smith@example.com>"
match = re.search(r"(?P<name>[\w\s]+) <(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>", text)
if match:
    print("Name:", match.group("name"))
    print("Email:", match.group("email"))
```

Go back to [Contents](#contents).



**Problem 10:** Lookahead and Lookbehind Assertions

Matches a pattern only if it is followed or preceded by another pattern.

Solution: 

```python
import re

# Positive lookahead to find 'is' only if it's followed by ' great'
text = "Python is great, but not all the time is easy."
matches = re.findall(r"is(?= great)", text)
for match in matches:
    print("Found:", match)

# Negative lookbehind to exclude matches preceded by 'not '
text = "good bad not good"
matches = re.findall(r"(?<!not )good", text)
for match in matches:
    print("Found:", match)
```

Go back to [Contents](#contents).



#### subprocess

The `subprocess` module in Python allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. 

Here are 10 examples demonstrating its use for various tasks:

Go back to [Contents](#contents).



**Problem 1:** Running an external command and capturing its output:

Solution: 

```python
import subprocess
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

Go back to [Contents](#contents).



**Problem 2:** Checking the output of a command:

Solution: 

```python
import subprocess
result = subprocess.check_output(['echo', 'Hello World'], text=True)
print(result)
```

Go back to [Contents](#contents).



**Problem 3:** Running a command and checking for errors:

Solution: 

```python
import subprocess
subprocess.run(['false'], check=True)
```

Go back to [Contents](#contents).



**Problem 4:** Running a shell command:

Solution: 

```python
import subprocess
subprocess.run('cat /etc/passwd | grep root', shell=True)
```

Go back to [Contents](#contents).



**Problem 5:** Piping data between processes:

Solution: 

```python
import subprocess
p1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'httpd'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]
print(output)
```

Go back to [Contents](#contents).



**Problem 6:** Running a command with environment variables:

Solution: 

```python
import subprocess
env = {'MY_VAR': 'value'}
subprocess.run(['env'], env=env)
```

Go back to [Contents](#contents).



**Problem 7:** Running a command with a timeout:

Solution: 

```python
import subprocess
try:
    subprocess.run(['sleep', '10'], timeout=5)
except subprocess.TimeoutExpired:
    print('The command timed out.')
```

Go back to [Contents](#contents).



**Problem 8:** Capturing `stderr` separately from stdout:

Solution: 

```python
import subprocess
result = subprocess.run(['ls', 'non_existent_file'], capture_output=True, text=True)
print('stdout:', result.stdout)
print('stderr:', result.stderr)
```

Go back to [Contents](#contents).



**Problem 9:** Using the `subprocess.Popen` class for more control:

Solution: 

```python
import subprocess
process = subprocess.Popen(['ping', '-c', '4', 'example.com'], stdout=subprocess.PIPE, text=True)
for line in process.stdout:
    print(line.strip())
process.stdout.close()
process.wait()
```

Go back to [Contents](#contents).



**Problem 10:** Sending input to a process:

Solution: 

```python
import subprocess
process = subprocess.Popen(['cat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
stdout, stderr = process.communicate('Hello World\n')
print(stdout)
```

Go back to [Contents](#contents).



#### threading

The `threading` module in Python is used for running tasks concurrently. 

This can significantly improve the performance of I/O-bound applications. 

Here are 10 examples demonstrating different uses of the `threading` module:

Go back to [Contents](#contents).



**Problem 1:** Creating and starting a thread:

Solution: 

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

t = threading.Thread(target=print_numbers)
t.start()
t.join()  # Wait for the thread to complete
```

Go back to [Contents](#contents).



**Problem 2:** Passing arguments to thread target function:

Solution: 

```python
import threading

def print_message(message):
    print(message)

t = threading.Thread(target=print_message, args=("Hello, threading!",))
t.start()
t.join()
```

Go back to [Contents](#contents).



**Problem 3:** Using a subclass of `Thread`:

Solution: 

```python
import threading

class MyThread(threading.Thread):
    def run(self):
        print("Thread running")

t = MyThread()
t.start()
t.join()
```

Go back to [Contents](#contents).



**Problem 4:** Synchronizing threads with a `Lock`:

Solution: 

```python
import threading

lock = threading.Lock()

def thread_safe_function():
    with lock:
        # Critical section of code
        print("Lock acquired")

t1 = threading.Thread(target=thread_safe_function)
t2 = threading.Thread(target=thread_safe_function)

t1.start()
t2.start()

t1.join()
t2.join()
```

Go back to [Contents](#contents).



**Problem 5:** Using `Semaphore` for limiting access:

Solution: 

```python
import threading
import time

semaphore = threading.Semaphore(2)

def access_resource(i):
    print(f"Thread {i} is waiting to access the resource")
    with semaphore:
        print(f"Resource accessed by thread {i}")
        time.sleep(1)
    print(f"Thread {i} released the resource")

threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(4)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

Go back to [Contents](#contents).



**Problem 6:** Using `Event` for signaling between threads:

Solution: 

```python
import threading

event = threading.Event()

def waiter():
    print("Waiting for event")
    event.wait()
    print("Event triggered")

def trigger():
    print("Triggering event")
    event.set()

t1 = threading.Thread(target=waiter)
t2 = threading.Thread(target=trigger)

t1.start()
t2.start()

t1.join()
t2.join()
```

Go back to [Contents](#contents).



**Problem 7:** Using `Condition` for complex thread synchronization:

Solution: 

```python
import threading

condition = threading.Condition()
item = None

def producer():
    global item
    with condition:
        item = "Something"
        condition.notify()

def consumer():
    with condition:
        condition.wait()
        print(f"Consumed {item}")

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()
```

Go back to [Contents](#contents).



**Problem 8:** Using `Barrier` for synchronizing threads at a point:

Solution: 

```python
import threading

barrier = threading.Barrier(3)

def worker():
    print(f"Thread {threading.current_thread().name} waiting at barrier")
    barrier.wait()
    print(f"Thread {threading.current_thread().name} passed the barrier")

threads = [threading.Thread(target=worker) for _ in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

Go back to [Contents](#contents).



**Problem 9:** Using `Timer` for delayed execution of a function:

Solution: 

```python
import threading

def delayed_function():
    print("Function executed after delay")

timer = threading.Timer(5, delayed_function)  # Delay for 5 seconds
timer.start()
timer.join()  # Wait for the timer to expire
```

Go back to [Contents](#contents).



**Problem 10:** Managing thread-local data:

Solution: 

```python
import threading

thread_local = threading.local()

def worker():
    thread_local.x = threading.current_thread().name
    print(f"Thread {thread_local.x} setting thread-local data")

t1 = threading.Thread(target=worker)
t2 = threading.Thread(target=worker)

t1.start()
t2.start()

t1.join()
t2.join()
```

Go back to [Contents](#contents).



#### urllib

The `urllib` library in Python is used for fetching URLs (Uniform Resource Locators). 

It offers a simple interface for network resource access. 

Below are 10 examples demonstrating various uses of the `urllib` library, specifically focusing on `urllib.request` for HTTP requests, `urllib.parse` for URL parsing, and handling exceptions.

Go back to [Contents](#contents).



**Problem 1:** Fetching a Web Page's Content

Solution: 

```python
import urllib.request

url = "http://example.com"
response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent[:500])  # Print the first 500 bytes of the content
```

Go back to [Contents](#contents).



**Problem 2:** Downloading a File

Solution: 

```python
import urllib.request

url = "http://example.com/somefile.zip"
filename = "somefile.zip"
urllib.request.urlretrieve(url, filename)

print(f"Downloaded {url} as {filename}")
```

Go back to [Contents](#contents).



**Problem 3:** Sending Data with a POST Request

Solution: 

```python
import urllib.parse
import urllib.request

url = "http://httpbin.org/post"
values = {'key': 'value'}
data = urllib.parse.urlencode(values).encode('utf-8')  # Data should be bytes
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
result = response.read()

print(result)
```

Go back to [Contents](#contents).



**Problem 4:** Adding Headers to a Request

Solution: 

```python
import urllib.request

url = "http://httpbin.org/headers"
headers = {'User-Agent': 'My User Agent 1.0'}
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)
result = response.read()

print(result)
```

Go back to [Contents](#contents).



**Problem 5:** Error Handling

Solution: 

```python
import urllib.request
from urllib.error import URLError

url = "http://thisurldoesnotexist.com"
try:
    response = urllib.request.urlopen(url)
except URLError as e:
    print(e.reason)
```

Go back to [Contents](#contents).



**Problem 6:** Parsing URLs

Solution: 

```python
from urllib.parse import urlparse

url = "http://www.example.com/site?name=Main&section=Home"
parsed_url = urlparse(url)

print(f"Scheme: {parsed_url.scheme}")
print(f"Netloc: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query: {parsed_url.query}")
```

Go back to [Contents](#contents).



**Problem 7:** Constructing URLs

Solution: 

```python
from urllib.parse import urlunparse

components = ('http', 'www.example.com', '/index.html', '', 'a=1&b=2', '')
url = urlunparse(components)

print(url)
```

Go back to [Contents](#contents).



**Problem 8:** Encoding Query Parameters

Solution: 

```python
from urllib.parse import urlencode

query_params = {'name': 'John Doe', 'city': 'New York'}
encoded_params = urlencode(query_params)

print(f"Encoded Query Parameters: {encoded_params}")
```

Go back to [Contents](#contents).



**Problem 9:** Basic Authentication

Solution: 

```python
import urllib.request

url = "http://example.com/login"
username = "user"
password = "pass"

# Create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent[:500])
```

Go back to [Contents](#contents).



**Problem 10:** Handling Redirects

Solution: 

```python
import urllib.request

url = "http://github.com"  # GitHub HTTP URLs redirect to HTTPS

response = urllib.request.urlopen(url)
final_url = response.geturl()

print(f"Final URL after redirects: {final_url}")
```

Go back to [Contents](#contents).



#### socket

The `socket` module in Python provides access to the BSD socket interface, offering a way to communicate over networks using the TCP/IP protocol. 

Here are 10 examples demonstrating different uses of the socket module, from creating basic clients and servers to more advanced networking concepts.

Go back to [Contents](#contents).



**Problem 1:** Basic TCP Server

Solution: 

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    client_socket.sendall(b'Hello, client!')
    client_socket.close()
```

Go back to [Contents](#contents).



**Problem 2:** Basic TCP Client

Solution: 

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
data = client_socket.recv(1024)
client_socket.close()

print(f"Received: {data.decode()}")
```

Go back to [Contents](#contents).



**Problem 3:** UDP Server

Solution: 

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

while True:
    data, addr = server_socket.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    server_socket.sendto(b'Hello, UDP client!', addr)
```

Go back to [Contents](#contents).



**Problem 4:** UDP Client

Solution: 

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = b'Hello, server!'
client_socket.sendto(message, ('localhost', 12345))
data, server = client_socket.recvfrom(1024)
client_socket.close()

print(f"Received: {data.decode()}")
```

Go back to [Contents](#contents).



**Problem 5:** Setting Socket Options

Solution: 

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Enable address reuse
```

Go back to [Contents](#contents).



**Problem 6:** Non-blocking Sockets

Solution: 

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)  # Set socket to non-blocking mode
try:
    s.connect(('localhost', 12345))
except BlockingIOError:
    pass  # Ignore expected blocking errors
```

Go back to [Contents](#contents).



**Problem 7:** Timeout for Sockets

Solution: 

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)  # Set timeout to 5 seconds

try:
    s.connect(('localhost', 12345))
except socket.timeout:
    print("Connection timed out")
```

Go back to [Contents](#contents).



**Problem 8:** Echo Server with SocketServer

Solution: 

```python
from socketserver import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.sendall(data)

server = TCPServer(('localhost', 12345), EchoHandler)
server.serve_forever()
```

Go back to [Contents](#contents).



**Problem 9:** Getting Local Machine Name

Solution: 

```python
import socket

hostname = socket.gethostname()
print(f"Hostname: {hostname}")

local_ip = socket.gethostbyname(hostname)
print(f"IP Address: {local_ip}")
```

Go back to [Contents](#contents).



**Problem 10:** Using `getaddrinfo` for DNS Resolution

Solution: 

```python
import socket

result = socket.getaddrinfo("www.example.com", None)
for item in result:
    print(item)
```

Go back to [Contents](#contents).



#### sqlite3

The `sqlite3` module in Python provides an SQL interface compliant with the DB-API 2.0 specification.

SQLite (https://www.sqlite.org/): 
- SQLite is a software library that provides a relational database management system. 
- It is lightweight, serverless, and self-contained, meaning it doesn't require a separate server process to operate. 
- SQLite stores the entire database (definitions, tables, indexes, and the data itself) as a single cross-platform file on a host machine. 
- It's widely used for embedded database applications, such as in mobile apps, desktop applications, and certain web browsers, because of its simplicity, reliability, and ease of integration.

The `sqlite3` is a built-in module, so you don't need to install anything extra to use [SQLite](https://www.sqlite.org/) databases in Python. 

Here are 10 examples demonstrating various uses of the `sqlite3` module, from basic database operations to more advanced concepts.

Go back to [Contents](#contents).



**Problem 1:** Creating a New SQLite Database and Table

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

conn.commit()
conn.close()
```

Go back to [Contents](#contents).



**Problem 2:** Inserting Data into a Table

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY','RHAT',100,35.14)")

conn.commit()
conn.close()
```

Go back to [Contents](#contents).



**Problem 3:** Querying Data

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM stocks WHERE trans=?', ('BUY',)):
    print(row)

conn.close()
```

Go back to [Contents](#contents).



**Problem 4:** Using Parameterized Queries

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))
print(c.fetchone())

conn.close()
```

Go back to [Contents](#contents).



**Problem 5:** Updating Data

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("UPDATE stocks SET price = 100.0 WHERE symbol = 'RHAT'")
conn.commit()

conn.close()
```

Go back to [Contents](#contents).



**Problem 6:** Deleting Data

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("DELETE FROM stocks WHERE symbol = 'RHAT'")
conn.commit()

conn.close()
```

Go back to [Contents](#contents).



**Problem 7:** Using Row Objects

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
conn.row_factory = sqlite3.Row

c = conn.cursor()
c.execute('SELECT * FROM stocks')

row = c.fetchone()
print(row['symbol'], row['price'])

conn.close()
```

Go back to [Contents](#contents).



**Problem 8:** Creating an Index

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('CREATE INDEX idx_symbol ON stocks (symbol)')

conn.commit()
conn.close()
```

Go back to [Contents](#contents).



**Problem 9:** Executing Multiple Commands at Once

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.executescript('''
    DROP TABLE IF EXISTS stocks;
    CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real);
''')

conn.commit()
conn.close()
```

Go back to [Contents](#contents).



**Problem 10:** Using Transactions

Solution: 

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Start a transaction
conn.execute('BEGIN TRANSACTION;')

try:
    c.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY','RHAT',100,35.14)")
    # Imagine some other operations here...
    conn.commit()  # Commit changes
except:
    conn.rollback()  # Roll back changes on error

conn.close()
```

Go back to [Contents](#contents).



#### logging

The `logging` module in Python is a standard module that provides a flexible framework for emitting log messages from Python programs. 

It is designed to be easy to use and configure. 

Here are 10 examples demonstrating different uses of the logging module, from basic logging to configuring loggers with different log levels, formats, and output destinations.

Go back to [Contents](#contents).



**Problem 1:** Basic Logging

Solution: 

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
```

Go back to [Contents](#contents).



**Problem 2:** Logging to a File

Solution: 

```python
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.debug('This message will be written to the log file.')
```

Go back to [Contents](#contents).



**Problem 3:** Setting the Logging Format

Solution: 

```python
import logging

logging.basicConfig(format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG)
logging.info('This is an info message with a custom format.')
```

Go back to [Contents](#contents).



**Problem 4:** Logging Exception Information

Solution: 

```python
import logging

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Exception occurred")
```

Go back to [Contents](#contents).



**Problem 5:** Creating Custom Loggers

Solution: 

```python
import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.WARNING)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.warning('This is a warning message.')
```

Go back to [Contents](#contents).



**Problem 6:** Logging to Multiple Destinations

Solution: 

```python
import logging

logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)

# Log to file
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.ERROR)

# Log to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('Debug message')
logger.error('Error message')
```

Go back to [Contents](#contents).



**Problem 7:** Using Different Log Levels

Solution: 

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:Config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

Go back to [Contents](#contents).



**Problem 8:** Rotating Log Files

Solution: 

```python
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('my_rotating_logger')
logger.setLevel(logging.INFO)

# add a rotating handler
handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info("This is a test log message.")
```

Go back to [Contents](#contents).



**Problem 9:** Using Filters to Control Logging Output

Solution: 

```python
import logging

class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.addFilter(InfoFilter())

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message and should not appear.')
logger.info('This is an info message and should appear.')
```

Go back to [Contents](#contents).



**Problem 10:** Configuring Logging Using a Configuration File

Assuming you have a configuration file named logging.conf with the appropriate content.

Solution: 

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

Go back to [Contents](#contents).



#### glob

The `glob` module in Python is used to retrieve files/pathnames matching a specified pattern according to the rules used by Unix shell. 

Here are 10 examples demonstrating different uses of the `glob` module to work with file system paths:

Go back to [Contents](#contents).



**Problem 1:** List all Python files in the current directory

Solution: 

```python
import glob

for file in glob.glob("*.py"):
    print(file)
```

Go back to [Contents](#contents).



**Problem 2:** List all files in the current directory

Solution: 

```python
HERE
```

Go back to [Contents](#contents).



**Problem 3:** List all Python files in a specific directory

Solution: 

```python
import glob

for file in glob.glob("/path/to/directory/*.py"):
    print(file)
```

Go back to [Contents](#contents).



**Problem 4:** Using recursive wildcards to match files in subdirectories

Solution: 

```python
import glob

for file in glob.glob("**/*.py", recursive=True):
    print(file)
```

Go back to [Contents](#contents).



**Problem 5:** List all JPEG and PNG files in the current directory

Solution: 

```python
import glob

for file in glob.glob("*.jpg") + glob.glob("*.png"):
    print(file)
```

Go back to [Contents](#contents).



**Problem 6:** List directories only

Solution: 

```python
import glob
import os

for dir in glob.glob("*/"):
    print(os.path.dirname(dir))
```

Go back to [Contents](#contents).



**Problem 7:** List specific files using wildcard in the middle of the pattern

Solution: 

```python
import glob

for file in glob.glob("session_*.log"):
    print(file)
```

Go back to [Contents](#contents).



**Problem 8:** Exclude specific files using a list comprehension and `glob`

Solution: 

```python
import glob

all_py_files = glob.glob("*.py")
excluded_files = ["setup.py", "config.py"]
files = [f for f in all_py_files if f not in excluded_files]

for file in files:
    print(file)
```

Go back to [Contents](#contents).



**Problem 9:** List files with multiple extensions using `glob` with set syntax

Solution: 

```python
import glob

for file in glob.glob("*.{py,txt}", recursive=True):
    print(file)
```

Go back to [Contents](#contents).



**Problem 10:** Using glob to find specific configuration files in a directory tree

Solution: 

```python
import glob

for file in glob.glob("**/*.conf", recursive=True):
    print(file)
```

Go back to [Contents](#contents).



#### argparse

The `argparse` module in Python is used for parsing command-line arguments. 

It provides a mechanism to specify what arguments are required and automatically generates help and usage messages. 

Here are 10 examples demonstrating different uses and features of the argparse module:

Go back to [Contents](#contents).



**Problem 1:** Basic Argument Parsing

A simple script that parses one argument and prints it.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
args = parser.parse_args()
print(args.integers)
```

Go back to [Contents](#contents).



**Problem 2:** Adding Optional Arguments

Demonstrates adding optional arguments, which are not required to run the script.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Example with optional arguments.')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.accumulate(args.integers))
```

Go back to [Contents](#contents).



**Problem 3:** Using Short and Long Option Names

Using Short and Long Option Names

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Short and long option names.')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='increase output verbosity')
args = parser.parse_args()
if args.verbose:
    print("Verbosity turned on.")
```

Go back to [Contents](#contents).



**Problem 4:** Specifying Data Types for Arguments

Specifies the expected data type for the input arguments.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Specify data type of arguments.')
parser.add_argument('radius', metavar='R', type=float,
                    help='the radius of a circle')
args = parser.parse_args()
print(f"The area of the circle is: {3.14159 * args.radius ** 2}")
```

Go back to [Contents](#contents).



**Problem 5:** Default Values for Arguments

Shows how to set default values for optional arguments.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Default values for arguments.')
parser.add_argument('--name', default='John Doe',
                    help='your name (default: %(default)s)')
args = parser.parse_args()
print(f"Hello, {args.name}!")
```

Go back to [Contents](#contents).



**Problem 6:** Choice Arguments

Limits the options for an argument to a specific set of choices.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Choosing from a set of values.')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'],
                    help='your move in the game')
args = parser.parse_args()
print(f"You chose {args.move}.")
```

Go back to [Contents](#contents).



**Problem 7:** Counting Arguments

Counts the number of occurrences of a specific optional argument.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Count the occurrences of an argument.')
parser.add_argument('-v', '--verbose', action='count', default=0,
                    help='increase output verbosity (can be repeated)')
args = parser.parse_args()
level = args.verbose
print(f"Verbosity level: {level}")
```

Go back to [Contents](#contents).



**Problem 8:** Grouping Arguments

Groups related arguments together in the help message.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Grouping arguments in help.')
group = parser.add_mutually_exclusive_group()
group.add_argument('--verbose', action='store_true',
                   help='make the operation more talkative')
group.add_argument('--quiet', action='store_true',
                   help='make the operation quieter')
args = parser.parse_args()
```

Go back to [Contents](#contents).



**Problem 9:** Sub-commands

Uses subparsers to implement sub-commands.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='An example with sub-commands.')
subparsers = parser.add_subparsers(dest='command', help='sub-command help')

# create the parser for the "a" command
parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

args = parser.parse_args()
print(f"Executing '{args.command}' command.")
```

Go back to [Contents](#contents).



**Problem 10:** Argument Groups for Organizing Arguments

Organizes arguments into groups for better help message organization.

Solution: 

```python
import argparse

parser = argparse.ArgumentParser(description='Groups for organizing arguments.')
group = parser.add_argument_group('group1', 'Group 1 description')
group.add_argument('--foo', help='foo help')
group2 = parser.add_argument_group('group2', 'Group 2 description')
group2.add_argument('--bar', help='bar help')

args = parser.parse_args()
```

Go back to [Contents](#contents).



### Installing Python Libraries

Installing Python libraries is a straightforward process that can be done using Python's package manager, `pip`. 

Here's a step-by-step guide on how to install Python libraries:

Go back to [Contents](#contents).



#### Step 1 - Ensure Python and pip are Installed

Before installing Python libraries, you need to have Python installed on your system. 

Python installation typically includes pip (Python's package installer). 

To check if Python and pip are installed, open a command line (Command Prompt on Windows, Terminal on macOS and Linux/Unix) and run:

```shell
python --version
pip --version
```

If you see version numbers for both Python and pip, you're ready to install libraries. 

If not, download and install Python from the official website: [python.org](https://www.python.org/). 

Make sure to select the option to add Python to your PATH during installation.

Go back to [Contents](#contents).



#### Step 2 - Use pip to Install Libraries


Once Python and pip are installed, you can use pip to install libraries. 

The general syntax for installing a library is:

```shell
pip install library_name
```

Replace `library_name` with the name of the library you want to install.

Examples:

* To install NumPy, run:

```shell
pip install numpy
```

* To install Pandas, run:

```shell
pip install pandas
```

* For libraries that require a specific version, you can specify the version number:

```shell
pip install numpy==1.18.5
```

Go back to [Contents](#contents).



#### Step 3 - Verifying Installation

After installation, you can verify that a library is installed correctly by importing it in Python. 

Open a Python shell (just type python in your command line) and try importing the library:

```shell
import numpy
```

If there are no error messages, the library has been successfully installed.

Go back to [Contents](#contents).



#### Virtual Environments


* **Creating Virtual Environments:** It's often a good practice to use virtual environments to manage dependencies for different projects. 
To create a virtual environment, you can use:

```shell
python -m venv myenv
```

Activate the virtual environment with:

* On Windows:

```shell
myenv\Scripts\activate
```

* On macOS and Linux:

```shell
source myenv/bin/activate
```

Once activated, you can install libraries within this environment without affecting your global Python installation.


* **Updating a Library:** To update an existing library, use:


```shell
pip install --upgrade library_name
```


* **Using requirements.txt:** For larger projects, you can list all required libraries along with their versions in a **requirements.txt** file and install them using:

```shell
pip install -r requirements.txt
```


* **Export the requirements.txt file:** To export the Python libraries installed in a virtual environment:

Once your virtual environment is activated, run the following command:

```shell
pip freeze > requirements.txt
```

* Deactivate the virtual environment:

```shell
deactivate
```

* **Troubleshooting:** 
 
If you encounter any issues:
  * Check your internet connection.
  * Check the spelling of the library name.
  * Ensure that you have the necessary permissions to install software on your system. 
  * For some systems, you might need to prefix pip commands with sudo for administrative access.

Go back to [Contents](#contents).



### NumPy

NumPy (https://numpy.org/), short for Numerical Python, is one of the most fundamental packages for numerical computations in Python. 

It provides powerful support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions that operate on these arrays.

The key features of NumPy include:

1. **Efficient Array Processing:** High-performance array object ndarray for efficient storage and manipulation of multi-dimensional dense arrays.

2. **Broadcasting Capabilities:** Simplifies array operations by allowing operations on arrays of different shapes and sizes.

3. **Mathematical Functions:** A comprehensive collection of mathematical functions to perform operations on arrays and matrices.

4. **Linear Algebra:** Support for various linear algebra operations like matrix multiplication, eigenvalues, determinants, and more.

5. **Random Number Generation:** Powerful random number generators and tools for random sampling.

6. **Integration with other Python Libraries:** Widely used in scientific computing, data science, and is the foundation for many other scientific libraries.

Go back to [Contents](#contents).



#### Steps to install and use the Numpy library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Numpy (if it is not installed)

```bash
pip install numpy
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Numpy Examples


**Example 1:** Creating a NumPy Array

```python
import numpy as np

# Creating a simple NumPy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

Output:

```
[1 2 3 4 5]
```

Go back to [Contents](#contents).


**Example 2:** Basic Array Operations (Addition, Multiplication)

```python
import numpy as np

# Element-wise addition and multiplication
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
```

Output:

```
Addition: [5 7 9]
Multiplication: [ 4 10 18]
```

Go back to [Contents](#contents).


**Example 3:** Reshaping an Array

```python
import numpy as np

# Reshaping a 1D array to a 2D array
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
```

Output:

```
[[1 2 3]
 [4 5 6]]
```

Go back to [Contents](#contents).


**Example 4:** Slicing Arrays

```python
import numpy as np

# Slicing an array
arr = np.array([1, 2, 3, 4, 5, 6])
sliced_arr = arr[1:5]
print(sliced_arr)
```

Output:

``` 
[2 3 4 5]
```

Go back to [Contents](#contents).


**Example 5:** Linear Algebra - Matrix Multiplication

```python
import numpy as np

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.dot(A, B)
print(result)
```

Output:

```
[[19 22]
 [43 50]]
```

Go back to [Contents](#contents).


**Example 6:** Computing the Inverse of a Matrix

```python
import numpy as np

# Inverse of a matrix
matrix = np.array([[1, 2], [3, 4]])
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)
```

Output:

```
[[-2.   1. ]
 [ 1.5 -0.5]]
```

Go back to [Contents](#contents).


**Example 7:** Generating Random Numbers

```python
import numpy as np

# Generating random numbers
random_arr = np.random.rand(5)
print(random_arr)
```

Output:

Note: Your output will be different random numbers

```
[0.99451184 0.11360742 0.12704345 0.4183472  0.9458018 ]
```

Go back to [Contents](#contents).


**Example 8:** Statistical Operations (Mean, Median, Standard Deviation)

```python
import numpy as np

# Statistical operations
arr = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
```

Output:

```
Mean: 3.0
Median: 3.0
Standard Deviation: 1.4142135623730951
```

Go back to [Contents](#contents).


**Example 9:** Boolean Indexing

```python
import numpy as np

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])
```

Output:

```
[4 5]
```

Go back to [Contents](#contents).


**Example 10:** Stacking Arrays

```python
import numpy as np

# Stacking arrays vertically and horizontally
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

v_stack = np.vstack((arr1, arr2))
h_stack = np.hstack((arr1, arr2))

print("Vertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)
```

Output:

```
Vertical Stack:
 [[1 2 3]
 [4 5 6]]
Horizontal Stack:
 [1 2 3 4 5 6]
```

Go back to [Contents](#contents).



### SciPy

SciPy (https://scipy.org/), short for Scientific Python, is a fundamental library for scientific computing in Python. 

It builds on NumPy arrays and provides a large number of higher-level functions that operate on numpy arrays and are useful for different types of scientific and engineering applications.

Key features of SciPy include:

1. **Multidimensional Image Processing:** Functions for image manipulation and processing. 
2. **Optimization Algorithms:** For function minimization, root finding, and curve fitting. 
3. **Signal Processing:** Tools for signal filtering, construction, and analysis. 
4. **Linear Algebra:** Advanced linear algebra capabilities and matrix decompositions. 
5. **Integration and Ordinary Differential Equations:** For integrating functions and solving differential equations. 
6. **Statistics and Random Numbers:** Extensive statistics and random number generation functions. 
7. **Interpolation:** Tools for interpolating between data points.

Go back to [Contents](#contents).



#### Steps to install and use the SciPy library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install SciPy (if it is not installed)

```bash
pip install scipy
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### SciPy Examples


**Example 1:** Solving a Linear System of Equations

```python
import numpy as np
from scipy.linalg import solve

# Define the coefficient matrix A and the constant vector b
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

# Solve the linear system Ax = b
x = solve(A, b)
print(x)
```

Output:

```
[2. 3.]
```

Go back to [Contents](#contents).


**Example 2:** Calculating Eigenvalues and Eigenvectors

```python
import numpy as np
from scipy.linalg import eig

# Define a square matrix
A = np.array([[1, 2], [3, 4]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
```

Output:

```
Eigenvalues: [-0.37228132+0.j  5.37228132+0.j]
Eigenvectors:
 [[-0.82456484 -0.41597356]
 [ 0.56576746 -0.90937671]]
```

Go back to [Contents](#contents).


**Example 3:** Optimization - Minimizing a Function

```python
import numpy as np
from scipy.optimize import minimize

# Define a quadratic function
def f(x):
    return x**2 + 10 * np.sin(x)

# Minimize the function
result = minimize(f, x0=0)
print(result.x)
```

Output:

```python
[-1.30644012]
```

Go back to [Contents](#contents).


**Example 4:** Interpolating Data

```python
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Define sample data
x = np.linspace(0, 10, num=10, endpoint=True)
y = np.cos(-x**2/9.0)

# Interpolate data
f = interp1d(x, y, kind='cubic')

# New x values
xnew = np.linspace(0, 10, num=40, endpoint=True)

# Plot
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.show()
```

Plotting:

![SciPy - Example 4 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/scipy_example_4.png)

Go back to [Contents](#contents).


**Example 5:** Signal Processing - Filtering a Signal

```python
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

# Sample data
t = np.linspace(0, 1.0, 200)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.random.randn(t.size)

# Butterworth filter
b, a = butter(N=3, Wn=0.05)
filtered_signal = lfilter(b, a, signal)

# Plot
plt.plot(t, signal, label='Noisy signal')
plt.plot(t, filtered_signal, label='Filtered signal')
plt.legend()
plt.show()
```

Plotting:

![SciPy - Example 5 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/scipy_example_5.png)

Go back to [Contents](#contents).


**Example 6:** Computing the Integral of a Function

```python
from scipy.integrate import quad

# Define a simple function
def integrand(x):
    return x**2

# Compute definite integral
result, error = quad(integrand, 0, 1)
print(result)
```

``` 
0.3333333333333333
```

Go back to [Contents](#contents).


**Example 7:** Solving a Differential Equation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define a differential equation y' = y
def model(y, t):
    return y

# Time points
t = np.linspace(0, 5)

# Solve ODE
y = odeint(model, y0=1, t=t)

# Plot
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()
```

Plotting:

![SciPy - Example 7 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/scipy_example_7.png)

Go back to [Contents](#contents).


**Example 8:** Fourier Transform of a Signal

```python
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt

# Sample data
t = np.linspace(0, 1.0, 400)
signal = np.sin(50 * 2 * np.pi * t)

# Compute Fourier Transform
signal_fft = fft(signal)

# Plot
plt.plot(t, signal)
plt.plot(t, np.abs(signal_fft))
plt.show()
```

Plotting:

![SciPy - Example 8 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/scipy_example_8.png)

Go back to [Contents](#contents).


**Example 9:** Performing a T-test

```python
import numpy as np
from scipy.stats import ttest_ind

# Sample data
a = np.random.normal(0, 1, size=100)
b = np.random.normal(1, 1, size=100)

# T-test
t_statistic, p_value = ttest_ind(a, b)
print("t-statistic:", t_statistic)
print("p-value:", p_value)
```

```
t-statistic: -6.670615980189455
p-value: 2.4886726181389886e-10
```

Go back to [Contents](#contents).


**Example 10:** Multidimensional Image Processing

```python
from scipy import ndimage
import imageio
import matplotlib.pyplot as plt

# Load an image
image = imageio.imread('images/RFP_YouTube_Profile_Picture.png')

# Gaussian blur
blurred_image = ndimage.gaussian_filter(image, sigma=3)

# Display images
plt.imshow(image, cmap=plt.cm.gray)
plt.imshow(blurred_image, cmap=plt.cm.gray)
plt.show()
```

Plotting:

![SciPy - Example 10 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/scipy_example_10.png)

Go back to [Contents](#contents).



### Pandas

Pandas (https://pandas.pydata.org/) is a highly popular Python library used primarily for data manipulation and analysis. 

Built on top of the NumPy library, it offers data structures and operations for manipulating numerical tables and time series. 

Pandas is particularly suited for handling tabular data (like spreadsheets), time series data, any form of observational or statistical data sets.

The key features of Pandas include:

1. **DataFrame:** A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).
2. **Series:** A one-dimensional labeled array capable of holding any data type.
3. **Efficient Data Handling:** Capabilities for efficiently handling missing data, merging, reshaping, grouping, and selecting data.
4. **Time Series Functionality:** Extensive support for working with dates, times, and time-indexed data.
5. **Reading and Writing Data:** Support for multiple formats including CSV, Excel, SQL databases, and HDF5 format.

Go back to [Contents](#contents).



#### Steps to install and use the Pandas library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Pandas (if it is not installed)

```bash
pip install pandas
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Pandas Examples


**Example 1:** Creating a DataFrame

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['John', 'Mary', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 15, 34, 29, 32]}
df = pd.DataFrame(data)
print(df)
# Save data frame to a CSV file
df.to_csv('data/data_name_age.csv', index=False)
```

Output:

```
    Name  Age
0   John   28
1   Mary   15
2   Anna   34
3  Peter    9
4  Linda   32
```

Go back to [Contents](#contents).


**Example 2:** Reading Data from a CSV File

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age_salary.csv')
print(df.head())
```

Output:

```
    Name  Age    Salary
0   John   28   80000.0
1   Mary   15       0.0
2   Anna   34   90000.0
3  Peter    9       NaN
4  Linda   32  100000.0
```

Go back to [Contents](#contents).


**Example 3:** Selecting Columns

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age_salary.csv')

print(df, '\n')

# Selecting a single column
ages = df['Age']
print(ages, '\n')

# Selecting multiple columns
subset = df[['Name', 'Age']]
print(subset, '\n')
```

Output:

```
    Name  Age    Salary
0   John   28   80000.0
1   Mary   15       0.0
2   Anna   34   90000.0
3  Peter    9       NaN
4  Linda   32  100000.0 

0    28
1    15
2    34
3     9
4    32
Name: Age, dtype: int64 

    Name  Age
0   John   28
1   Mary   15
2   Anna   34
3  Peter    9
4  Linda   32
```

Go back to [Contents](#contents).


**Example 4:** Filtering Rows

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age.csv')

print(df, '\n')

# Filtering rows based on a condition
adults = df[df['Age'] >= 18]
print(adults)
```

Output:

```
    Name  Age
0   John   28
1   Mary   15
2   Anna   34
3  Peter    9
4  Linda   32 

    Name  Age
0   John   28
2   Anna   34
4  Linda   32
```

Go back to [Contents](#contents).


**Example 5:** Data Aggregation (Group By)

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_and_salary_with_duplicate_names.csv')

print(df, '\n')

# Grouping and aggregating data
average_age = df.groupby('Name')['Salary'].mean()
print(average_age)
```

Output:

```
   Name  Salary
0  John   80000
1  Mary       0
2  Anna   90000
3  John   20000
4  Anna  100000 

Name
Anna    95000.0
John    50000.0
Mary        0.0
Name: Salary, dtype: float64
```

Go back to [Contents](#contents).


**Example 6:** Handling Missing Data

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age_salary_missing_values.csv')

print(df, '\n')

# Filling missing values
df.fillna(value=0, inplace=True)

print(df, '\n')

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age_salary_missing_values.csv')

print(df, '\n')

# Dropping rows with missing values
df.dropna(inplace=True)

print(df)
```

Output:

```
    Name   Age    Salary
0   John  28.0   80000.0
1    NaN   NaN       NaN
2   Anna  34.0       NaN
3  Peter   9.0       NaN
4  Linda  32.0  100000.0 

    Name   Age    Salary
0   John  28.0   80000.0
1      0   0.0       0.0
2   Anna  34.0       0.0
3  Peter   9.0       0.0
4  Linda  32.0  100000.0 

    Name   Age    Salary
0   John  28.0   80000.0
1    NaN   NaN       NaN
2   Anna  34.0       NaN
3  Peter   9.0       NaN
4  Linda  32.0  100000.0 

    Name   Age    Salary
0   John  28.0   80000.0
4  Linda  32.0  100000.0
```

Go back to [Contents](#contents).


**Example 7:** Merging DataFrames

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age.csv')

# Merging two DataFrames
other_data = pd.DataFrame({'Name': ['John', 'Anna'], 'Salary': [70000, 80000]})
merged_df = pd.merge(df, other_data, on='Name')
print(merged_df)
```

Output:

```
   Name  Age  Salary
0  John   28   70000
1  Anna   34   80000
```

Go back to [Contents](#contents).


**Example 8:** Sorting Data

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age.csv')

# Sorting the DataFrame by a column
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
```

Output:

```
    Name  Age
2   Anna   34
4  Linda   32
0   John   28
1   Mary   15
3  Peter    9
```

Go back to [Contents](#contents).


**Example 9:** Pivot Tables

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_and_salary_with_duplicate_names.csv')

# Creating a pivot table
pivot = df.pivot_table(values='Salary', index='Name', aggfunc='mean')
print(pivot)
```

Output:

```
       Salary
Name         
Anna  95000.0
John  50000.0
Mary      0.0
```

Go back to [Contents](#contents).


**Example 10:** Writing to an Excel File

```python
import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age.csv')

# Writing DataFrame to an Excel file
df.to_excel('data/data_name_age.xlsx', index=False)
```

Go back to [Contents](#contents).



### Matplotlib

Matplotlib (https://matplotlib.org/) is a comprehensive library for creating static, animated, and interactive visualizations in Python. 

It is one of the most popular Python libraries used for data visualization. 

Matplotlib makes it easy to create plots, histograms, power spectra, bar charts, error charts, scatterplots, etc., with just a few lines of code.

Key features of Matplotlib include:

1. **Plotting Interface:** Simple functions for creating common types of plots.
2. **Customization:** Extensive support for customizing all aspects of a plot. 
3. **Backend Support:** Works with many operating systems and graphics backends. 
4. **Integration:** Integrates well with Pandas and NumPy for data analysis. 
5. **Subplots:** Create figures with multiple subplots.

Go back to [Contents](#contents).



#### Steps to install and use the Matplotlib library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Matplotlib (if it is not installed)

```bash
pip install matplotlib
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Matplotlib Examples

**Example 1:** Basic Line Plot

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Basic Line Plot')
plt.show()
```

Plotting:

![Matplotlib - Example 1 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_1.png)

Go back to [Contents](#contents).


**Example 2:** Bar Chart

```python
import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C']
values = [3, 7, 2]

plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()
```

Plotting:

![Matplotlib - Example 2 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_2.png)

Go back to [Contents](#contents).


**Example 3:** Histogram

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()
```

Plotting:

![Matplotlib - Example 3 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_3.png)

Go back to [Contents](#contents).


**Example 4:** Scatter Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()
```

Plotting:

![Matplotlib - Example 4 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_4.png)

Go back to [Contents](#contents).


**Example 5:** Pie Chart

```python
import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['Apples', 'Bananas', 'Grapes', 'Oranges']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Pie Chart')
plt.show()
```

Plotting:

![Matplotlib - Example 5 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_5.png)

Go back to [Contents](#contents).


**Example 6:** Error Bars

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
error = 0.1 + 0.2 * x

plt.errorbar(x, y, yerr=error, fmt='-o')
plt.title('Error Bars')
plt.show()
```

Plotting:

![Matplotlib - Example 6 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_6.png)

Go back to [Contents](#contents).


**Example 7:** Subplots

```python
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(2)
x = np.arange(0, 2, 0.01)

axs[0].plot(x, np.sin(2 * np.pi * x))
axs[1].plot(x, np.cos(2 * np.pi * x))
plt.show()
```

Plotting:

![Matplotlib - Example 7 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_7.png)

Go back to [Contents](#contents).


**Example 8:** 3D Plot

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.linspace(-5, 5, 100)
ax.plot(x, y, z)
plt.show()
```

Plotting:

![Matplotlib - Example 8 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_8.png)

Go back to [Contents](#contents).


**Example 9:** Heatmap

```python
import matplotlib.pyplot as plt
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.show()
```

Plotting:

![Matplotlib - Example 9 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_9.png)

Go back to [Contents](#contents).


**Example 10:** Contour Plot

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()
plt.show()
```

Plotting:

![Matplotlib - Example 10 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/matplotlib_example_10.png)

Go back to [Contents](#contents).



### Seaborn

Seaborn (https://seaborn.pydata.org/) is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. 

Seaborn is particularly well suited for exploring and understanding data through the use of plotting functions that operate on entire dataframes and arrays containing whole datasets.

Key features of Seaborn include:

1. **Built-In Datasets:** Offers a variety of built-in datasets, making it easy to demonstrate the capabilities of its plotting functions.
2. **Statistical Estimation:** Automatically performs the statistical estimation while plotting data, which is helpful for exploring complex datasets.
3. **Plotting with DataFrames:** Seamlessly integrates with Pandas DataFrames, allowing for efficient plotting directly from data frames.
4. **Advanced Plots:** Provides support for more advanced plots such as heatmaps, time series, violin plots, and pair plots.
5. **Aesthetic Themes:** Offers a variety of themes and color palettes to make attractive plots that are more appealing and readable.

Go back to [Contents](#contents).



#### Steps to install and use the Seaborn library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Seaborn (if it is not installed)

```bash
pip install seaborn
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Seaborn Examples


**Example 1:** Basic Scatter Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 1 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_1.png)

Go back to [Contents](#contents).


**Example 2:** Line Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.show()
```

Plotting:

![Seaborn - Example 2 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_2.png)

Go back to [Contents](#contents).


**Example 3:** Bar Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 3 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_3.png)

Go back to [Contents](#contents).


**Example 4:** Histogram

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total_bill", kde=True)
plt.show()
```

Plotting:

![Seaborn - Example 4 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_4.png)

Go back to [Contents](#contents).


**Example 5:** Box Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 5 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_5.png)

Go back to [Contents](#contents).


**Example 6:** Violin Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 6 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_6.png)

Go back to [Contents](#contents).


**Example 7:** Pair Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.pairplot(data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 7 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_7.png)

Go back to [Contents](#contents).


**Example 8:** Heatmap

```python
import seaborn as sns
import matplotlib.pyplot as plt

flights = sns.load_dataset("flights")
# Use keyword arguments for clarity and to match the method's expected signature
flights = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(flights, annot=True, fmt="d")
plt.show()
```

Plotting:

![Seaborn - Example 8 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_8.png)

Go back to [Contents](#contents).


**Example 9:** Joint Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
plt.show()
```

Plotting:

![Seaborn - Example 9 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_9.png)

Go back to [Contents](#contents).


**Example 10:** Facet Grid

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time", row="smoker")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
```

Plotting:

![Seaborn - Example 10 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_10.png)

Go back to [Contents](#contents).


**Example 11:** Count Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.countplot(x="day", data=tips)
plt.show()
```

Plotting:

![Seaborn - Example 11 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_11.png)

Go back to [Contents](#contents).


**Example 12:** Pair Plot with Hue

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.pairplot(data=tips, hue="smoker")
plt.show()
```

Plotting:

![Seaborn - Example 12 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/seaborn_example_12.png)

Go back to [Contents](#contents).



### Plotly

Plotly (https://plotly.com/python/) is a Python graphing library that makes interactive, publication-quality graphs online. 

It is an open-source library capable of creating complex plots with simple syntax, and it supports over 40 unique chart types. 

One of Plotly's main features is its ability to render interactive plots that can be embedded in web applications or viewed as standalone web pages.

Key features of Plotly include:

1. **Interactivity:** Users can zoom, pan, update, and hover over points in the plot, making it highly interactive.
2. **Variety of Plot Types:** Supports a wide range of plots including line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and 3D charts.
3. **Customizable:** Offers extensive customization options for each element of a plot.
4. **Web Integration:** Easily integrates with web technologies, allowing plots to be rendered in a web browser.
5. **Ease of Use:** Provides a simple and intuitive syntax for creating complex plots.

Go back to [Contents](#contents).



#### Steps to install and use the Plotly library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Plotly (if it is not installed)

```bash
pip install plotly
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Plotly Examples


**Example 1:** Basic Line Plot

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13], mode='lines+markers'))
fig.show()
```

Plotting:

![Plotly - Example 1 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_1.png)

Go back to [Contents](#contents).


**Example 2:** Bar Chart

```python
import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(name='Group A', x=['Category 1', 'Category 2'], y=[10, 12]),
    go.Bar(name='Group B', x=['Category 1', 'Category 2'], y=[13, 17])
])
fig.update_layout(barmode='group')
fig.show()
```

Plotting:

![Plotly - Example 2 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_2.png)

Go back to [Contents](#contents).


**Example 3:** Scatter Plot

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.show()
```

Plotting:

![Plotly - Example 3 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_3.png)

Go back to [Contents](#contents).


**Example 4:** Pie Chart

```python
import plotly.express as px

fig = px.pie(values=[30, 35, 35], names=['Product A', 'Product B', 'Product C'])
fig.show()
```

Plotting:

![Plotly - Example 4 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_4.png)

Go back to [Contents](#contents).


**Example 5:** 3D Surface Plot

```python
import plotly.graph_objects as go
import numpy as np

x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
y = x.copy().T
z = np.sin(x ** 2 + y ** 2)

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.show()
```

Plotting:

![Plotly - Example 5 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_5.png)

Go back to [Contents](#contents).


**Example 6:** Heatmap

```python
import plotly.graph_objects as go
import numpy as np

data = np.random.rand(10, 10)
fig = go.Figure(data=go.Heatmap(z=data))
fig.show()
```

Plotting:

![Plotly - Example 6 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_6.png)

Go back to [Contents](#contents).


**Example 7:** Histogram

```python
import plotly.graph_objects as go
import numpy as np

data = np.random.randn(500)
fig = go.Figure(data=[go.Histogram(x=data)])
fig.show()
```

Plotting:

![Plotly - Example 7 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_7.png)

Go back to [Contents](#contents).


**Example 8:** Box Plot

```python
import plotly.graph_objects as go
import numpy as np

data = np.random.normal(size=100)
fig = go.Figure(data=[go.Box(y=data, boxpoints='all', jitter=0.3, pointpos=-1.8)])
fig.show()
```

Plotting:

![Plotly - Example 8 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_8.png)

Go back to [Contents](#contents).


**Example 9:** Contour Plot

```python
import plotly.graph_objects as go
import numpy as np

x = np.arange(15)
y = np.arange(15)
z = np.random.rand(15, 15)

fig = go.Figure(data=[go.Contour(z=z, x=x, y=y)])
fig.show()
```

Plotting:

![Plotly - Example 9 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_9.png)

Go back to [Contents](#contents).


**Example 10:** Bubble Chart

```python
import plotly.express as px

df = px.data.gapminder().query("year==2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                 hover_name="country", log_x=True, size_max=60)
fig.show()
```

Plotting:

![Plotly - Example 10 - Plotting](https://github.com/ramonfigueiredo/python_course/blob/main/images/plotly_example_10.png)

Go back to [Contents](#contents).



### Requests

The requests (https://requests.readthedocs.io/en/latest/) library in Python simplifies making HTTP requests to web servers. 

It's not part of the standard library, so it requires installation using pip install requests. Once installed, it provides an easy-to-use API for making GET, POST, and other HTTP requests, handling cookies, sessions, headers, and more. 

Go back to [Contents](#contents).



#### Steps to install and use the Requests library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Requests (if it is not installed)

```bash
pip install requests
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Requests Examples


**Example 1:** Making a GET Request

Retrieves information from a specified URL.

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.text)
```

Go back to [Contents](#contents).



**Example 2:** Adding Query Parameters to GET Request

Sends additional data in the URL's query string.

```python
import requests

payload = {'q': 'python', 'sort': 'stars'}
response = requests.get('https://api.github.com/search/repositories', params=payload)
print(response.url)  # The URL will contain the query parameters
```

Go back to [Contents](#contents).



**Example 3:** Making a POST Request

Sends data to a URL to create/update a resource.

```python
import requests

data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.text)
```

Go back to [Contents](#contents).



**Example 4:** Adding Headers to Your Request

Modifies request headers.

```python
import requests

headers = {'User-Agent': 'my-app/0.0.1'}
response = requests.get('https://api.github.com', headers=headers)
print(response.request.headers)
```

Go back to [Contents](#contents).



**Example 5:** Handling Response JSON Content

Automatically decodes JSON response content.

```python
import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    data = response.json()
    print(data)  # `data` is a Python dictionary
```

Go back to [Contents](#contents).



**Example 6:** Handling HTTP Exceptions Gracefully

Catches HTTP errors elegantly.

```python
import requests
from requests.exceptions import HTTPError

try:
    response = requests.get('https://api.github.com/invalid')
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
```

Go back to [Contents](#contents).



**Example 7:** Using Sessions with `requests`

Reuses configuration across requests.

```python
import requests

with requests.Session() as session:
    session.headers.update({'User-Agent': 'my-app/0.0.1'})
    
    response = session.get('https://api.github.com')
    print(response.headers)
```

Go back to [Contents](#contents).



**Example 8:** Downloading Files

Efficiently downloads files without loading them entirely into memory.

```python
import requests

url = 'http://example.com/somefile.zip'
with requests.get(url, stream=True) as r:
    with open('somefile.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192): 
            f.write(chunk)
```

Go back to [Contents](#contents).



**Example 9:** Handling Cookies

Sends and receives cookies.

```python
import requests

response = requests.get('https://www.google.com')
print(response.cookies)

# Send cookies to a server
cookies = {'session_token': '123456789'}
response = requests.get('https://www.google.com', cookies=cookies)
```

Go back to [Contents](#contents).



**Example 10:** Using Timeouts

Sets a timeout for a request to avoid hanging indefinitely.

```python
import requests

try:
    response = requests.get('https://api.github.com', timeout=1)
    print(response.status_code)
except requests.Timeout:
    print('The request timed out')
```

Go back to [Contents](#contents).



### Flask

Flask (https://flask.palletsprojects.com/) is a lightweight and powerful web framework for Python. 

It is classified as a microframework because it does not require particular tools or libraries and has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. 

However, Flask supports extensions that can add application features as if they were implemented in Flask itself.

Key features of Flask include:

1. **Simplicity:** Easy to get started with a simple and minimalistic approach.
2. **Flexibility:** Highly customizable and adaptable to the developer's needs.
3. **Built-in Development Server and Debugger:** Includes a development server and a debugger.
4. **RESTful Request Dispatching:** Supports REST principles, making it a great choice for building RESTful APIs.
5. **Jinja2 Templating:** Integrated support for Jinja2 templates.
6. **WSGI 1.0 Compliance:** Compatible with WSGI (Web Server Gateway Interface).
7. **Unicode-Based:** Fully Unicode-compliant for seamless processing of text data.
8. **Extensibility:** Flask can be extended with numerous extensions available for tasks such as database integration, form validation, upload handling, and more.

Go back to [Contents](#contents).



#### Steps to install and use the Flask library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Flask (if it is not installed)

```bash
pip install flask
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Flask Examples


**Example 1:** Basic Flask Application

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

Go back to [Contents](#contents).


**Example 2:** Using Route Parameters

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
```

Go back to [Contents](#contents).


**Example 3:** Rendering Templates

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

Go back to [Contents](#contents).


**Example 4:** Handling POST Requests

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

Go back to [Contents](#contents).


**Example 5:** Redirects and Errors

```python
from flask import abort, redirect, url_for

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('hello_world'))

@app.route('/error')
def error_example():
    abort(404)
```

Go back to [Contents](#contents).


**Example 6:** Creating a RESTful API

```python
from flask import jsonify

@app.route('/api/data')
def get_data():
    return jsonify({'data': 'Here is some data'})
```

Go back to [Contents](#contents).


**Example 7:** File Upload

```python
from flask import request

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/path/to/uploaded/file')
```

Go back to [Contents](#contents).


**Example 8:** Working with Cookies

```python
from flask import request, make_response

@app.route('/setcookie')
def setcookie():
    resp = make_response('Setting cookie!')
    resp.set_cookie('mycookie', 'cookie value')
    return resp

@app.route('/getcookie')
def getcookie():
    cookie = request.cookies.get('mycookie')
    return f'Cookie value: {cookie}'
```

Go back to [Contents](#contents).


**Example 9:** Session Management

```python
from flask import session

@app.route('/setsession')
def setsession():
    session['username'] = 'username'
    return 'Session set'

@app.route('/getsession')
def getsession():
    return session.get('username', 'Not set')
```

Go back to [Contents](#contents).


**Example 10:** Using Flask Extensions (Flask-SQLAlchemy)

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

Go back to [Contents](#contents).



#### Some examples of Flask projects are available on my GitHub account

My GitHub repository has some publicly available Flask projects.

[TODO list application - REST api using Flask-RESTful](https://github.com/ramonfigueiredo/flask_todo_app_rest_api-using_flask-restful)
- Use Flask, Flask-HTTPAuth, and Flask-RESTful to create a TODO list application!

[RESTful Authentication with Flask](https://github.com/ramonfigueiredo/restful_authentication_with_flask)
- Use Flask, Flask-HTTPAuth, and Flask-SQLAlchemy to create a RESTful Authentication with Flask

[A Flask API for serving scikit-learn models](https://github.com/ramonfigueiredo/flask_api_for_serving_scikit_learn_models)
- Use Flask, Numpy, Pandas, and Scikit-Learn to craete a Flask API for serving scikit-learn models (using random forest as an example)

Go back to [Contents](#contents).



### Django

Django (https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design. 

It's known for its robustness and is designed to help developers take applications from concept to completion as quickly as possible.

Key features of Django include:

1. **MTV Architecture:** Similar to the MVC framework, it uses a Model-Template-View architecture.
2. **ORM (Object-Relational Mapping):** Allows you to interact with your database using Python code instead of SQL.
3. **Admin Interface:** Automatically generated and highly customizable admin interface for your models.
4. **Scalability:** Suitable for both small-scale applications and large-scale websites.
5. **Security:** Emphasizes security and helps developers avoid common security mistakes.
6. **Versatile:** Can be used for almost any type of website.
7. **Extensible:** Can be extended with plug-ins available in the Django ecosystem.

Go back to [Contents](#contents).



#### Steps to install and use the Django library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Django (if it is not installed)

```bash
pip install django
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Django Examples


**Example 1:** Setting Up a Django Project

```shell
# First, install Django using pip
pip install django

# Create a new Django project
django-admin startproject myproject
```

Go back to [Contents](#contents).


**Example 2:** Running the Development Server

```shell
# Change into the project directory
cd myproject

# Run the Django development server
python manage.py runserver
```

Go back to [Contents](#contents).


**Example 3:** Creating an App

```shell
# Inside the Django project directory
python manage.py startapp myapp
```

Go back to [Contents](#contents).


**Example 4:** Defining a Model

```python
# In myapp/models.py

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

Go back to [Contents](#contents).


**Example 5:** Creating Database Tables for Models

```shell
# First, make migrations for the app
python manage.py makemigrations myapp

# Then, apply the migrations to the database
python manage.py migrate
```

Go back to [Contents](#contents).


**Example 6:** Using Django Admin

```python
# In myapp/admin.py

from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

Go back to [Contents](#contents).


**Example 7:** Writing a View

```python
# In myapp/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
```

Go back to [Contents](#contents).


**Example 8:** Configuring URLs

```python
# In myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Go back to [Contents](#contents).


**Example 9:** Creating Templates

```python
<!-- In myapp/templates/myapp/index.html -->

<html>
    <body>
        <h1>Hello, world!</h1>
    </body>
</html>
```

Go back to [Contents](#contents).


**Example 10:** Handling Static Files

```python
<!-- In your template -->

<link href="{% static 'css/style.css' %}" rel="stylesheet">
```

Go back to [Contents](#contents).


**Example 11:** Form Handling

```python
# In myapp/forms.py

from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
```

Go back to [Contents](#contents).


**Example 12:** User Authentication

```python
# Using Django's built-in user authentication system
from django.contrib.auth.models import User

# Creating a new user
user = User.objects.create_user('username', 'email@example.com', 'password')
```

Go back to [Contents](#contents).



#### Some examples of Django projects are available on my GitHub account

My GitHub repository has some publicly available Django projects.

[Titanic survival predictor using Django and Machine Learning](https://github.com/ramonfigueiredo/titanic_survival_predictor_using_django_and_ml)
- Use Django, DjangoRESTFramework, Pandas, and Scikit-Learn to predict whether a passenger (with characteristics as your input) can survive the Titanic drowning or not!

[Django REST API - CRUD - supermarket application](https://github.com/ramonfigueiredo/django_rest_api-CRUD_supermarket_application)
- Use Django and Django REST Framework to create supermarket application

Go back to [Contents](#contents).



### Pillow

Pillow (https://pillow.readthedocs.io/) is the friendly fork of the Python Imaging Library (PIL). 

It is an open-source library that adds support for opening, manipulating, and saving many different image file formats in Python. 

Pillow is widely used for basic image processing tasks such as reading and writing images, image transformations, color manipulations, adding text, and applying filters.

Key features of Pillow include:

1. **Extensive File Format Support:** Supports an extensive range of image file formats, including JPEG, PNG, BMP, GIF, and many others.
2. **Image Processing:** Offers basic image processing capabilities like cropping, resizing, rotating, and more.
3. **Image Enhancement:** Provides tools for image enhancement, like adjusting contrast, brightness, and sharpness.
4. **Drawing:** Ability to draw on images using simple drawing tools.
5. **Filters:** Supports built-in filters like blurring, contouring, edge enhancement, etc.
6. **Color Transformations:** Offers color space transformations.
7. **Efficient and Easy to Use:** Designed to be efficient and straightforward for basic image manipulation tasks.


Go back to [Contents](#contents).



#### Steps to install and use the Pillow library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Pillow (if it is not installed)

```bash
pip install pillow
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Pillow Examples


**Example 1:** Opening and Saving Images

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

# Save the image in a different format
image.save('images/pillow-RFP_YouTube_Profile_Picture-copy.png')
```

Saved image:

![Pillow - Example 1 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-copy.png)

Go back to [Contents](#contents).


**Example 2:** Creating Thumbnails

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

image.thumbnail((100, 100))
image.save('images/pillow-RFP_YouTube_Profile_Picture-thumbnail.png')
```

Saved image:

![Pillow - Example 2 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-thumbnail.png)

Go back to [Contents](#contents).


**Example 3:** Cropping Images

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

# Cropping an image
cropped_image = image.crop((0, 0, 300, 300))
cropped_image.save('images/pillow-RFP_YouTube_Profile_Picture-cropped_image.png')
```

Saved image:

![Pillow - Example 3 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-cropped_image.png)

Go back to [Contents](#contents).


**Example 4:** Rotating and Flipping

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

# Rotate an image
rotated_image = image.rotate(90)
rotated_image.save('images/pillow-RFP_YouTube_Profile_Picture-rotated_image.png')

# Flip the image
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
flipped_image.save('images/pillow-RFP_YouTube_Profile_Picture-flipped_image.png')
```

Saved images:

a) Rotated image

![Pillow - Example 4 - Output rotated image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-rotated_image.png)

b) Flipped image

![Pillow - Example 4 - Output flipped image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-flipped_image.png)

Go back to [Contents](#contents).


**Example 5:** Applying Filters

```python
from PIL import Image, ImageFilter

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

# Apply a blur filter
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('images/pillow-RFP_YouTube_Profile_Picture-blurred_image.png')
```

Saved image:

![Pillow - Example 5 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-blurred_image.png)

Go back to [Contents](#contents).


**Example 6:** Adjusting Image Brightness

```python
from PIL import Image, ImageEnhance

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

enhancer = ImageEnhance.Brightness(image)
brightened_image = enhancer.enhance(2)  # Increase brightness
brightened_image.save('images/pillow-RFP_YouTube_Profile_Picture-brightened_image.png')
```

Saved image:

![Pillow - Example 6 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-brightened_image.png)

Go back to [Contents](#contents).


**Example 7:** Drawing Shapes and Text

```python
from PIL import Image, ImageDraw

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

draw = ImageDraw.Draw(image)
draw.rectangle(((100, 100), (200, 200)), fill="black")
draw.text((150, 150), "Hello", fill="white")
image.save('images/pillow-RFP_YouTube_Profile_Picture-rectangle_and_text_image.png')
```

Saved image:

![Pillow - Example 7 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-rectangle_and_text_image.png)

Go back to [Contents](#contents).


**Example 8:** Converting Images to Black and White

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

bw_image = image.convert('L')
bw_image.save('images/pillow-RFP_YouTube_Profile_Picture-black_white_image.png')
```

Saved image:

![Pillow - Example 8 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-black_white_image.png)

Go back to [Contents](#contents).


**Example 9:** Resizing Images

```python
from PIL import Image

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

resized_image = image.resize((200, 200))
resized_image.save('images/pillow-RFP_YouTube_Profile_Picture-resized_image.png')
```

Saved image:

![Pillow - Example 9 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-resized_image.png)

Go back to [Contents](#contents).


**Example 10:** Merging Images

```python
from PIL import Image, ImageChops

# Open an image
image = Image.open('images/RFP_YouTube_Profile_Picture.png')

# Flip the image
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

merged_image = ImageChops.add(image, flipped_image)
merged_image.save('images/pillow-RFP_YouTube_Profile_Picture-merged_image.png')
```

Saved image:

![Pillow - Example 10 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/pillow-RFP_YouTube_Profile_Picture-merged_image.png)

Go back to [Contents](#contents).



### Some Python Libraries for Artificial Intelligence - AI

Python offers a wide range of libraries for Artificial Intelligence (AI), each tailored to specific aspects of AI like machine learning, deep learning, natural language processing, computer vision and more.

Here are some of the most popular Python libraries for AI:

1. **[OpenCV](https://opencv.org/):** 
   - Open Source Computer Vision Library for image and video processing tasks.

2. **[NLTK (Natural Language Toolkit)](https://www.nltk.org/):** 
   - Library for natural language processing (NLP) tasks such as tokenization, stemming, tagging, parsing, and semantic reasoning.

3. **[Scikit-Learn](https://scikit-learn.org/):** 
   -  Simple and efficient tools for data mining and data analysis, including various machine learning algorithms and utilities for model evaluation and data preprocessing.

4. **[TensorFlow](https://www.tensorflow.org/):** 
   - Open-source machine learning framework for building and deploying machine learning models, developed by Google Brain team.

5. **[Keras](https://keras.io/):** 
   - High-level neural networks API, written in Python and capable of running on top of TensorFlow, Theano, or Microsoft Cognitive Toolkit (CNTK).

6. **[PyTorch](https://pytorch.org/):** 
   - Open-source deep learning framework developed by Facebook's AI Research lab, known for its dynamic computation graph and easy-to-use API.

7. **[Gensim](https://radimrehurek.com/gensim/):** 
   - Library for topic modeling, document similarity analysis, and other natural language processing tasks, particularly focusing on unsupervised algorithms.
   
8. **[OpenAI](https://openai.com/):** 
   - Research laboratory focusing on artificial intelligence, known for developing cutting-edge AI models and applications.

9. **[LangChain](https://www.langchain.com/):** 
   - A library for natural language understanding and processing tasks, including text generation, translation, summarization, and more.

10. **[MediaPipe](https://github.com/google/mediapipe):** 
    - A cross-platform framework for building multimodal applied ML pipelines, including perception (hand, face, pose detection), media (video, audio) understanding, and 3D perception.
    - https://developers.google.com/mediapipe

11. **[Detectron2](https://detectron2.readthedocs.io/):** 
    - High-performance object detection library built on PyTorch, offering state-of-the-art object detection algorithms and models.
    - https://ai.meta.com/tools/detectron2/

12. **[TF-Graphics](https://www.tensorflow.org/graphics/overview):** 
    - A TensorFlow library for creating and manipulating 3D structures and images, particularly useful for graphics and image generation tasks.

13. **[PyTorch3D](https://pytorch3d.org/):** 
    - A library built on PyTorch for 3D computer vision tasks, including rendering, mesh processing, and differentiable rendering.

14. **[Keras-GAN](https://keras.io/examples/generative/conditional_gan/):** 
    - A collection of generative adversarial network (GAN) implementations using Keras and TensorFlow, useful for generating realistic images and videos based on a given dataset.

15. **[DALL-E](https://github.com/openai/DALL-E):** 
    - A deep learning model developed by OpenAI that generates images from textual descriptions, suitable for creating diverse and creative visuals based on textual prompts.

These libraries offer a wide range of tools and functionalities for developing AI applications, spanning computer vision, natural language processing, generative modeling, and more.

Go back to [Contents](#contents).



#### Check out my Machine Learning and Deep Learning courses

- ML 101: Introduction to Machine Learning and Deep Learning - YouTube Video
  - https://www.youtube.com/watch?v=E3onjLGGBxk
- Course: ML and DL - Practical code examples - YouTube Playlist
  - https://www.youtube.com/playlist?list=PLZjc37fQX2kVbZcc8iwm61lJW9fubDEtd
- Machine Learning in Python - GitHub Repository
  - https://github.com/ramonfigueiredo/machine_learning_in_python

Go back to [Contents](#contents).



### OpenCV

OpenCV (Open Source Computer Vision Library, https://pypi.org/project/opencv-python/, https://opencv.org/) is an open-source computer vision and machine learning software library. 

It was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in commercial products. 

OpenCV supports a wide variety of programming languages including Python, and it can run on various operating systems.

Key features of OpenCV include:

1. **Image Processing:** Functions for image capture, manipulation, and analysis.
2. **Object Detection:** Detect and recognize faces, identify objects, classify human actions, track moving objects, and more.
3. **Feature Detection and Description:** Find meaningful features in images.
4. **Video Analysis:** Includes methods for motion analysis and object tracking.
5. **Camera Calibration and 3D Reconstruction:** Calibrate cameras and turn 2D images into 3D models.
6. **Machine Learning:** Integrated with the state-of-the-art machine learning framework.
7. **Optimization Algorithms:** Algorithms for image optimization and reconstruction.

Go back to [Contents](#contents).



#### Steps to install and use the OpenCV library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install OpenCV (if it is not installed)

```bash
pip install opencv-python
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### OpenCV Examples


**Example 1:** Reading and Displaying an Image

```python
import cv2

# Load an image
img = cv2.imread('images/RFP_YouTube_Profile_Picture.png')

# Display the image
cv2.imshow('image', img)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 1 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-input_image.png)

Go back to [Contents](#contents).


**Example 2:** Converting an Image to Grayscale

```python
import cv2

# Load an image
img = cv2.imread('images/RFP_YouTube_Profile_Picture.png')

# Converting an Image to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the image
cv2.imshow('gray image', gray_img)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 2 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-gray_image.png)

Go back to [Contents](#contents).


**Example 3:** Saving an Image

```python
import cv2

# Load an image
img = cv2.imread('images/RFP_YouTube_Profile_Picture.png')

# Converting an Image to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the image
cv2.imwrite('images/opencv-RFP_YouTube_Profile_Picture-gray_image_saved_image.png', gray_img)

# Display the image
cv2.imshow('gray image', gray_img)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 3 - Saved image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-gray_image_saved_image.png)

Go back to [Contents](#contents).


**Example 4:** Resizing an Image

```python
import cv2

# Load an image
img = cv2.imread('images/RFP_YouTube_Profile_Picture.png')

# Resize image
resized_img = cv2.resize(img, (100, 100))

# Show resized image
cv2.imshow('Resized Image', resized_img)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 4 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-resized_image.png)

Go back to [Contents](#contents).


**Example 5:** Edge Detection

```python
import cv2

# Load an image
img = cv2.imread('images/RFP_YouTube_Profile_Picture.png')

# Find edges using the Canny algorithm
edges = cv2.Canny(img, 100, 200)

# Show Edge Image
cv2.imshow('Edges', edges)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 5 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-canny_edges.png)

Go back to [Contents](#contents).


**Example 6:** Face Detection in an Image

```python
import cv2

# Load an image
img = cv2.imread('images/albert_einstein.png')

# Converting an Image to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('Face Detected', img)

# Press any key to continue
cv2.waitKey(0)

# Destroy and close all windows
cv2.destroyAllWindows()
```

Saved image:

![OpenCV - Example 6 - Output image](https://github.com/ramonfigueiredo/python_course/blob/main/images/opencv-RFP_YouTube_Profile_Picture-face_detection.png)

Go back to [Contents](#contents).


**Example 7:** Capturing Video from Camera

```python
import cv2

# Get access to the webcam
cap = cv2.VideoCapture(0)

while True:
    # Get video frame
    ret, frame = cap.read()

    # Show video frame
    cv2.imshow('Video', frame)

    # Press the q key to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release video
cap.release()

# Destroy and close all windows
cv2.destroyAllWindows()
```

**Note:** Try the code above with a laptop or a computer that has access to a webcam or other type of input camera.

Go back to [Contents](#contents).


**Example 8:** Read a Video File and Display Its Frames

```python
import cv2

# Path to the video file
video_path = 'videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
else:
    # Read and display frames in a loop
    while True:
        # Read a frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the frame
        cv2.imshow('Frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

# Release the VideoCapture object and close display window
cap.release()
cv2.destroyAllWindows()
```

Input video:

![OpenCV - Example 8 - Input video](https://github.com/ramonfigueiredo/python_course/blob/main/videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.gif)

Go back to [Contents](#contents).


**Example 9:** Read a Video, Apply the Algorithm Canny, and Save the Output Video

```python
import cv2

# Specify the path of the input video
input_video_path = 'videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.mp4'

# Open the input video
cap = cv2.VideoCapture(input_video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Determine the input video's frame size and frame rate to configure the output video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create a VideoWriter object to write the output video in MP4 format
output_video_path = 'videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel_canny_edges.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for the output video
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height), isColor=False) # Set isColor to False for grayscale output

while True:
    # Read a frame from the input video
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Reached the end of the video or error in reading video frame.")
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200) # These thresholds can be adjusted

    # Write the frame with Canny edge detection applied into the output video file
    out.write(edges)

# Release everything if job is finished
cap.release()
out.release()
print("The video was successfully saved as", output_video_path)
```

Input video:

![OpenCV - Example 9 - Input video](https://github.com/ramonfigueiredo/python_course/blob/main/videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.gif)

Output video:

![OpenCV - Example 9 - Output video - Applying the Canny Algorithm](https://github.com/ramonfigueiredo/python_course/blob/main/videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel_canny_edges.gif)

Go back to [Contents](#contents).


**Example 10:** Create an Output Video with the Histogram of Each Frame of the Input Video

```python
import cv2
import numpy as np

# Path to the video file
video_path = 'videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Determine the video's original frame size and frame rate
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter objects
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_histogram = cv2.VideoWriter('videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel-histogram_video.mp4',
                                fourcc, fps,
                                (256, 300))  # Assuming histogram image size of 256x300

while True:
    # Read a frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert the frame to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate the histogram of the grayscale image
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    # Normalize the histogram
    hist = cv2.normalize(hist, hist).flatten()

    # Create an image to display the histogram
    hist_img = np.zeros((300, 256, 3), dtype=np.uint8)

    # Scale the histogram to fit in the display image
    hist_height = hist_img.shape[0]
    max_val = np.max(hist)
    for x in range(256):
        pt1 = (x, hist_height)
        pt2 = (x, hist_height - int((hist[x] / max_val) * hist_height))
        cv2.line(hist_img, pt1, pt2, (255, 255, 255))

    # Write the histogram image to their respective video frame
    out_histogram.write(hist_img)

# Release everything if job is finished
cap.release()
out_histogram.release()
print("Videos have been successfully saved.")
```

Input video:

![OpenCV - Example 9 - Input video](https://github.com/ramonfigueiredo/python_course/blob/main/videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel.gif)

Output video:

![OpenCV - Example 9 - Output video - Histogram](https://github.com/ramonfigueiredo/python_course/blob/main/videos/thank_you_for_watch_and_subscribe_in_ramon_figueiredo_youtube_channel-histogram_video.gif)

Go back to [Contents](#contents).

#### Converting MP4 video to GIF using FFmpeg

To convert all MP4 videos in a folder to GIF files using [FFmpeg](https://ffmpeg.org/), you can use a command line loop. 

Below, I provide examples for both Windows and Unix-based systems (like Linux and macOS).

**For Unix-based Systems (Linux/macOS):**

```shell
for f in *.mp4; do ffmpeg -i "$f" -vf "fps=10,scale=320:-1:flags=lanczos" "${f%.mp4}.gif"; done
```

This command does the following:

- Loops through each MP4 file in the current directory.
- Uses FFmpeg to convert the video to a GIF. The `-vf "fps=10,scale=320:-1:flags=lanczos"` part of the command sets the frames per second to 10 and scales the output GIF to a width of 320 pixels (maintaining aspect ratio). The `lanczos` flag specifies a high-quality downsampling filter.
- Saves the output GIF with the same name as the input MP4 file, but with a `.gif` extension.

#### For Windows

```shell
FOR %G IN (*.mp4) DO ffmpeg -i "%G" -vf "fps=10,scale=320:-1:flags=lanczos" "%~nG.gif"
```

This command works similarly to the Unix-based version but is adapted for Windows command-line syntax:

- `FOR %G IN (*.mp4) DO` iterates over each MP4 file in the current directory.
- `ffmpeg -i "%G"` calls FFmpeg for each file.
- The `-vf` option and its arguments specify the video filters for FPS, scaling, and the resampling algorithm.
- `%~nG.gif` specifies the output filename by stripping the original extension and appending .gif instead.

Go back to [Contents](#contents).



### NLTK

NLTK, or the Natural Language Toolkit (https://www.nltk.org/), is a leading platform for building Python programs to work with human language data. 

It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.

Key features of NLTK include:

1. **Corpora:** Access to a variety of textual corpora, including well-known ones like Gutenberg, WordNet, and movie reviews.
2. **Text Processing Libraries:** Tools for various linguistic tasks like tokenization, part-of-speech tagging, and parsing.
3. **Classification:** Functions for text classification, including sentiment analysis.
4. **Stemming and Lemmatization:** Reducing words to their base or root form.
5. **Frequency Distributions:** Analyzing the frequency distribution of words in a text.
6. **NLP Pipelines:** Building complete natural language processing pipelines.

Go back to [Contents](#contents).



#### Steps to install and use the NLTK library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install NLTK (if it is not installed)

```bash
pip install nltk
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### NLTK Examples


**Example 1:** Tokenizing Text

```python
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text = "Hello, welcome to the world of NLTK!"
tokens = word_tokenize(text)
print(tokens)
```

Go back to [Contents](#contents).


**Example 2:** Stopwords Removal

```python
nltk.download('stopwords')
from nltk.corpus import stopwords

filtered_words = [word for word in tokens if word not in stopwords.words('english')]
print(filtered_words)
```

Go back to [Contents](#contents).


**Example 3:** Part-of-Speech Tagging

```python
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag

tagged = pos_tag(tokens)
print(tagged)
```

Go back to [Contents](#contents).


**Example 4:** Stemming Words

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in tokens]
print(stems)
```

Go back to [Contents](#contents).


**Example 5:** Lemmatizing Words

```python
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]
print(lemmas)
```

Go back to [Contents](#contents).


**Example 6:** Named Entity Recognition

```python
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk import ne_chunk

tagged = pos_tag(word_tokenize("Mark and John are working at Google."))
entities = ne_chunk(tagged)
print(entities)
```

Go back to [Contents](#contents).


**Example 7:** Parsing Sentence Structure

```python
from nltk import CFG

grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    V -> "saw" | "ate"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park"
    PP -> P NP
    P -> "in" | "on" | "by" | "with"
""")
```

Go back to [Contents](#contents).


**Example 8:** Frequency Distribution of Words

```python
from nltk.probability import FreqDist

fdist = FreqDist(tokens)
print(fdist.most_common(3))
```

Go back to [Contents](#contents).


**Example 9:** Sentiment Analysis

```python
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores("I love NLTK. It's amazing!")
print(sentiment)
```

Go back to [Contents](#contents).


**Example 10:** Chunking

```python
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
"""
cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged)
print(result)
```

Go back to [Contents](#contents).


### Scikit-Learn

Scikit-Learn (https://scikit-learn.org/), often referred to as sklearn, is a popular Python library for machine learning. 

It provides a range of supervised and unsupervised learning algorithms via a consistent interface. 

This library, built on NumPy, SciPy, and Matplotlib, is known for its ease of use and flexibility.

Key features of Scikit-Learn include:

1. **Classification:** Identifying which category an object belongs to.
2. **Regression:** Predicting a continuous-valued attribute associated with an object.
3. **Clustering:** Automatic grouping of similar objects into sets.
4. **Dimensionality Reduction:** Reducing the number of random variables to consider.
5. **Model Selection:** Comparing, validating, and choosing parameters and models.
6. **Preprocessing:** Feature extraction and normalization.

Go back to [Contents](#contents).



#### Steps to install and use the Scikit-Learn library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Scikit-Learn (if it is not installed)

```bash
pip install scikit-learn
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Scikit-Learn Examples


**Example 1:** Loading a Dataset

```python
from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()
```

Go back to [Contents](#contents).


**Example 2:** Splitting Data into Training and Test Sets

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5)
```

Go back to [Contents](#contents).


**Example 3:** Training a Classification Model

```python
from sklearn import svm

clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(X_train, y_train)
```

Go back to [Contents](#contents).


**Example 4:** Making Predictions

```python
predicted = clf.predict(X_test)
print(predicted)
```

Go back to [Contents](#contents).


**Example 5:** Evaluating Model Accuracy

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predicted)
print(accuracy)
```

Go back to [Contents](#contents).


**Example 6:** Using a Pipeline

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

pipe = make_pipeline(StandardScaler(), svm.SVC(gamma='auto'))
pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

Go back to [Contents](#contents).


**Example 7:** K-Means Clustering

```python
from sklearn.cluster import KMeans

k_means = KMeans(n_clusters=3)
k_means.fit(iris.data)
print(k_means.labels_)
```

Go back to [Contents](#contents).


**Example 8:** Principal Component Analysis (PCA)

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit_transform(iris.data)
```

Go back to [Contents](#contents).


**Example 9:** Decision Trees

```python
from sklearn.tree import DecisionTreeClassifier

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, y_train)
tree.score(X_test, y_test)
```

Go back to [Contents](#contents).


**Example 10:** Random Forest Classifier

```python
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=100, random_state=0)
forest.fit(X_train, y_train)
forest.score(X_test, y_test)
```

Go back to [Contents](#contents)


**Example 11:** Cross-Validation

```python
from sklearn.model_selection import cross_val_score

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
```

Go back to [Contents](#contents)


**Example 12:** Grid Search for Parameter Tuning

```python
from sklearn.model_selection import cross_val_score

clf = svm.SVC(kernel='linear', C=1)
scores = cross_val_score(clf, iris.data, iris.target, cv=5)
print(scores)
```

Go back to [Contents](#contents)



### TensorFlow

TensorFlow (https://www.tensorflow.org/) is an open-source machine learning library developed by the Google Brain team. 

It's widely used for deep learning or neural network tasks and is well-regarded for its flexibility and capability to handle large-scale, complex computations. 

TensorFlow allows developers to create dataflow graphs – structures that show how data moves through a graph, or a series of processing nodes. 

Each node in the graph represents a mathematical operation, and each connection or edge between nodes is a multidimensional data array, or tensor.

Key features of TensorFlow include:

1. **High Performance:** Optimized for speed and performance, crucial for large-scale neural networks.
2. **Scalability:** Capable of running on both CPUs and GPUs, and even on distributed computing systems.
3. **Flexibility:** Offers both high-level and low-level APIs for building and training models.
4. **Visualization:** Integrated with TensorBoard for visualization of neural network training and performance.
5. **Automatic Differentiation:** Provides automatic differentiation capabilities to compute gradients.
6. **Large Community:** Strong community support with many resources for learning and troubleshooting.

Go back to [Contents](#contents).



#### Steps to install and use the TensorFlow library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install TensorFlow (if it is not installed)

```bash
pip install tensorflow
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### TensorFlow Examples


**Example 1:** Basic Operations

```python
import tensorflow as tf

# Constant tensors
tensor1 = tf.constant([[1, 2], [3, 4]])
tensor2 = tf.constant([[5, 6], [7, 8]])

# Basic operations
result = tf.add(tensor1, tensor2)
print(result)
```

Go back to [Contents](#contents)


**Example 2:** Linear Regression

```python
# Placeholder tensors for input and output
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# Model parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

# Linear model
linear_model = W * X + b

# Loss function
squared_delta = tf.square(linear_model - Y)
loss = tf.reduce_sum(squared_delta)

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
```

Go back to [Contents](#contents)


**Example 3:** Creating and Running a Session

```python
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Run a session to evaluate the output
print(sess.run(result))
sess.close()
```

Go back to [Contents](#contents)


**Example 4:** Building a Simple Neural Network

```python
from tensorflow.keras import layers

# Build a simple neural network with one dense layer
model = tf.keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(32,)),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

Go back to [Contents](#contents)


**Example 5:** Training and Evaluating Models

```python
# Dummy data
data = tf.random.normal([1000, 32])
labels = tf.random.normal([1000, 10])

# Training the model
model.fit(data, labels, epochs=10, batch_size=32)

# Evaluating the model
model.evaluate(data, labels, batch_size=32)
```

Go back to [Contents](#contents)


**Example 6:** Image Classification with CNNs

```python
# Convolutional Neural Network for image classification
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

Go back to [Contents](#contents)


**Example 7:** Saving and Loading Models

```python
# Save a model
model.save('my_model.h5')

# Load a model
new_model = tf.keras.models.load_model('my_model.h5')
```

Go back to [Contents](#contents)


**Example 8:** Data Augmentation

```python
datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')
```

Go back to [Contents](#contents)


**Example 9:** Text Generation with RNNs

```python
# Text generation with a Recurrent Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(tokenizer.vocab_size, 64),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

Go back to [Contents](#contents)


**Example 10:** Transfer Learning

```python
base_model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3),
                                               include_top=False,
                                               weights='imagenet')
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
prediction_layer = tf.keras.layers.Dense(1)

model = tf.keras.Sequential([
  base_model,
  global_average_layer,
  prediction_layer
```

Go back to [Contents](#contents)


### Keras

Keras (https://keras.io/) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. 

It was developed with a focus on enabling fast experimentation. 

Being able to go from idea to result as fast as possible is key to doing good research.

Key features of Keras include:

1. **User-Friendly:** Keras has a simple, consistent interface optimized for common use cases.
2. **Modular and Composable:** Keras models are made by connecting configurable building blocks together with few restrictions.
3. **Easy to Extend:** Write custom building blocks to express new ideas for research.
4. **Works with Python:** No separate models configuration files in a declarative format. Models are described in Python code.

Go back to [Contents](#contents).



#### Steps to install and use the Keras library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install Keras (if it is not installed)

```bash
pip install keras
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### Keras Examples


**Example 1:** Sequential Model

```python
from keras.models import Sequential
from keras.layers import Dense

# Define a Sequential model
model = Sequential([
    Dense(32, input_shape=(784,), activation='relu'),
    Dense(10, activation='softmax')
])
```

Go back to [Contents](#contents).


**Example 2:** Compiling the Model

```python
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

Go back to [Contents](#contents).


**Example 3:** Model Training

```python
import numpy as np

# Dummy data
data = np.random.random((1000, 784))
labels = np.random.random((1000, 10))

# Train the model
model.fit(data, labels, epochs=10, batch_size=32)
```

Go back to [Contents](#contents).


**Example 4:** Model Evaluation

```python
# Dummy test data
test_data = np.random.random((100, 784))
test_labels = np.random.random((100, 10))

# Evaluate the model
score = model.evaluate(test_data, test_labels, batch_size=32)
```

Go back to [Contents](#contents).


**Example 5:** Model Prediction

```python
predictions = model.predict(test_data, batch_size=128)
print(predictions)
```

Go back to [Contents](#contents).


**Example 6:** Functional API for Complex Models

```python
from keras.layers import Input, Dense
from keras.models import Model

# Define a Functional API model
inputs = Input(shape=(784,))
x = Dense(64, activation='relu')(inputs)
predictions = Dense(10, activation='softmax')(x)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```

Go back to [Contents](#contents).


**Example 7:** Saving and Loading a Model

```python
# Save a model
model.save('my_model.h5')

# Load a model
from keras.models import load_model
model = load_model('my_model.h5')
```

Go back to [Contents](#contents).


**Example 8:** Using Pretrained Models

```python
from keras.applications import VGG16

# Load VGG16 model pre-trained on ImageNet
model = VGG16(weights='imagenet', include_top=False)
```

Go back to [Contents](#contents).


**Example 9:** Callbacks

```python
from keras.callbacks import EarlyStopping

# Early stopping callback
early_stopping = EarlyStopping(monitor='val_loss', patience=2)

# Train the model with the callback
model.fit(data, labels, validation_split=0.2, callbacks=[early_stopping])
```

Go back to [Contents](#contents).


**Example 10:** CNN with Keras

```python
from keras.layers import Conv2D, MaxPooling2D, Flatten

# Create a CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))
```

Go back to [Contents](#contents).


### PyTorch

PyTorch (https://pytorch.org/) is an open-source machine learning library developed by Facebook's AI Research lab. 

It is widely used for applications such as computer vision and natural language processing. 

PyTorch is known for its ease of use, flexibility, and dynamic computational graph, which allows changes to be made on-the-fly during processing.

Key features of PyTorch include:

**Tensor Computing:** Similar to NumPy, but with strong GPU acceleration.
**Dynamic Computational Graph:** Known as Autograd, this feature provides automatic differentiation for all operations on tensors.
**Deep Neural Networks:** Built-in support for creating deep neural networks.
**Modular and Versatile:** Easy to use with other Python libraries and for various machine learning tasks.
**Customizable and Extendable:** Create and extend neural network modules to suit complex architectures.
**Community and Ecosystem:** Strong community support with a wide range of tools and libraries.

Go back to [Contents](#contents).



#### Steps to install and use the PyTorch library

* Create a virtual environment (if it doesn't exist)
  * You can give any name for your virtual folder. Replace `venv` folder name with any name you want.
```bash
virtualenv -p python3 venv
```

* Activate the virtual environment
```bash
source venv/bin/activate
```

* Upgrade pip (if necessary)

```bash
pip install --upgrade pip
```

* Install PyTorch (if it is not installed)

```bash
pip install torch
```

* List the virtual environment packages (if you want to list the packages)

```bash
pip list
```

* Create the Python script

* Run the Python script
  * Note: Replace `main.py` with the correct Python script name.

```bash
python main.py
```

* To deactivate the virtual environment, type:

```bash
deactivate
```

Go back to [Contents](#contents).



#### PyTorch Examples


**Example 1:** Basic Tensor Operations

```python
import torch

# Create a tensor
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Basic operations
z = x + y
print(z)
```

Go back to [Contents](#contents).


**Example 2:** Tensor Reshaping

```python
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())
```

Go back to [Contents](#contents).


**Example 3:** Computing Gradients (Autograd)

```python
x = torch.ones(2, 2, requires_grad=True)
y = x + 2
z = y * y * 3
out = z.mean()

# Compute gradients
out.backward()
print(x.grad)
```

Go back to [Contents](#contents).


**Example 4:** Creating a Simple Neural Network

```python
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Define layers
        self.fc1 = nn.Linear(3, 3)
        self.fc2 = nn.Linear(3, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

net = Net()
print(net)
```

Go back to [Contents](#contents).


**Example 5:** Training a Model

```python
import torch.optim as optim

# Create a simple dataset
X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
Y = torch.tensor([[0.0], [1.0]])

# Define a loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Training loop
for epoch in range(500):
    optimizer.zero_grad()
    outputs = net(X)
    loss = criterion(outputs, Y)
    loss.backward()
    optimizer.step()
```

Go back to [Contents](#contents).


**Example 6:** Saving and Loading Models

```python
# Save the model
torch.save(net.state_dict(), 'model.pth')

# Load the model
model = Net()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

Go back to [Contents](#contents).


**Example 7:** Working with Pretrained Models

```python
# Load a pretrained ResNet model
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True)
```

Go back to [Contents](#contents).


**Example 8:** Image Classification

```python
from torchvision import transforms

# Preprocess the image
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# An example PIL image
img = Image.open("path/to/image.jpg")
img_t = transform(img)
batch_t = torch.unsqueeze(img_t, 0)

# Inferencing
model.eval()
out = model(batch_t)
print(out)
```

Go back to [Contents](#contents).


**Example 9:** Image Segmentation

```python
# Example for semantic segmentation
model = torch.hub.load('pytorch/vision:v0.6.0', 'fcn_resnet101', pretrained=True)
model.eval()
out = model(batch_t)
print(out)
```

Go back to [Contents](#contents).


**Example 10:** Working with Text Data

```python
# Example of embedding layer for text data
embedding = nn.Embedding(10, 3)
input = torch.LongTensor([[1,2,4,5],[4,3,2,9]])
output = embedding(input)
```

Go back to [Contents](#contents)



### Gensim

Go back to [Contents](#contents)



#### Steps to install and use the Gensim library

Go back to [Contents](#contents)



#### Gensim Examples

Go back to [Contents](#contents)



### OpenAI

Go back to [Contents](#contents)



#### Steps to install and use the OpenAI library

Go back to [Contents](#contents)



#### OpenAI Examples

Go back to [Contents](#contents)



### LangChain

Go back to [Contents](#contents)



#### Steps to install and use the LangChain library

Go back to [Contents](#contents)



#### LangChain Examples

Go back to [Contents](#contents)



### MediaPipe

Go back to [Contents](#contents)



#### Steps to install and use the MediaPipe library

Go back to [Contents](#contents)



#### MediaPipe Examples

Go back to [Contents](#contents)



### Detectron2

Go back to [Contents](#contents)



#### Steps to install and use the Detectron2 library

Go back to [Contents](#contents)



#### Detectron2 Examples

Go back to [Contents](#contents)



### TF-Graphics

Go back to [Contents](#contents)



#### Steps to install and use the TF-Graphics library

Go back to [Contents](#contents)



#### TF-Graphics Examples

Go back to [Contents](#contents)



### PyTorch3D

Go back to [Contents](#contents)



#### Steps to install and use the PyTorch3D library

Go back to [Contents](#contents)



#### PyTorch3D Examples

Go back to [Contents](#contents)



### Keras-GAN

Go back to [Contents](#contents)



#### Steps to install and use the Keras-GAN library

Go back to [Contents](#contents)



#### Keras-GAN Examples

Go back to [Contents](#contents)



### DALL-E

Go back to [Contents](#contents)



#### Steps to install and use the DALL-E library

Go back to [Contents](#contents)



#### DALL-E Examples 

Go back to [Contents](#contents)



### How to publish your Python library on Python Package Index

To publish your Python library on PyPI (Python Package Index), follow these steps:

1. Prepare Your Package:
- Organize your code into a Python package. 
  - This typically involves creating a directory structure with your library code and adding a `setup.py` file to define metadata about your package.
- Ensure that your package includes a `__init__.py` file in each subdirectory to make it a Python package.

2. Create a `setup.py` File:
- This file contains information about your package, such as its name, version, description, and dependencies.

- Here's an example of a `setup.py` file:

```python
from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    description='A description of your package',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/your_username/your_package',
    install_requires=[
        'dependency1',
        'dependency2',
    ],
)
```

3. Build Your Package:

Run the following command in your package directory to build your package:

```shell
python setup.py sdist bdist_wheel
```

4. Register on PyPI:

- If you haven't already, create an account on PyPI (https://pypi.org/account/register/).
- Once registered, you need to create an API token for uploading packages. 
  - Go to https://pypi.org/manage/account/ and create a new API token.

5. Upload Your Package:

Use the `twine` tool to upload your package to PyPI. 

First, install `twine` if you haven't already:

```shell
pip install twine
```

Then, upload your package using the following command:

```shell
twine upload dist/*
```

6. Verify Your Package:

After uploading, your package should be available on PyPI. 

You can verify this by searching for your package on https://pypi.org/.

7. Installation:

Users can now install your package using `pip`:

```shell
pip install your_package_name
```

8. Update Your Package:

If you make changes to your package and want to update it on PyPI, increment the version number in your `setup.py` file and repeat steps 3-5.


By following these steps, you can successfully publish your Python library on [PyPI](https://pypi.org/), making it available for others to install and use via pip.

Go back to [Contents](#contents).


## Conclusion

Throughout this course, we've embarked on an extensive exploration of Python, starting from the very basics and advancing through to complex topics that touch on the forefronts of technology and innovation. 

We've delved into Python syntax, data structures, functions, file handling, and moved through to more advanced topics such as object-oriented programming, web development, data analysis, visualization, and even a glimpse into machine learning and AI.

We've seen how Python's simplicity and flexibility make it a powerful tool in the hands of developers, researchers, and data scientists alike. 

By now, you should have a solid foundation in Python and a toolkit that's ready to tackle real-world problems.

Go back to [Contents](#contents).



### Further Learning Resources

But remember, the journey of learning never truly ends. 

To continue growing your skills and knowledge, I encourage you to explore the following resources:

- **Official Python Documentation:** For a comprehensive understanding of Python's capabilities: https://docs.python.org/3/
- **GitHub Projects:** To see real-world applications and contribute to open-source projects.
- **Online Forums like Stack Overflow:** To engage with the community, ask questions, and find answers.
- **Continue Reading:** Books and articles that dive deeper into specific areas of interest.
- **Practice:** Work on personal projects, participate in coding challenges, and contribute to open-source software.

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