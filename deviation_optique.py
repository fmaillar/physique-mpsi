#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print the optic deviation."""

from itertools import product
from numpy import linspace, sin, arcsin, pi, arange
import matplotlib.pyplot as plt

COEF = 2 * pi / 360


def deviation(angle0, indice, eps):
    """Compute the deviation."""
    theta0 = arcsin(indice * sin(angle - arcsin(1 / indice))) / COEF + eps
    x0 = linspace(theta0, 90, num=1000) * COEF  # conversion en radians
    y1 = indice * sin(angle0 - arcsin(sin(x0) / indice))
    y0 = x0 + arcsin(y1) - angle0
    return x0 / COEF, y0 / COEF


list_angle = [pi / 4, pi / 6]
list_n = [1.1, 1.25, 1.5]
fig, ax = plt.subplots()
ax.minorticks_on()
for angle, n in list(product(list_angle, list_n)):
    x, y = deviation(angle, n, 0.001)
    plt.plot(
        x,
        y,
        label=r"$\theta=$" + f"{round(angle / COEF)}° " + r"$n=$" + f"{n}",
        linewidth=1.2,
        )
plt.legend(loc="upper center", fontsize=7)
plt.xlabel(r"Incidence $i (°)$")
plt.ylabel(r"Deviation $D (°)$")
plt.tick_params(axis="x", which="major", length=10, color="g")
plt.tick_params(axis="y", which="major", length=10, color="g",
                labelrotation=45.0)
ax.set_xticks(arange(-50, 100, 2), minor=True)
ax.set_yticks(arange(0, 60, 2), minor=True)
ax.grid(which="major", linestyle="--", linewidth="0.3", color="blue")
ax.grid(which="minor", linestyle="-", linewidth="0.1", color="black")
# ax.yaxis.set_label_coords(-55.0, 40.0)
plt.savefig("Deviation.png", dpi=240)
