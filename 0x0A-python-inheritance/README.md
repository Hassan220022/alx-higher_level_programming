# 0x0A. Python - Inheritance

In this project, I delve into the concept of inheritance in Python. We explore the hows and whys, look at superclass and subclass relationships, and learn to manage inherited attributes and methods.

## Description

Throughout this project, a series of tasks are presented that challenge us to think about inheritance in Python. From the creation of simple lookup functions to the development of a complete geometry system, this project covers a variety of inheritance concepts.

### Key Learning Objectives

By the end of this project, I have an understanding of:

- The principles of inheritance and how they apply to Python programming.
- The relationship between superclasses and subclasses.
- How to inherit one class from another and how to check inheritance relationships.
- How to list and manage attributes and methods of classes.
- The importance and application of `isinstance`, `issubclass`, `type`, and `super`.

### Resources

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Tasks

Each file in this repository corresponds to a task:

- **0-lookup.py**: Function that returns the list of available attributes and methods of an object.
- **1-my_list.py**: A class `MyList` that inherits from `list` with a method to print it sorted.
- **2-is_same_class.py**: Function that checks if an object is exactly an instance of a specified class.
- ...and more advanced tasks building up to a complete geometry module with class inheritance and method overriding.

## Usage

All scripts are executed on Ubuntu 20.04 LTS using `python3` (version 3.8.5). Here is an example of how to run the scripts:

```bash
./0-main.py
```

Output from the above script would be something similar to this:

```
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', ...]
```

## Author

Written by Hassan Mikawi, a student at ALX School.
