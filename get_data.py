import sys

# Define function to get data from specified columns


def read_stdin_col(col_num):
    """Get numbers from specified column.

    Parameters
    --------
    col_num : column number

    Returns
    --------
    A : list of numbers
        A list of numbers from specific column
    None
        Returns None if cannot be extracted
    """
    # Check input file and range of column
    if sys.stdin is None:
        return None

    A = []
    for line in sys.stdin:
        try:
            Array = [int(x) for x in line.split()]
            A.append(int(Arrary[col_num]))
        except IndexError:
            return None
        except ValueError:
            return None
    return A
