# -*- coding: utf-8 -*-
"""Trace le tir parabolique freiné."""

from itertools import cycle
import numpy as np
from scipy.integrate import odeint
# from scipy import integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["text.usetex"] = True
# from labellines import labelLines


def chute_frot(y, t, g0, msurk, gamma):
    """Renvoie."""
    _, _, vx, vz = y
    ax_o = -msurk * np.abs(vx) ** gamma
    az_o = -g0 - msurk * np.abs(vz) ** gamma
    return [vx, vz, ax_o, az_o]


x0, z0, V0, n = 0, 0, 20, 8
theta = (1 / 2 - 1 / n) * np.pi
thetadeg = np.ceil(theta * 180 / np.pi)
Vz0, Vx0 = V0 * np.sin(theta), V0 * np.cos(theta)
t = np.linspace(0, 30, 10000)
g, ksurm, gamma = 9.81, 0.1, 1.5
y0 = [x0, z0, Vx0, Vz0]

lines = ["-", "--", "-.", ":"]
linecycler = cycle(lines)

sol0 = odeint(chute_frot, y0, t, args=(g, ksurm, 0))
# index pour lequel z devient negatif
END0 = np.where(sol0[:, 1] < 0, sol0[:, 1], -np.inf).argmax()

cm = 1 / 2.54  # centimeters in inches
for gamma in [0.5, 0.707, 1]:
    figsize = (20 * cm, 15 * cm)
    fig, ax = plt.subplots()
    plt.plot(sol0[:END0, 0], sol0[:END0, 1], label=r"$k/m=0$", ls="-")
    for ksurm in [0.1, 0.2, 0.5, 0.707, 1]:
        sol = odeint(chute_frot, y0, t, args=(g, ksurm, gamma))
        END = 10 + np.where(sol[:, 1] < 0, sol[:, 1], -np.inf).argmax()
        plt.plot(
            sol[:END, 0],
            sol[:END, 1],
            # label=f'$k/m={ksurm:.1f},\\alpha={gamma:.1f}$',
            label=f"$k/m={ksurm:.1f}$",
            ls=next(linecycler),
        )

    plt.legend(loc="best")
    lines = ax.get_lines()
    xvals = [22, 18, 10.5, 20, 14, 7.46, 18, 11.53, 6.09, 30]
    plt.xlabel("$x$")
    plt.ylabel("$z$")
    plt.ylim([0, 20])
    plt.xlim([0, 35])
    props = {"boxstyle": "round", "facecolor": "wheat", "alpha": 0.5}
    title = f"$V_0={V0} m/s$, $\\alpha={gamma}$, $\\theta={thetadeg}$"
    title += "° selon les types de frottements $f$"
    plt.title(title, bbox=props)
    plt.grid()
    plt.tight_layout()
    dpi = 200
    plt.savefig(f"Tir_parabolique_frottements_alpha_{gamma:.1f}.png", dpi=dpi)
plt.close()
