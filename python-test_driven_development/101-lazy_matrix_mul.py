#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy.

Defines lazy_matrix_mul, which delegates directly to numpy and
lets numpy raise its own native errors on invalid input.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices together using numpy.matmul."""
    return numpy.matmul(m_a, m_b)
