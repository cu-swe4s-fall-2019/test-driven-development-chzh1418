import math
import argparse
import sys

# Define function to calculate the mean value of a list.


def list_mean(L):
    """Compute the mean of a non-empty array.

    Parameters
    --------
    L : list of numbers
        could be integers, float or both.

    Returns
    --------
    m
        Arithmetic mean of the values in L

    """
    # Check if input is a non-empty list
    if len(L) == 0:
        print('Empty input')
        return None

    if L is None:
        return None

    # Check if the list contains only numbers
    if (isinstance(L, list)):
        for i in L:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Input should be list of integers or floats')
                return None

    m = float(sum(L)) / float(len(L))
    return m
# Define function to calculate the standard deviation of a list of numbers.


def list_stdev(L):
    """Calculate the standard deviation of a non-empty array.

    Parameters
    --------
    L : List of numebrs
        could be integer, float or both.

    Returns
    --------
    stdev
        Arithmetic standard deviation of the values in L
    """
    # Check if input is a non-empty list
    if len(L) < 2:
        print('List is too short')
        return None

    if L is None:
        return None

    # Check if the list contains only numbers
    if (isinstance(L, list)):
        for i in L:
            if not (isinstance(i, int) or isinstance(i, float)):
                print('Input should be a list of integers or floats')
                return None
    mean = list_mean(L)
    stdev = math.sqrt(float(sum([(float(x) - mean)**2 for x in L])) /
                      (len(L) - 1))
    return stdev
