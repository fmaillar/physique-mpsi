# -*- coding: utf-8 -*-
"""Trace les figures du chap12."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# use latex for font rendering
mpl.rcParams["text.usetex"] = True


def Heavyside(x):
    """Define the Heavyside function."""
    return 0.5 * (np.sign(x) + 1)


a, b, n = -2, 5.0, 1000
tau, gain = 1, 1
delta = n / (a - b)
t = np.linspace(a, b, n)


u1 = gain * (1 - np.exp(-t / tau)) * Heavyside(t)
u2 = 1 - u1


fig1 = plt.figure(1)
plt.plot(t, u1)
plt.grid(True)
plt.xlabel(r"$t/\tau$")
plt.ylabel(r"$u/E$")

# fig2 = plt.figure(2)
# plt.plot(t, U2)
# plt.grid(True)
# plt.xlabel(r'$t/\tau$')
# plt.ylabel(r'$u/E$')
