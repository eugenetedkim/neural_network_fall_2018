_author = ["Sagar Patel", "Quimpie Tuada", "Eugene Kim", "Andrew Beechko",
           "Adrian Insingo", "Garrett Gant", "Joseph Premdas", "Tyler Oviatt" ,"Jorge Martinez",
           "Manuel Gavino", "Chris Magnuson", "Mike Chang Godinez", "Ethan Jones",
           "Zion Jones", "Colin Morris", "Mario Victorino"]
import numpy as np
import pandas

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)

# X = array([[2., 9.],
#			 [1., 5.],
#			 [3., 6.]])

y = np.array(([92], [86], [89]), dtype=float)

# y = array([[92.],
#			 [86.],
#			 [89.])

X = X/np.amax(X, axis=0)

# X = array([[2., 9.],
#			 [1., 5.],
#			 [3., 6.]])

# np.amax(X, axis=0) = array([3., 9.])

# X = array([[2./3., 9./9.],
#			 [1./3., 5./9.],
#			 [3./3., 6./9.]])

# array([[0.66666667, 1.        ],
#        [0.33333333, 0.55555556],
#        [1.        , 0.66666667]])

y = y/100

# array([[92./100],
#        [86./100],
#        [89./100]])

# array([[0.92],
#        [0.86],
#        [0.89]])

class Neural_Network:
    def __init__(self):
        print("This is a Neural Network")
        
    def forward(self, x):
        o = 10
        return o
    
    def sigmoid(self, s):
        return s

    def sigmoidPrime(self, s):
        return s
    def backward(self,X,y,o):
        print("nothing to return here")

    def train(self, X, y):
        print("nothing to return here")

    def saveWeights(self):
        print("nothing to return here")
    def predict(self):
        
