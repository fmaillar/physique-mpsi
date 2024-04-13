#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 01:42:00 2024.

@author: florian
"""

# from itertools import product
import numpy as np
import matplotlib.pyplot as plt


def plot_potential_curve(a, b, c):
    """Ploit the curve."""
    r = np.linspace(0.05, 10, 10_000)
    ep = a/r + b/r**2 + c/r**3
    plt.figure(dpi=200)
    plt.plot(r, ep)
    plt.xlabel("$r$")
    plt.ylabel("$Ep(r)$")
    plt.ylim([-3, 3])
    plt.xlim([0, 4])
    plt.grid(which='both')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    text = r"$Ep(r) = \frac{a}{r} + \frac{b}{r^2} + \frac{c}{r^3}$" + "\n"
    text += f"$a={a}, b={b}, c={c}$"
    plt.text(2, 2.3, text)
    plt.xticks([])
    plt.yticks([-1.75, -0.8, 1.8, 2.8],
               labels=[r"$E_0$", r"$E_3$", r"$E_2$", r"$E_1$"])
    # plt.show()
    plt.savefig('puits_potentiel.png', dpi=200)


plot_potential_curve(3.9, -1.8, 0.19)
# list_a = [3.8, 3.9, 4.0]
# list_b = [-1.7, -1.8, -1.9]
# list_c = [0.18, 0.19, 0.20]
# for a, b, c in product(list_a, list_b, list_c):
#     plot_potential_curve(a, b, c)
