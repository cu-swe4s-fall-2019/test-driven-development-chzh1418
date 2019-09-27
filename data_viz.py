import sys
import os.path
from os import path
import math_lib
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends import pylab_setup
# Different methods for data visualization


def boxplot(L, out_file_name):
    """ Boxplot of numerical array and give specified name
    Parameters
    --------
    L :  Numerical array
        Array contains list of integers or floats
    out_file_name : file name
        File name of the output file
    Returns
    --------
        Generate file with specified name containing boxplot
        , tile and labeled axist
    Raises
    --------
    NameError
        No output file name
    SystemExit
        File exits
    """
    # Check input
    if out_file_name is None:
        raise NameError('Out_file_name required')
    if path.exists(out_file_name):
        raise SystemExit('File already exits')

    plt.boxplot(L)
    plt.title(str('Mean: ' + str(math_lib.list_mean(L)) +
                  ' Stdev: ' + str(math_lib.list_stdev(L))))
    plt.xlabel('Box')
    plt.ylabel('Distribution')
    plt.savefig(out_file_name, dpi=300)
    pass


def histogram(L, out_file_name):
    """ Histogram of numerical array and give specified name
    Parameters
    --------
    L :  Numerical array
        Array contains list of integers or floats
    out_file_name : file name
        File name of the output file
    Returns
    --------
        Generate file with specified name containing histogram
        , tile and labeled axis.
    Raises
    --------
    NameError
        No output file name
    SystemExit
        File exits
    """
    if out_file_name is None:
        raise NameError('Out_file_name required')
    if path.exists(out_file_name):
        raise SystemExit('File already exits')
    plt.hist(L)
    plt.title(str('Mean: ' + str(math_lib.list_mean(L)) +
                  ' Stdev: ' + str(math_lib.list_stdev(L))))
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig(out_file_name, dpi=300)
    pass


def combo(L, out_file_name):
    """ Histogram and boxplot of numerical array and give specified name
    Parameters
    --------
    L :  Numerical array
        Array contains list of integers or floats
    out_file_name : file name
        File name of the output file
    Returns
    --------
        Generate file with specified name containing histogram, boxplot
        , tile and labeled axis.
    Raises
    --------
    NameError
        No output file name
    SystemExit
        File exits
    """
    if out_file_name is None:
        raise NameError('Out_file_name required')
    if path.exists(out_file_name):
        raise SystemExit('File already exits')
    fig, (axs1, axs2) = plt.subplots(1, 2)
    axs1.hist(L)

    axs1.title(str('Mean: ' + str(math_lib.list_mean(L)) +
                   ' Stdev: ' + str(math_lib.list_stdev(L))))

    axs1.xlabel('Value')
    axs1.ylabel('Frequency')
    axs2.hist(L)

    axs2.title(str('Mean: ' + str(math_lib.list_mean(L)) +
                   ' Stdev: ' + str(math_lib.list_stdev(L))))

    axs2.xlabel('Box')
    axs2.ylabel('Distribution')
    plt.savefig(out_file_name, dpi=300)
    pass
