# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:26:11 2020

@author: prasa
"""
"""
x=[1,2,3,4,5]
y=[5,7,9,11,13]
y=2x+3

"""
'''
area = [2600,3000,3200,3600,4000]
price = [550k,565k,610k,680k,725k]

price = 135.78 * area + 180616.43

''' 

""" 
Gradient descent is an algorithm that finds best fit
line for given training data 

"""

import numpy as np
 
def gradient_descent(x,y):
    m_curr = b_curr=0
    iterations = 10000
    n = len(x)
    learning_rate = 0.08
    
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost= (1/n) * sum( [val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr - learning_rate*bd
        print("m {}, b {}, cost {} iteration{}".format(m_curr,b_curr,cost,i))
    
    
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)