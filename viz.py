import sys
import os
import argparse
import data_viz
import get_data

# Parsing arguments using argparse


def parse_args():
    parser = argparse.ArgumentParser(
            description='Pass Parameters')
    # Add output file_name
    parser.add_argument('--out_file',
                        type=str,
                        help='Name of the file',
                        required=True)
    # Add plot type
    parser.add_argument('--plot_type',
                        type=str,
                        help='Number of column',
                        required=True)
    # Add column number
    parser.add_argument('--col_num',
                        type=int,
                        help='Column number',
                        required=False)

    return parser.parse_args()


def main():
    # Get the arquments
    args = parse_args()
    # Get the data from stdin
    A = get_data.read_stdin_col(args.col_num)
    if len(A) == 0:
        print('Empty list')
        sys.exit(1)
    if args.plot_type == 'boxplot':
        data_viz.boxplot(A, args.out_file)
    if args.plot_type == 'histogram':
        data_viz.histogram(A, args.out_file)
    if args.plot_type == 'combo':
        data_viz.combo(A, args.out_file)
    else:
        print('Check plot type')
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
