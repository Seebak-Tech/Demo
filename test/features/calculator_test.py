#!/usr/bin/env python
# -*- coding: utf-8 -*-

from demo.features.calculator import Calculator
from demo.features.calculator import CalcTypeError
import pytest


def test_sum():
    calculator = Calculator()
    result = calculator.sum(2, 3)
    assert result == 5


def test_rest():
    calculator = Calculator()
    assert calculator.rest(4, 2) == 2
    
def test_mult():                                               
    calculator = Calculator()                                 
    assert calculator.mult(2, 2) == 4

def test_div():                                               
    calculator = Calculator()                                 
    assert calculator.div(10, 5) == 2


@pytest.mark.parametrize(
    'num_arg1, num_arg2',
    [
        ('a', 'b'),
        (3, 'Mr'), 
        ('5b', 2) 
    ]
)
def test_exception_operator(num_arg1, num_arg2):
    calculator = Calculator()
    with pytest.raises(CalcTypeError):
        res = calculator.sum(num_arg1, num_arg2)


