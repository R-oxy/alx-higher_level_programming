#!/usr/bin/python3
import numpy as np
"""Module that implements that multiplies 2 matrices by using the module NumPy"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    Parameters:
        m_a (list): A list of lists representing the first matrix.
        m_b (list): A list of lists representing the second matrix.
    Returns:
        list: The resulting matrix as a list of lists.
    Raises:
        ValueError: If the matrices are not compatible for multiplication.
    """
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
