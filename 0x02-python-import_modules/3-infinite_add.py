#!/usr/bin/python3
import sys

# Function to add all arguments
def infinite_add():
    # Start with a total sum of 0
    total_sum = 0
    # Iterate over all arguments starting from the second one (skip the script name)
    for arg in sys.argv[1:]:
        # Add the integer value of each argument to the total sum
        total_sum += int(arg)
    # Print the total sum followed by a new line
    print(total_sum)

if __name__ == "__main__":
    infinite_add()
    