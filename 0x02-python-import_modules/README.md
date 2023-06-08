0x02. Python - import & modules

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Why Python programming is awesome
How to import functions from another file
How to use imported functions
How to create a module
How to use the built-in function dir()
How to prevent code in your script from being executed when imported
How to use command line arguments with your Python programs
General
Python is a programming language that is known for its simplicity, power, and flexibility. It is a great choice for beginners and experienced programmers alike.

One of the things that makes Python so powerful is its ability to import functions from other files. This allows you to reuse code and create modular programs.

To import a function from another file, you use the import keyword. For example, to import the print() function from the print.py file, you would use the following code:

import print

Once you have imported a function, you can use it like any other function in your program. For example, the following code will print the message "Hello, world!" to the console:

import print

print("Hello, world!")

Creating a module
A module is a file that contains Python code. Modules can be used to organize your code and make it easier to reuse.

To create a module, you simply create a file with the .py extension. For example, to create a module called my_module.py, you would create a new file in your current directory and save it as my_module.py.

Once you have created a module, you can import it into your other programs. For example, the following code imports the my_module module and prints the value of the variable variable:

import my_module

print(my_module.variable)

Using the dir() function
The dir() function is a built-in function that returns a list of the names of all the variables, functions, and classes in a module.

To use the dir() function, you simply pass the name of the module as an argument. For example, the following code will print a list of all the names in the my_module module:

import my_module

print(dir(my_module))

Preventing code from being executed when imported
If you do not want code in your script to be executed when it is imported, you can use the if __name__ == "__main__": statement.

The if __name__ == "__main__": statement is a special statement that is only executed when the script is run as a standalone program. If the script is imported into another program, the if __name__ == "__main__": statement will not be executed.

For example, the following code will only print the message "Hello, world!" if the script is run as a standalone program:

if name == "main":
print("Hello, world!")

Using command line arguments with your Python programs
You can use command line arguments to pass information to your Python programs. Command line arguments are the arguments that you type after the name of the program when you run it from the command line.

To access command line arguments in your Python program, you can use the sys.argv variable. The sys.argv variable is a list that contains all of the command line arguments that were passed to the program.

For example, the following code will print the value of the first command line argument:

import sys

print(sys.argv[1])

If you run the above code from the command line and pass the argument "Hello, world!", the program will print the message "Hello, world!".

Conclusion
In this project, you learned about the basics of importing and creating modules in Python. You also learned about the dir() function, the if __name__ == "__main__": statement, and how to use command line arguments with your Python programs.