# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:06:02 2022

@author: marie
"""
import math
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 16})

#%% PYTHON (MR, AKS, TD) & MAPLE (AKS)
aksdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python_3reps.csv')
mtdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python_singlevalues.csv')
mapledata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_maple.csv')

N = aksdata["nums"]
aks = aksdata["aks"]
mr = mtdata["mr"]
td = mtdata["td"]
aks_m = mapledata["aks"]

idx = [i for i in range(len(N)) if aks[i] > 1]
N = [N[i] for i in idx]
aks = [aks[i] for i in idx]
mr = [mr[i] for i in idx]
td = [td[i] for i in idx]
aks_m = [aks_m[i] for i in idx]

plt.plot(N, aks, color='green', linestyle='solid', label=r'\rm{AKS (Python)}')
plt.plot(N, aks_m, color='gold', linestyle='solid', label=r'\rm{AKS (Maple)}')
plt.plot(N, mr, color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin (Python)}')
plt.plot(N, td, color='darkorchid', linestyle='dotted', label=r'\rm{Trial division (Python)}')
plt.xlabel(r"\bf{n}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Primality Test Time Consumption}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/Presentation/Figures/all_python_high_values.eps', format='eps')
plt.show()

#%% PYTHON (MR, AKS, TD) & MAPLE (AKS) (LOGS)
aksdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python_3reps.csv')
mtdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python_singlevalues.csv')
mapledata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_maple.csv')

N = aksdata["nums"]
aks = aksdata["aks"]
mr = mtdata["mr"]
td = mtdata["td"]
aks_m = mapledata["aks"]

idx = [i for i in range(len(N)) if aks[i] > 1]
idx_inv = [i for i in range(len(N)) if aks[i] <= 1]
N = [N[i] for i in idx]
aks = [aks[i] for i in idx]
mr = [mr[i] for i in idx]
td = [td[i] for i in idx]
aks_m = [aks_m[i] for i in idx]
N = [math.log(i,2) for i in N]

plt.plot(N, aks, color='green', linestyle='solid', label=r'\rm{AKS (Python)}')
plt.plot(N, aks_m, color='gold', linestyle='solid', label=r'\rm{AKS (Maple)}')
plt.plot(N, mr, color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin (Python)}')
plt.plot(N, td, color='darkorchid', linestyle='dotted', label=r'\rm{Trial division (Python)}')
plt.xlabel(r"\bf{log(n)}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Primality Test Time Consumption}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/Presentation/Figures/all_python_high_values_log.eps', format='eps')
plt.show()
#%% Which numbers are slow?
aksdata_rbc = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python_reach_binom_test.csv')
aks_rbc = aksdata_rbc["aks"]

N_rbc = aksdata["nums"]

for i in idx:
    if aks_rbc[i] == 0:
        print(N_rbc[i], "is slow, but does not reach the binomial check")

for i in idx_inv:
    if aks_rbc[i] == 1:
        print(N_rbc[i], "is fast, but reaches the the binomial check")

#%% PYTHON (MR) (LOGS)
def f(X):
    return [3.30285431388118e-7*x*x - 0.0000900672060047346*x + 0.00866010867064043 for x in X]

R = 0.997075638689574

data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_python_singlevalues.csv')

mr = data["mr"]
n = [_ for _ in range(len(mr))]

rstr = r'$R^2=%.5f$' % R

plt.plot(mr, color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
plt.plot(f(n), color='coral', linestyle='solid', label=r'\rm{Quadratic polynomial}')
plt.xlabel(r"\bf{log(n)}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.text(0, 0.18, rstr, va='bottom', bbox=dict(boxstyle='Round', facecolor='white', alpha=0.2))
plt.tight_layout()
#plt.title(r'\bf{Fitted 2nd degree polynomial to Miller-Rabin test}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/Presentation/Figures/mr_python_singlevalues.eps', format='eps')
plt.show()

#%%












