import numpy as np

def cumulative_sum_1d(array_1d):
    return np.cumsum(array_1d)

def cumulative_sum_2d(array_2d):
    row_cumsum = np.cumsum(array_2d, axis=0)
    col_cumsum = np.cumsum(row_cumsum, axis=1)
    return col_cumsum

def calculate(array):
    if array.ndim == 1:
        return cumulative_sum_1d(array)
    elif array.ndim == 2:
        return cumulative_sum_2d(array)