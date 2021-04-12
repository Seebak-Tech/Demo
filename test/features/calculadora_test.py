#!/usr/bin/env python
# -*- coding: utf-8 -*-

from demo.features.calculadora import Calculadora

def test_suma():
    calculadora = Calculadora()
    resultado = calculadora.suma(2, 3)
    assert resultado == 5


def test_resta():
    calculadora = Calculadora()
    assert calculadora.resta(4, 2) == 2
    
def test_mult():                                               
    3     calculadora = Calculadora()                                 
    2     assert calculadora.mult(2, 2) == 4

def test_div():                                               
    3     calculadora = Calculadora()                                 
    2     assert calculadora.div(10, 5) == 2
