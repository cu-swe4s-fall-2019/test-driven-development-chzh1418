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
    if L is None:
        return None

    if len(L) == 0:
        return None

    # Check if the list contains only numbers
    if (isinstance(L, list)):
        for i in L:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise ValueError('Unsupported value in list.')

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
    if L is None:
        return None

    if len(L) < 2:
        return None

    # Check if the list contains only numbers
    if (isinstance(L, list)):
        for i in L:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise ValueError('Unsupported value in list.')

    mean = list_mean(L)
    stdev = math.sqrt(float(sum([(float(x) - mean)**2 for x in L])) /
                      (len(L) - 1))
    return stdev
