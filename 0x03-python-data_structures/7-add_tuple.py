#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extend the tuples to ensure they both have at least two elements
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # Calculate the sum of the first and second elements of the tuples
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Return a new tuple containing the sums
    return (sum_first, sum_second)
