# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:09:08 2022

@author: marie
"""

import math
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 16})

#%% MAPLE (MR, AKS, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/all_maple.csv')

n = [math.log(i, 2) for i in range(1, len(data["mr"])+1)]

plt.plot(n, data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
plt.plot(n, data["aks"], color='green', linestyle='solid', label=r'\rm{AKS}')
plt.plot(n, data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
plt.xlabel(r"\bf{log of number size (100)}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Primality Tests - Time Consumption (Maple)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/all_maple_logs.eps', format='eps')
plt.show()

#%% MAPLE (MR, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_maple.csv')

n = [math.log(i, 2) for i in range(1, len(data["mr"])+1)]

plt.plot(n, data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
plt.plot(n, data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
xlab = r" $\displaystyle (10^5)$"
plt.xlabel(r"\bf{log of number size} " + xlab)
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Miller-Rabin and Trial Division\\ Time Consumption (Maple)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_td_maple_logs.eps', format='eps')
plt.show()

#%% PYTHON (MR, AKS, TD) & MAPLE (AKS)
aksdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python_3reps.csv')
mtdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python_singlevalues.csv')
mapledata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_maple.csv')

N = aksdata["nums"]
aks = aksdata["aks"]
mr = mtdata["mr"]
td = mtdata["td"]

N = [math.log(i, 2) for i in N]

plt.plot(N, aks, color='green', linestyle='solid', label=r'\rm{AKS (Python)}')
plt.plot(N, mapledata["aks"], color='gold', linestyle='solid', label=r'\rm{AKS (Maple)}')
plt.plot(N, mr, color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin (Python)}')
plt.plot(N, td, color='darkorchid', linestyle='dotted', label=r'\rm{Trial division (Python)}')
plt.xlabel(r"\bf{log(n)}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Primality Test Time Consumption}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/all_python_logs.eps', format='eps')
plt.show()


#%% PYTHON (MR, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python.csv')

print("error: ", data["errors"][0])
n = [math.log(i, 2) for i in range(1, len(data["mr"])+1)]

plt.plot(n, data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
plt.plot(n, data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
xlab = r" $\displaystyle (10^5)$"
plt.xlabel(r"\bf{log of number size} " + xlab)
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
#plt.title(r'\bf{Miller-Rabin and Trial Division Time Consumption (Python)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_td_python_logs.eps', format='eps')
plt.show()

#%% PYTHON (MR)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_python.csv')

n = [math.log(i, 2) for i in range(1, len(data["mr"])+1)]

plt.plot(n, data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
xlab = r" $\displaystyle (10^6)$"
plt.xlabel(r"\bf{log of number size} " + xlab)
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.tight_layout()
plt.title(r'\bf{Miller-Rabin Time Consumption (Python)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_python_logs.eps', format='eps')
plt.show()


