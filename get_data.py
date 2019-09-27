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
        Return 'None' if cannot be extracted
    """
    # Check input file and range of column
    if col_num < 0:
        raise ValueError('Column number should be positive')
    try:
        f = open(sys.stdin)
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
        return None
    A = []
    for line in f:
        Array = line.strip().split()
        if col_num >= len(Array):
            raise ValueError('Index out of bound')
        A.append(int(Array[col_num]))
    f.close()
    return A
