# 0x07. Python - Test-driven development

## Description

This project is focused on learning Test-driven development (TDD) in Python. The main goal is to understand why and how to apply TDD methodologies to write robust Python applications. By using documentation and doc-tests, we aim to ensure that each function not only performs its intended task but is also ready to handle edge cases and errors effectively.

## Table of Contents

- [Learning Objectives](#learning-objectives)
- [Technologies](#technologies)
- [Files and Tests](#files-and-tests)
- [Setup and Usage](#setup-and-usage)
- [Contributing](#contributing)

## Learning Objectives

By the end of this project, participants are expected to understand:

- Why Python programming is awesome
- The importance of tests in programming
- How to write effective docstrings to create tests
- The process and benefits of test-driven development
- How to find and handle edge cases in software development

## Technologies

- Language: Python 3.8.5
- OS: Ubuntu 20.04 LTS
- Style guidelines: Pycodestyle (version 2.8.\*)

## Files and Tests

- `0-add_integer.py`: Function that adds 2 integers.
  - **Usage**: `./0-main.py`
- `2-matrix_divided.py`: Function that divides all elements of a matrix.
  - **Usage**: `./2-main.py`
- `tests/`: Directory containing all test files.
  - **Execution**: `python3 -m doctest ./tests/*`

## Setup and Usage

1. **Clone the repository**:

   ```
   git clone https://github.com/Hassan220022/alx-higher_level_programming.git
   cd 0x07-python-test_driven_development
   ```

2. **Run the scripts**:
   - To run a script file, use:
     ```
     ./<script-name>
     ```
   - To check the tests using doctest:
     ```
     python3 -m doctest -v ./tests/<test-file>
     ```

## Contributing

This project is for educational purposes and is part of the curriculum of ALX. Contributions are welcome for educational enhancements but are not intended for project solution sharing.
