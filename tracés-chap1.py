# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:07:20 2020

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.sans-serif": ["Helvetica"]})
## for Palatino and other serif fonts use:
#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "serif",
#    "font.serif": ["Palatino"],
#})

#mpl.rcParams['text.usetex']=True
#mpl.rcParams['text.latex.unicode']=True

N = 1000
g = 9.81
z0 = 0
xmax = 40
alphav = np.pi*np.array([1.0/32, 1.0/8, 1.0/6, 1.0/4, 1.0/3, 3.0/8, 15/32.0], float)
v0 = 7.0#*np.array([0, 1/2, 2/3, 3/4, 4/5, 1], float)
x = np.linspace(0, xmax, N)

def chute(v0, alphav):
    return -g/(2*v0**2*np.cos(alphav)**2) * x**2 + x*np.tan(alphav)+z0

z = np.zeros((len(alphav), N), dtype=float)

for j in range(len(alphav)):
    z[j, :] = chute(v0, alphav[j])

zlim = v0**2/(2*g) - g/(2*v0**2)*x**2 +z0

plt.figure(1)
plt.ylim(bottom = 0, top=6)
plt.xlim(0, 0.3*xmax)
for j in range(len(alphav)):
    plt.plot(x, z[j,:], label = 'alpha =' + str(round(alphav[j]*180/np.pi,1)) + 'degres')
plt.plot(x, zlim, '--', label = '$z_{max}$')
#plt.fill_between(x, zlim, 0, alpha=0.01, color = 'red')
plt.xlabel('$x$')
plt.ylabel('$z$')
plt.title('Tir à accéleration constante selon plusieurs angles')
plt.legend()
plt.grid(True)     

#plt.savefig('./acceleration_constante.png', format='png', dpi=96)

#plt.figure(2)
#plt.ylim(bottom = 0, top=6)
#plt.xlim(0, xmax)
#for i in range(len(v0)):
#    plt.plot(x, z[i,1,:])
#plt.grid(True)
#z = vchute(v0, alpha)
#z(0, 0, 0)