"""Tests for my functions. I tried using the mock and builtins but did not work because I'm calling a function with multiple input() calls in it. This will be an area for improvement."""

from functions import Q1_function, Q21_function, Q61_function, start

def test_Q1_function():
    
    assert callable(Q1_function)
    
def test_Q21_function():
    
    assert callable(Q21_function)

def test_Q61_function():
    
    assert callable(Q61_function)

def test_start():
    
    assert callable(start)
