# -*- coding: utf-8 -*-
"""Trace les figures du chap12."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# use latex for font rendering
mpl.rcParams["text.usetex"] = True


def Heavyside(x):
    return 0.5 * (np.sign(x) + 1)


a = -2
b = 5.0
N = 1000
t = np.linspace(a, b, N)

tau = 1
Gain = 1

U1 = Gain * (1 - np.exp(-t / tau)) * Heavyside(t)

# U1[0:(b-a)*N/2] = 0
U2 = 1 - U1

delta = N / (a - b)

fig1 = plt.figure(1)
plt.plot(t, U1)
plt.grid(True)
plt.xlabel(r"$t/\tau$")
plt.ylabel(r"$u/E$")

# fig2 = plt.figure(2)
# plt.plot(t, U2)
# plt.grid(True)
# plt.xlabel(r'$t/\tau$')
# plt.ylabel(r'$u/E$')
