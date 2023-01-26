"""
Unit tests for the calculator library
"""
import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
path = os.path.dirname(current) + '/calculatorLibrary_Tuuli_TG'
 
# adding the parent directory to
# the sys.path.
sys.path.append(path)

import calculator

class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 3 == calculator.divide(6, 2)
