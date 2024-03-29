# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:47:42 2022

@author: e_fmaill
"""

import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
import numpy as np
from scipy.integrate import odeint
from scipy import integrate
import matplotlib.pyplot as plt
from itertools import cycle
# from labellines import labelLines

#def chute_frot_x(vx, t, g, m, k):        
#    return -k/m*vx
#def chute_frot_z(vz, t, g, m, k):        
#    return -k/m*vz-g
def chute_frot(y, t, g, msurk, gamma):
    x, z, vx, vz = y        
    return [vx, vz, -ksurm*np.abs(vx)**gamma, -g-ksurm*np.abs(vz)**gamma]

x0  = 0
z0  = 0
V0 = 20
n = 8
theta = (1/2-1/n)*np.pi
thetadeg = np.ceil(theta * 180/np.pi)
Vz0 = V0*np.sin(theta)
Vx0 = V0*np.cos(theta)
#y0 = [Vx0, Vz0, 0, 0]
t = np.linspace(0, 30, 10000)
g = 9.81
#m = 10
#k = 1
ksurm = 0.1
gamma = 1.5
y0 = [x0, z0, Vx0, Vz0]

#lines = ["-"]
lines = ["-","--","-.",":"]
linecycler = cycle(lines)

sol0 = odeint(chute_frot, y0, t, args=(g,ksurm,0))
#index pour lequel z devient negatif
END0 = np.where(sol0[:,1] < 0, sol0[:,1], -np.inf).argmax()

cm = 1/2.54  # centimeters in inches
for gamma in [0.5, 0.707, 1]:
    figsize=(20*cm,15*cm)
    fig, ax = plt.subplots()
    plt.plot(sol0[:END0, 0], sol0[:END0, 1], label=r'$k/m=0$', ls='-')
    for ksurm in [0.1, 0.2, 0.5, 0.707, 1]:
        sol = odeint(chute_frot, y0, t, args=(g,ksurm,gamma))
        END = 10+np.where(sol[:,1] < 0, sol[:,1], -np.inf).argmax()
        plt.plot(sol[:END, 0], sol[:END, 1], 
                 #label=f'$k/m={ksurm:.1f},\\alpha={gamma:.1f}$',
                 label=f'$k/m={ksurm:.1f}$',
                 ls=next(linecycler))        

    plt.legend(loc='best')
    lines = ax.get_lines()
    xvals = [22, 18, 10.5, 20, 14, 7.46, 18, 11.53, 6.09, 30]
    plt.xlabel('$x$')
    plt.ylabel('$z$')
    plt.ylim([0, 20])
    plt.xlim([0, 35])
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.title(f"$V_0={V0} m/s$, $\\alpha={gamma}$, $\\theta={thetadeg}$° selon les types de frottements $f$", bbox=props)
    plt.grid()
    plt.tight_layout()
    dpi=200
    plt.savefig(f'Tir_parabolique_frottements_alpha_{gamma:.1f}.png', dpi=dpi)
plt.close() 
