# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:23:25 2022

@author: marie
"""

import random
import timeit 

def MillerRabin(n):
    if n==0 or n==1:
        return False
    
    t = n-1
    s = 0
    
    while not t%2:
        t = t//2
        s += 1
    
    b = random.randrange(1,n)
    print("b = ", b)
    print("t = ", t)
    print("s = ", s)
    
    y = pow(b, t, n) 
    print("b^t = ", y)
    
    if not (y-1)%n:
        return True
        
    for i in range(s):
        if not (y+1)%n:
            return True
        y = pow(y, 2, n)
        print("b^",2**(i+1)*t, " = ", y)
    
    return False

def itMillerRabin(n,l):
    for i in range(l):
        print("iteration ", i+1)
        if not MillerRabin(n):
            return 0
    return 1

def main(): 
    main_tic = timeit.default_timer()
    if(itMillerRabin(561,3)):
        print("prime")
    else:
        print("not prime")
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)

if __name__ == "__main__":
    main()