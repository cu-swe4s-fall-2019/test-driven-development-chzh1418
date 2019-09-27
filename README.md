# Test Driven DevelopmentI (TDD)

## Description
This repository constains codes for assignment 3, aiming to practice on the test driven software development.

The math_lib module gives the mean and standard deviation of an array. 
The get_data module takes a column number and returns an array of numbers that correspond to the values from standard input file at the column number position.
The data_viz module can plot boxplot, histogram or both with required input file and output file name.
The viz.py script can use all the module above and generate corresponding plot.

## Installation
Install and update matplotlib
```
conda install matplotlib
```

## How to use
- To run the main script viz.py, run the following command
```
bash gen_data.sh | python viz.py --out_file [file name] --plot_type [histogram] --col_num [integer]
```

- To do unittest
	- `python test_math_lib.py` to test math_lib.py
	- `python test_get_data.py` to test get_data.py
	- `python test_data_viz.py` to test data_viz.py




