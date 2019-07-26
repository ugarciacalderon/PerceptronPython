import sys
sys.path.append('..') # Adds higher directory to python modules path.

from Perceptron.Perceptron import *

def test_Perceptron():

    inputs = [
        [0,0,1],
        [0,1,1],
        [1,0,1],
        [1,1,1]
    ]

    outputs = [0,0,0,1]

    perceptron = Perceptron(inputs, outputs)
    result = perceptron.Fit()

    ### test ###
    assert result is True, 'unittest passed!'