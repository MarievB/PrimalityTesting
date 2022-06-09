# -*- coding: utf-8 -*-
"""
Created on Thu May 12 09:53:06 2022

@author: marie
"""

import math

def isPowerOf(n,b,A,i,j):
    """ Return a if A[i..j] contains a base a such that a^b = n. """
    m = int((j-i)/2)
    x = pow(A[i+m],b)
    
    if x == n:
        return A[i+m]
    elif j-i <= 1:
        return False 
    elif x < n:
        return isPowerOf(n,b,A,i+m,j)
    else:
        return isPowerOf(n,b,A,i,i+m)

def findPerfectPowerFactor(n):
    """ Returns a factor of n if n is a perfect power. """
    A = [_ for _ in range(2,int(math.sqrt(n))+1)]
    
    for b in range(2, int(math.log(n,2))+1):
        a = isPowerOf(n,b,A,0,len(A))
        if a > 0:
            return a
    return 0

def gcd(a, b):
    """ Return the greatest common divisor of a and b. """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def double(P, E):
    """ Return [2]P over elliptic curve E if defined. 
    Return [inf, factor of n], if denominator is non-invertible. 
    """
    if(gcd(2*P[1], E[2]) > 1):
        return [float('inf'), gcd(2*P[1], E[2])]
    
    m = (3*P[0]*P[0] + E[0]) * pow(2*P[1], -1, E[2])
    x3 = (m*m-2*P[0])
    y3 = (m*(x3-P[0])+P[1])
    
    return [x3 % E[2], -y3 % E[2]]

def add(P1, P2, E):
    """ Return P1+P2 over elliptic curve E if defined. 
    Return [inf, factor of n], if denominator is non-invertible. 
    """
    if(gcd(P2[0]-P1[0], E[2]) > 1):
        return [float('inf'), gcd(P2[0]-P1[0], E[2])]
    
    m = (P2[1]-P1[1]) * pow(P2[0]-P1[0], -1, E[2])
    x3 = (m*m-P1[0]-P2[0])
    y3 = (m*(x3-P1[0])+P1[1])
    
    return [x3 % E[2], -y3 % E[2]]

def ECM(n, B):
    """ Return factor of n using Lenstra's ECM"""
    g = gcd(n,6)
    if g > 1:
        return g
    
    g = findPerfectPowerFactor(n)
    if g > 0:
        return g
    
    x, y, a = 1, 3, 12
    b = (pow(y,2) - pow(x,3) - a*x) % n
    P = [x, y]
    E = [a, b, n]
    
    print("P = ", P)
    
    Q = double(P,E)
    
    print("[2]P = ", Q)
    
    for i in range(math.factorial(B)):
        Q = add(P, Q, E)
        if(Q[0] == float('inf')):
            print("factor found: ")
            return Q[1]
        print(i+3,"P = ", Q)
    
    print("increase B")
    
def main():
    n = 13*7717*7669*5783
    B = 4
    print(ECM(n, B))
    print("n = ", n)

if __name__ == "__main__":
    main()