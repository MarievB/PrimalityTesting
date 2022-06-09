# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 14:29:56 2022

@author: marie
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

# from Lark Ramkilde Knudsen
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
    
    a = 43 
    b = 1001 # odd 
    steps = (b-a)//2
    t_td = [0]*steps
    t_mr = [0]*steps
    j, m1, m2 = 0,0,0
    
    for i in range(a,b,2):
        print("i = ", i)
        tic = timeit.default_timer()
        for j in range(reps):
            m1 += trialDivision(i)
        toc = timeit.default_timer() 
        t_td[j] = (toc-tic)/reps
        
        tic = timeit.default_timer()
        for j in range(reps):
            m2 += itMillerRabin(i, 4)
        toc = timeit.default_timer() 
        t_td[j] = (toc-tic)/reps
        
        j += 1
    
    df = pd.DataFrame(data = {'nums':[i*2+43 for i in range(steps)], 'mr':t_mr, 'td':t_td})
    path = 'C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python_singlevalues.csv'
    df.to_csv(path)
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)
    print("error: ", abs(m1-m2))

if __name__ == "__main__":
    main()