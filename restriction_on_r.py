# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 13:29:42 2022

@author: marie
"""

import timeit 
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 12})

def f(n):
    return [i-1 for i in n]
def g(n):
    return [(pow(math.log2(i),2))+1 for i in n]

def main():
    main_tic = timeit.default_timer()
    n = [_ for _ in range(1,50)]
    
    plt.scatter(n, f(n), color='darkorchid', marker =".", label=r"$\displaystyle n-1$")
    plt.scatter(n, g(n), color='dodgerblue', marker ="1", label= r"$\displaystyle \log (n)^2+1$")
    plt.vlines(x = 22, ymin = 0, ymax = 49, color='black', linestyle = 'dashed', label = r"$\displaystyle n = 22$")
    plt.xlabel(r'\bf{n}')
    plt.legend(loc='lower right', fancybox=True)
    plt.title(r'\bf{Possible values for r}')
    plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/restricting_r.eps', format='eps')
    plt.show()
    
    main_toc = timeit.default_timer()
    print("time elapsed: ", main_toc-main_tic)
    
if __name__ == "__main__":
    main()