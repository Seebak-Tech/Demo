#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Calculadora:

    def __init__(self):
        self.a = 0
        self.b = 0


    def suma(self, a, b):
        self.a = a
        self.b = b
        resultado = self.a + self.b    
        return resultado


    def resta(self, a, b):
        self.a = a
        self.b = b
        resultado = self.a - self.b
        return resultado


    def div(self, a, b):
        self.a = a
        self.b = b
        resultado = self.a / self.b
        return resultado


    def mult(self, a, b):
        self.a = a
        self.b = b
        resultado = self.a * self.b
        return resultado
