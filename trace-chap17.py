# -*- coding: utf-8 -*-
"""Trace les figures du chap17."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# use latex for font rendering
mpl.rcParams["text.usetex"] = True
plt.rcParams.update({"font.size": 9})


def fun(omega_i, q):
    """Compute phi."""
    xi = ((1 - omega_i**2) ** 2 + omega_i**2 / q**2) ** (-0.5)
    phi = (np.arctan(q * (1 / omega_i - omega_i)) - np.pi / 2) * 180 / np.pi
    return [xi, phi]


def fun2(omega_i, q):
    """Compute psi."""
    xi = (q**2 * (omega_i - 1.0 / omega_i) ** 2 + 1) ** (-0.5)
    psi = np.arctan(q * (1.0 / omega_i - omega_i)) * 180 / np.pi
    return [xi, psi]


omega = np.linspace(0.01, 3, 300)
xi_max = [(1 - i**4) ** (-0.5) for i in omega if i < 1]
nx = len(xi_max)
ql = [1 / 4, 1 / np.sqrt(2), 1, 2, 4]
qla = np.array(ql)
a_list = [fun(omega, qi) for qi in ql]
nsubfig = 2
array_i = np.array(a_list)
label = ["$\\xi = \\frac{X}{X_0}$", "$\\Phi$ (deg)"]

fig, axs = plt.subplots(nsubfig, 1, figsize=(6, 10), dpi=200)
for i in range(nsubfig):
    if i == 0:
        axs[i].plot(omega[:nx], xi_max, c="red", ls="--", label="$\\xi_m$")
    for k in range(len(ql)):
        axs[i].plot(omega, array_i[k, i, :], label=str(np.around(ql[k], 3)))
    axs[i].grid(True, which="both")
    axs[i].set_ylabel(label[i])
    axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
    axs[i].legend(loc="best")
plt.tight_layout()
plt.savefig("Fig17.png")
plt.close(fig)

list2 = [fun2(omega, q) for q in ql]
array2 = np.array(list2)
label2 = ["$\\xi = \\frac{V}{V_M}$", "$\\Psi$ (deg)"]
fig, axs = plt.subplots(nsubfig, 1, figsize=(6, 10), dpi=200)
for i in range(nsubfig):
    for k, q in enumerate(ql):
        axs[i].plot(omega, array2[k, i, :], label=str(np.around(q, 3)))
    axs[i].grid(True, which="both")
    axs[i].set_ylabel(label2[i])
    axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
    axs[i].legend(loc="best")
plt.tight_layout()
plt.savefig("Fig17-2.png")
plt.close(fig)

fig, ax = plt.subplots(1, 1, dpi=200)
for k, q in enumerate(ql):
    plt.plot(omega, array2[k, 0, :] ** 2, label=str(np.around(q, 3)))
ax.grid(True, which="both")
ax.set_ylabel("$\\tau = \\frac{P}{P_M}$")
ax.set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig("Fig17-3.png")
plt.close(fig)
