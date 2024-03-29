# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:35:12 2022

@author: e_fmaill
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# use latex for font rendering
mpl.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 9})

def fun(Omega, Q):
    xi = ((1-Omega**2)**2+Omega**2/Q**2)**(-0.5)
    phi = (np.arctan(Q*(1/Omega-Omega))-np.pi/2)*180/np.pi
    return [xi, phi, Omega]

def fun2(Omega, Q):
    xi = (Q**2*(Omega-1./Omega)**2+1)**(-0.5)
    psi = np.arctan(Q*(1./Omega-Omega))*180/np.pi
    return [xi, psi, Omega]

Omega = np.linspace(0.01, 3, 300)
XiMax = [(1-i**4)**(-0.5) for i in Omega if i < 1]
Nx = len(XiMax)
Ql = [1/4, 1/np.sqrt(2), 1, 2, 4]
Qla = np.array(Ql)
List = [fun(Omega, Q) for Q in Ql]
Nsubfig = 2
Array = np.array(List)
label = ['$\\xi = \\frac{X}{X_0}$', '$\\Phi$ (deg)']

fig, axs = plt.subplots(Nsubfig, 1, figsize=(6, 10), dpi=200)
for i in range(Nsubfig):
    if i == 0:
        axs[i].plot(Omega[:Nx], XiMax, c='red', ls='--', label='$\\xi_m$')
    for k in range(len(Ql)):
        axs[i].plot(Omega, Array[k, i, :], label=str(np.around(Ql[k], 3)))
    axs[i].grid(True, which='both')
    axs[i].set_ylabel(label[i])
    axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
    axs[i].legend(loc='best')
plt.tight_layout()
plt.savefig("Fig17.png")
plt.close(fig)

List2 = [fun2(Omega, Q) for Q in Ql]
Array2 = np.array(List2)
label2 = ['$\\xi = \\frac{V}{V_M}$', '$\\Psi$ (deg)']
fig, axs = plt.subplots(Nsubfig, 1, figsize=(6, 10), dpi=200)
for i in range(Nsubfig):
    for k in range(len(Ql)):
        axs[i].plot(Omega, Array2[k, i, :], label=str(np.around(Ql[k], 3)))
    axs[i].grid(True, which='both')
    axs[i].set_ylabel(label2[i])
    axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
    axs[i].legend(loc='best')
plt.tight_layout()
plt.savefig("Fig17-2.png")
plt.close(fig)

fig, ax = plt.subplots(1, 1, dpi=200)
for k in range(len(Ql)):
    plt.plot(Omega, Array2[k, 0, :]**2, label=str(np.around(Ql[k], 3)))
ax.grid(True, which='both')
ax.set_ylabel("$\\tau = \\frac{P}{P_M}$")
ax.set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
ax.legend(loc='best')
plt.tight_layout()
plt.savefig("Fig17-3.png")
plt.close(fig)

