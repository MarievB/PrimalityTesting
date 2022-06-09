# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:06:45 2022

@author: marie
"""

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
    print([x3 % E[2], -y3 % E[2]])
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
    print([x3 % E[2], -y3 % E[2]])
    return [x3 % E[2], -y3 % E[2]]

def ECM_example(n):
    """ Print toy example of Lenstra's ECM with B = 4"""
    g = gcd(n,6)
    if g > 1:
        return g
    x, y, a = 1, 3, 12
    b = (pow(y,2) - pow(x,3) - a*x) % n
    P = [x, y]
    E = [a, b, n]
    print("computing [2]P")
    P2 = double(P,E)
    if(P2[0] == float('inf')):
        print("factor found: ")
        return P2[1]
    
    print("computing [4]P")
    P4 = double(P2,E)
    if(P4[0] == float('inf')):
        print("factor found: ")
        return P4[1]
    
    print("computing [8]P")
    P8 = double(P4,E)
    if(P8[0] == float('inf')):
        print("factor found: ")
        return P8[1]
    
    print("computing [16]P")
    P16 = double(P8,E)
    if(P16[0] == float('inf')):
        print("factor found: ")
        return P16[1]
    
    print("computing [24]P")
    P24 = add(P16, P8,E)
    if(P24[0] == float('inf')):
        print("factor found: ")
        return P24[1]
    
    print("increase B")
    
def main():
    n = 61*7919
    print(ECM_example(n))
    print("n = ", n)

if __name__ == "__main__":
    main()