# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:07:20 2020

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
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

theta = np.linspace(0, np.pi/2, 100)

N = 10000
g = 9.81
z0 = 0
xmax = 40
alphav = np.pi*np.array([1.0/16, 1.0/8, 1.0/6, 1.0/5, 1.0/4, 0.5-1.0/5, 0.5-1.0/6, 0.5-1.0/8, 0.5-1/16.0], float)
v0 = np.sqrt(2*g)#*np.array([0, 1/2, 2/3, 3/4, 4/5, 1], float)
x = np.linspace(0, xmax, N)

def chute(v0, alphav, x):
    return -g/(2*v0**2*np.cos(alphav)**2) * x**2 + x*np.tan(alphav)+z0

z = np.zeros((len(alphav), N), dtype=float)
z_enveloppe = v0**2/(2*g) - g/(2*v0**2)*x**2 +z0
for j in range(len(alphav)):
    z[j, :] = chute(v0, alphav[j], x)

fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
fig.set_size_inches(8,6)
ax.set_ylim(bottom = 0, top=1.5)
ax.set_xlim(0, 5./2)
for j in range(len(alphav)):
    ax.plot(x, z[j,:], label = r'$\alpha = $ ' + str(round(alphav[j]*180/np.pi,1)) + ' degres')
ax.plot(x, z_enveloppe, '--', label = 'enveloppe')
e = mpl.patches.Ellipse((0, 0.5*(z0+v0**2/(2*g))), v0**2/(1*g) ,v0**2/(2*g), fill=False, ls='-.', label = 'max')
ax.add_artist(e)
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$z$', fontsize=14)
#plt.title('Tir à accéleration constante selon plusieurs angles')
ax.legend()
ax.grid(True)     

#plt.savefig('./acceleration_constante.png', format='png', dpi=1200)
#plt.savefig('./acceleration_constante.svg')

#plt.figure(2)
#plt.ylim(bottom = 0, top=6)
#plt.xlim(0, xmax)
#for i in range(len(v0)):
#    plt.plot(x, z[i,1,:])
#plt.grid(True)
#z = vchute(v0, alpha)
#z(0, 0, 0)
