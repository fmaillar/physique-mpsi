#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trace les figure du chapitre1."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["text.usetex"] = True

theta = np.linspace(0, np.pi / 2, 100)

N = 10000
g = 9.81
z0 = 0
xmax = 40
alphav = np.pi * np.array(
    [
        1.0 / 16,
        1.0 / 8,
        1.0 / 6,
        1.0 / 5,
        1.0 / 4,
        0.5 - 1.0 / 5,
        0.5 - 1.0 / 6,
        0.5 - 1.0 / 8,
        0.5 - 1 / 16.0,
        ],
    float,
    )
v0 = np.sqrt(2 * g)  # *np.array([0, 1/2, 2/3, 3/4, 4/5, 1], float)
x = np.linspace(0, xmax, N)


def chute(v0_i, alphav_i, x_i):
    """Retourne la chute paramétrée."""
    chute_o = -g / (2 * v0_i ** 2 * np.cos(alphav_i) ** 2) * x_i ** 2
    chute_o += x_i * np.tan(alphav_i) + z0
    return chute_o


z = np.zeros((len(alphav), N), dtype=float)
z_enveloppe = v0 ** 2 / (2 * g) - g / (2 * v0 ** 2) * x ** 2 + z0
for j, alpha in enumerate(alphav):
    z[j, :] = chute(v0, alpha, x)

fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
fig.set_size_inches(8, 6)
ax.set_ylim(bottom=0, top=1.5)
ax.set_xlim(0, 5.0 / 2)
for j, alpha in enumerate(alphav):
    ax.plot(
        x,
        z[j, :],
        label=r"$\alpha = $ " + str(round(alpha * 180 / np.pi, 1)) + " degres",
        )
ax.plot(x, z_enveloppe, "--", label="enveloppe")
e = mpl.patches.Ellipse(
    (0, 0.5 * (z0 + v0 ** 2 / (2 * g))),
    v0 ** 2 / (1 * g),
    v0 ** 2 / (2 * g),
    fill=False,
    ls="-.",
    label="max",
    )
ax.add_artist(e)
plt.xlabel(r"$x$", fontsize=14)
plt.ylabel(r"$z$", fontsize=14)
# plt.title('Tir à accéleration constante selon plusieurs angles')
ax.legend()
ax.grid(which="both")

plt.savefig("acceleration_constante.png")
