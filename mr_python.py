# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 08:36:16 2022

@author: marie
"""
    
# initialization 
import random
import timeit 
import pandas as pd

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
    
    reps = 2
    steps = 100000
    stepsize = 1000000
    
    N = [_ for _ in range(steps)]
    
    t_mr = [0]*steps
    
    # iterations in Miller-Rabin
    m = 4
    
    for n in N:
        print("step: ", n)
        # test odd numbers from a to b
        a = n*stepsize+1
        b = (n+1)*stepsize
        
        tic = timeit.default_timer()
        m2 = 0
        for i in range(a, b, 1000):
            for j in range(reps):
                m2 += itMillerRabin(i,m)
        toc = timeit.default_timer() 
        t_mr[n] = (toc-tic)/reps
    
    df = pd.DataFrame(data = {'nums':N, 'mr':t_mr, 'stepsize':stepsize})
    path = 'C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_python.csv'
    df.to_csv(path)
    
    main_toc = timeit.default_timer()
    print(main_toc-main_tic)
    

if __name__ == "__main__":
    main()