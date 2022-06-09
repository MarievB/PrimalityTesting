# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:19:51 2022

@author: marie
"""

import array as arr
import timeit 
import math
import pandas as pd

def trialDivision(n):
    """ Return 1 if n is prime. Return 0 otherwise. """
    if n==0 or n==1:
        return 0
    
    for i in range(2, int(math.sqrt(n))+1):
        if not n%i:
            return 0
    return 1

def isPowerOf(n,b,A,i,j):
    """ Return if A[i..j] contains a base a such that a^b = n. """
    m = int((j-i)/2)
    x = pow(A[i+m],b)
    
    if x == n:
        return True
    elif j-i <= 1:
        return False 
    elif x < n:
        return isPowerOf(n,b,A,i+m,j)
    else:
        return isPowerOf(n,b,A,i,i+m)

def isPerfectPower(n):
    """ Return if n is a perfect power. """
    A = [_ for _ in range(2,int(math.sqrt(n))+1)]
    
    for b in range(2, int(math.log(n,2))+1):
        if isPowerOf(n,b,A,0,len(A)):
            return True
    return False

# from Sophoclis Stephanou: https://github.com/Ssophoclis/AKS-algorithm
def fastPoly(base,power,r):
    """Use fast modular exponentiation for polynomials to raise them to a big power.
    """
    x = arr.array('d',[],)
    a = base[0]

    for i in range(len(base)):
        x.append(0)
    x[(0)] = 1 
    n = power
    
    while power > 0:
        if power % 2 == 1: 
            x = multi(x,base,n,r)
        base = multi(base,base,n,r)
        power = power // 2

    x[(0)] = x[(0)] - a
    x[(n % r )] = x[(n % r )] - 1        
    return(x)

# from Sophoclis Stephanou: https://github.com/Ssophoclis/AKS-algorithm
def multi(a,b,n,r):
    """Function used by fastPoly to multiply two polynomials together.
    """ 
    x = arr.array('d',[])
    for i in range(len(a)+len(b)-1):
        x.append(0)
    for i in range(len(a)):
        for j in range(len(b)):
                x[(i+j) % r ] += a[(i)] * b[(j)] 
                x[(i+j) % r] = x[(i+j) % r] % n 
    for i in range(r,len(x)):
            x=x[:-1]
    return(x)

# from Sophoclis Stephanou: https://github.com/Ssophoclis/AKS-algorithm
def binomialCheck(a, n, r):
    """ Return if (x+a)^n = x^n + a mod (n, x^r-1). """
    x = arr.array('l',[],)
    for a in range(1,int(math.sqrt(r)*math.log2(n))):      
        x = fastPoly(arr.array('l',[a,1]),n,r)
        if any(x):
            return False
    return True

def gcd(a, b):
    """ Return the greatest common divisor of a and b. """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def AKS(n):
    """ Return 1 if n is prime. Return 0 otherwise. """
    r = 0
    if isPerfectPower(n):
        return 0
    
    for q in range(int(pow(math.log2(n),2)), n+1):
        potential_r_is_found = True
        n_q = n%q
        
        for j in range(1, int(pow(math.log2(n),2))+1):
            if pow(n_q, j, q) == 1:
                potential_r_is_found = False
                break
        
        if potential_r_is_found:
            r = q
            break
    
    if r == 0:
        return 1

    for a in range(1, r):
        if gcd(a,n) > 1:
            return 0
    
    for a in range(1, int(math.sqrt(r)*math.log2(n))):
        if not binomialCheck(a, n, r):
            return 0 
        
    return 1

def main(): 
    reps = 3
    
    # small example of disproportional time consumption
    #tic = timeit.default_timer()
    #for i in range(reps):
    #    print(AKS(839))
    #print("elapsed time: ", (timeit.default_timer()-tic)/3)

    # measurements
    main_tic = timeit.default_timer()
    a = 43 
    b = 1001 # odd 
    steps = (b-a)//2
    t = [0]*steps
    j = 0
    for i in range(a,b,2):
        print("i = ", i)
        tic = timeit.default_timer()
        for k in range(reps):
            AKS(i)
        toc = timeit.default_timer()
        t[j] = (toc-tic)/reps
        j += 1
    
    df = pd.DataFrame(data = {'nums':[i*2+43 for i in range(steps)], 'aks':t})
    path = 'C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python2.csv'
    df.to_csv(path)
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)
    
if __name__ == "__main__":
    main()