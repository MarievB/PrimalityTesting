# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:36:22 2022

@author: marie
"""

import timeit 
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

def f1(m):
    # n is prime when MR reports prime
    beta = 1024
    return [1/(1 + 1/(pow(2,i))*(beta*math.log(2)-1)) for i in m]

def g1(m):
    # MR reports composite when n is composite 
    return [1-1/(pow(2,i)) for i in m]

def f2(m):
    # n is prime when MR reports prime
    beta = 1024
    return [1/(1 + 1/(pow(4,i))*(beta*math.log(2)-1)) for i in m]

def g2(m):
    # MR reports composite when n is composite 
    return [1-1/(pow(4,i)) for i in m]

def tableGen(m,f1,f2,g1,g2):
    print("Trials", "&", "$\Pr(A|B)$", "&", "$\\Pr(\\bar{B} | \\bar{A})$", "&", "$\Pr(A|B)$", "&", "$\\Pr(\\bar{B} | \\bar{A})$", "\\\\", "\\hline")
    for i in m:
        if i%5 == 0:
            print(i, "&", round(f1([i])[0],10), "&", round(g1([i])[0],10), "&", round(f2([i])[0],10), "&", round(g2([i])[0],10),  "\\\\", "\\hline")
        
def main():
    main_tic = timeit.default_timer()
    m = [_ for _ in range(50)]
    tableGen(m,f1,f2,g1,g2)
    
    plt.scatter(m, f1(m), color='darkorchid', marker ="o", label=r"$\displaystyle \Pr(A|B)$")
    plt.scatter(m, g1(m), color='dodgerblue', marker ="^", label= r"$\displaystyle \Pr(\bar{B}| \bar{A})$")
    plt.xlabel(r'\bf{trials}')
    plt.ylabel(r'\bf{probability}')
    plt.legend(loc='lower right', fancybox=True)
    plt.title(r'\bf{Probability of Correctness. Bound: $\frac{n-1}{2}$}')
    plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/probability_of_correctness_1.eps', format='eps')
    plt.show()
    
    m = [_ for _ in range(30)]
    
    plt.scatter(m, f2(m), color='darkorchid', marker ="o", label=r"$\displaystyle \Pr(A|B)$")
    plt.scatter(m, g2(m), color='dodgerblue', marker ="^", label= r"$\displaystyle \Pr(\bar{B} | \bar{A})$")
    plt.xlabel(r'\bf{trials}')
    plt.ylabel(r'\bf{probability}')
    plt.legend(loc='lower right', fancybox=True)
    plt.title(r'\bf{Probability of Correctness. Bound: $\frac{n-1}{4}$}')
    plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/probability_of_correctness_2.eps', format='eps')
    plt.show()
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)
    
    
if __name__ == "__main__":
    main()