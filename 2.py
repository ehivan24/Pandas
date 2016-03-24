'''
Created on Feb 27, 2015

@author: edwingsantos
'''
from numpy import sign
from numpy.matlib import rand
import numpy as np
import matplotlib.pyplot as plt


def primes1(n):
    primes =[False, False]+[True]*(n-2)
    i = 2
    while i < n:
        if not primes[i]:
            i += 1
            continue
        k = i * i
        while k < n:
            primes[k] = False
            k += i
        i +=1
    return [i for i in xrange(2, n) if primes[i]]

def step():
    return sign(rand(1) - .5)
def sim1(n):
    x = np.zeros(n)
    dx  = 1. / n
    for i in xrange(n - 1):
        x[i+1] = x[i] + dx * step()
    return x


plt.plot(sim1(10000))
plt.show()




#print primes1(20)

if __name__ == '__main__':
    pass