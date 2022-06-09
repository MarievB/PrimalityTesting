# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 10:10:18 2022

@author: marie
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

#%% MAPLE (MR, AKS, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/all_maple.csv')

plt.plot(data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
plt.plot(data["aks"], color='green', linestyle='solid', label=r'\rm{AKS}')
plt.plot(data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
plt.xlabel(r"\bf{number size (100)}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.title(r'\bf{Primality Tests - Time Consumption (Maple)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/all_maple.eps', format='eps')
plt.show()

#%% MAPLE (MR, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_maple.csv')
    
plt.plot(data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
plt.plot(data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
xlab = r" $\displaystyle (10^5)$"
plt.xlabel(r"\bf{number size} " + xlab)
plt.legend(loc='upper left', fancybox=True)
plt.title(r'\bf{Miller-Rabin and Trial Division Time Consumption (Maple)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_td_maple.eps', format='eps')
plt.show()

#%% PYTHON (MR, AKS, TD) & MAPLE (AKS)
aksdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_python_3reps.csv')
mtdata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python_singlevalues.csv')
mapledata = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/aks_maple.csv')

N = aksdata["nums"]
aks = aksdata["aks"]
mr = mtdata["mr"]
td = mtdata["td"]

# maybe remove outlier that makes all the rest of the data difficult to interpret (due to sleep)
#outlier = 474
#N = pd.concat([aksdata["nums"][0:outlier], aksdata["nums"][outlier+1:]])
#aks = pd.concat([aksdata["aks"][0:outlier], aksdata["aks"][outlier+1:]])
#mr = pd.concat([mtdata["mr"][0:outlier], mtdata["mr"][outlier+1:]])
#td = pd.concat([mtdata["td"][0:outlier], mtdata["td"][outlier+1:]])

plt.plot(N, aks, color='green', linestyle='solid', label=r'\rm{AKS (Python)}')
plt.plot(aksdata["nums"], mapledata["aks"], color='gold', linestyle='solid', label=r'\rm{AKS (Maple)}')
plt.plot(N, mr, color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin (Python)}')
plt.plot(N, td, color='darkorchid', linestyle='dotted', label=r'\rm{Trial division (Python)}')
plt.xlabel(r"\bf{n}")
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.title(r'\bf{Primality Test Time Consumption}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/all_python.eps', format='eps')
plt.show()


#%% PYTHON (MR, TD)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_td_python.csv')

print("error: ", data["errors"][0])

plt.plot(data["td"], color='darkorchid', linestyle='dotted', label=r'\rm{Trial division}')
plt.plot(data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
xlab = r" $\displaystyle (10^5)$"
plt.xlabel(r"\bf{number size} " + xlab)
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.title(r'\bf{Miller-Rabin and Trial Division Time Consumption (Python)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_td_python.eps', format='eps')
plt.show()

#%% PYTHON (MR)
data = pd.read_csv('C:/Users/marie/OneDrive/STUDIE/F22/BP/Scripts/data/mr_python.csv')

plt.plot(data["mr"], color='dodgerblue', linestyle='dashed', label=r'\rm{Miller-Rabin}')
xlab = r" $\displaystyle (10^6)$"
plt.xlabel(r"\bf{number size} " + xlab)
plt.ylabel(r'\bf{time (sec)}')
plt.legend(loc='upper left', fancybox=True)
plt.title(r'\bf{Miller-Rabin Time Consumption (Python)}')
plt.savefig('C:/Users/marie/OneDrive/STUDIE/F22/BP/LaTeX/Figures/mr_python.eps', format='eps')
plt.show()


