#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numbers 


class CalcTypeError(Exception):
    
    def __init__(self, message):
        self.message = message 
    

class Calculator:

    def __init__(self):
        self.__set_params(0, 0)


    def __set_params(self, num_arg1, num_arg2):
        self.num_arg1 = num_arg1 
        self.num_arg2 = num_arg2

    def __is_number(self, num_arg):
        txt_message = (  
            "\nCause: The argument >> " + str(num_arg) +
            " << should be a number\n" +
            "Action: Please enter numbers only\n"
        )
        if not isinstance(num_arg, numbers.Number):
            raise CalcTypeError(txt_message)

    
    def __validate_params(self, num_arg1, num_arg2):
        self.__is_number(num_arg1)
        self.__is_number(num_arg2)


    def sum(self, num_arg1, num_arg2):
        self.__validate_params(num_arg1, num_arg2)
        self.__set_params(num_arg1, num_arg2)

        return self.num_arg1 + self.num_arg2    


    def rest(self, num_arg1, num_arg2):
        self.__validate_params(num_arg1, num_arg2)
        self.__set_params(num_arg1, num_arg2)

        return (
            self.num_arg1 -
            self.num_arg2
        )


    def div(self, num_arg1, num_arg2):
        self.__validate_params(num_arg1, num_arg2)
        self.__set_params(num_arg1, num_arg2)
        
        return self.num_arg1 / self.num_arg2


    def mult(self, num_arg1, num_arg2):
        self.__validate_params(num_arg1, num_arg2)
        self.__set_params(num_arg1, num_arg2)

        return self.num_arg1 * self.num_arg2
