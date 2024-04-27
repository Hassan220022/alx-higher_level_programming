#!/usr/bin/python3
"""
Module to find a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None
    
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]

# Save this file as '6-peak.py'.
# '6-peak.txt' should contain the complexity of the algorithm, which is O(log(n)).
