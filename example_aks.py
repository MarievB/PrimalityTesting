# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 09:46:52 2022

@author: marie
"""

import timeit 
import math

def isPowerOf(n,b,A,i,j):
    """ Return if A[i..j] contains a base a such that a^b = n. """
    m = int((j-i)/2)
    x = pow(A[i+m],b)
    print(A[i+m], "^", b, "=", x)
    if x == n:
        print("woop, this is a perfect power, no need to continue the search:)")
        return True
    elif j-i <= 1:
        print("404 power not found with b = ", b)
        return False 
    elif x < n:
        print("recurse in larger half of A")
        return isPowerOf(n,b,A,i+m,j)
    else:
        print("recurse in smaller half of A")
        return isPowerOf(n,b,A,i,i+m)

def isPerfectPower(n):
    """ Return if n is a perfect power. """
    A = [_ for _ in range(2,int(math.sqrt(n))+1)]
    for b in range(2, int(math.log(n,2))+1):
        if isPowerOf(n,b,A,0,len(A)):
            return True
    return False

def binomialCheck(a, n, r):
    """ Return if (x+a)^n = x^n + a mod (n, x^r-1). """
    
    
    return True

def gcd(a, b):
    """ Return the greatest common divisor of a and b. """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def AKS(n):
    r = 0
    print("perfect power testing")
    if isPerfectPower(n):
        return 0
    
    print("finding r")
    print("(\\log_2 n)^2 = ", int(pow(math.log2(n),2)))
    for q in range(int(pow(math.log2(n),2))+1, n):
        #print("q = ", q)
        potential_r_is_found = True
        n_q = n%q
        
        for j in range(1, int(pow(math.log2(n),2))+1):
            if pow(n_q, j, q) == 1:
                #print("nope, n has order ", j, "mod ", q)
                print(n,"^",j, "=",pow(n,j), "&", " mod ", q, " = ", pow(n_q, j, q), "\\\\")
                potential_r_is_found = False
                break
        
        if potential_r_is_found:
            r = q
            break
    
    for a in range(1, r):
        if gcd(a,n) > 1:
            print("gcd(",a,",",n,") = ", gcd(a,n))
            return 0
    print("woop! we found r = ", r)
    
    print("binomial check")
    for a in range(1, int(math.sqrt(r)*math.log2(n))):
        if not binomialCheck(a, n, r):
            return 0 
        
    return 1

def main(): 
    main_tic = timeit.default_timer()
    if(AKS(137)):
        print("prime")
    else:
        print("not prime")
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)

if __name__ == "__main__":
    main()