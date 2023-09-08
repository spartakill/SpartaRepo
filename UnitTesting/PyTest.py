import pytest
def square(n):
    return n*n
def cube(n):
    return n*n*n
def test_sqaure():
    n = 2
    assert n*n == 4
def test_cube():
    n = 2
    assert n*n*n == 8