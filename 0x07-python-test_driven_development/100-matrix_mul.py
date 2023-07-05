#!/usr/bin/python3
"""Module that defines a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
    Args:
        m_a (list): The first matrix represented as a list of lists of integers or floats.
        m_b (list): The second matrix represented as a list of lists of integers or floats.
    Raises:
        TypeError: If m_a or m_b is not a list, or if m_a or m_b is not a list of lists,
                   or if one element of the lists is not an integer or a float.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.
        TypeError: If each row of m_a is not of the same size, or if each row of m_b is not of the same size.
    Returns:
        list: The resulting matrix after the multiplication.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    
    if len(set(len(row) for row in m_a)) > 1 or len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            val = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(val)
        result.append(row)
    
    return result
