#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices together using numpy.matmul."""
    return numpy.matmul(m_a, m_b)
