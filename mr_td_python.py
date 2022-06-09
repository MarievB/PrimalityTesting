# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 08:33:42 2022

@author: marie

This script contains primality tests. 
Take care when using. 
Primes may cause addiction.
Maybe another introduction?
Remember to specify that the algorithms return 1 if prime and 0 if composite
"""

# initialization 
import random
import timeit 
import math
import pandas as pd

def pow2(x, y, z):
    """ Return x^y mod z. """
    w = 1
    y = bin(y)
    k = len(y)
    for i in range(2,k): # 2 bcs. python reps first w. '0b'
        w = (w*w)%z
        if y[i] == '1':
            w = (w*x)%z
    return w

def trialDivision(n):
    if n==0 or n==1:
        return 0
    
    for i in range(2, int(math.sqrt(n))+1):
        if not n%i:
            return 0
    return 1

def MillerRabin(n):
    if n==0 or n==1:
        return False
    
    t = n-1
    s = 0
    
    while not t%2:
        t = t//2
        s += 1
    
    b = random.randrange(1,n)
    
    y = pow(b, t, n) 
    
    if not (y-1)%n:
        return True
        
    for i in range(s):
        if not (y+1)%n:
            return True
        y = pow(y, 2, n)
    
    return False

def itMillerRabin(n,m):
    for i in range(m):
        if not MillerRabin(n):
            return 0
    return 1

def main(): 
    main_tic = timeit.default_timer()
    
    reps = 5
    steps = 100
    stepsize = 100000
    
    N = [_ for _ in range(steps)]
    
    t_td = [0]*steps
    t_mr = [0]*steps
    err = [0]*steps
    
    # iterations in Miller-Rabin
    m = 4
    
    for n in N:
        print("step: ", n)
        # test odd numbers from a to b
        a = n*stepsize+1
        b = (n+1)*stepsize
        
        # trial division 
        tic = timeit.default_timer()
        m1 = 0
        for i in range(a, b, 2):
            for j in range(reps):
                m1 += trialDivision(i)
        toc = timeit.default_timer() 
        t_td[n] = (toc-tic)/reps
        
        # Miller-Rabin
        tic = timeit.default_timer()
        m2 = 0
        for i in range(a, b, 2):
            for j in range(reps):
                m2 += itMillerRabin(i,m)
        toc = timeit.default_timer() 
        t_mr[n] = (toc-tic)/reps
        
        # compute number of errors of Miller-Rabin
        err[n] = m2-m1
    
    df = pd.DataFrame(data = {'nums':N, 'mr':t_mr, 'td':t_td, 'errors':sum(err), 'stepsize':stepsize})
    path = 'C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python.csv'
    df.to_csv(path)
    
    main_toc = timeit.default_timer()
    print(main_toc-main_tic)
    

if __name__ == "__main__":
    main()