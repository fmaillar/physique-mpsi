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
from labellines import labelLines

#def chute_frot_x(vx, t, g, m, k):        
#    return -k/m*vx
#def chute_frot_z(vz, t, g, m, k):        
#    return -k/m*vz-g
def chute_frot(y, t, g, msurk, gamma):
    x, z, vx, vz = y        
    return [vx, vz, -1/msurk*np.abs(vx)**gamma, -g-1/msurk*np.abs(vz)**gamma]

x0  = 0
z0  = 0
V0 = 19
n = 7
theta = (1/2-1/n)*np.pi
thetadeg = np.ceil(theta * 180/np.pi)
Vz0 = V0*np.sin(theta)
Vx0 = V0*np.cos(theta)
#y0 = [Vx0, Vz0, 0, 0]
t = np.linspace(0, 30, 10000)
g = 9.81
#m = 10
#k = 1
msurk = 10
gamma = 1.5
y0 = [x0, z0, Vx0, Vz0]



# fig1 = plt.plot(x,z, '.')
# plt.xlabel('$x$')
# plt.ylabel('$y$')
# plt.ylim([0, 25])
# plt.xlim([0, 35])
# plt.grid()
#plt.tight_layout()

#lines = ["-"]
lines = ["-","--","-.",":"]
linecycler = cycle(lines)

sol0 = odeint(chute_frot, y0, t, args=(g,msurk,0))
#index pour lequel z devient negatif
END0 = np.where(sol0[:,1] < 0, sol0[:,1], -np.inf).argmax()

cm = 1/2.54  # centimeters in inches
figsize=(20*cm,15*cm)
fig, ax = plt.subplots()
plt.plot(sol0[:END0, 0], sol0[:END0, 1], label=r'$k=0$', ls=next(linecycler))
for gamma in [1, 2]:
    for msurk in [5.0, 2.0, 1.0]:    
        sol = odeint(chute_frot, y0, t, args=(g,msurk,gamma))
        END = 10+np.where(sol[:,1] < 0, sol[:,1], -np.inf).argmax()
        plt.plot(sol[:END, 0], sol[:END, 1], label=f'$m/k={msurk:.0f},\\alpha={gamma:.0f}$',
                 ls=next(linecycler))        

plt.legend(loc='best')
lines = ax.get_lines()
xvals = [22, 18, 10.5, 20, 14, 7.46, 18, 11.53, 6.09, 30]
#labelLines(lines, fontsize=10, xvals=xvals, yoffsets=0, zorder=5.5, align=True)
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.ylim([0, 20])
plt.xlim([0, 35])
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
# plt.text(0.8,0.9, '$f = k v^{\\alpha}$', transform=ax.transAxes, fontsize=14,
#         verticalalignment='top', bbox=props)
plt.title(f"$V_0={V0} m/s$, $\\theta={thetadeg}$° selon les types de frottements $f$", bbox=props)
plt.grid()
plt.tight_layout()
dpi=200
plt.savefig('Tir_parabolique_frottements.png', dpi=dpi)
plt.show()        
