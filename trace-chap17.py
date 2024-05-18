#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trace les figures du chap17."""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# use latex for font rendering
mpl.rcParams["text.usetex"] = True
plt.rcParams.update({"font.size": 9})


def configure_plot(func):
    """Decorator to configure the plot."""

    def wrapper(*args, **kwargs):
        """Decore la fonction func."""
        fig, axs = func(*args, **kwargs)
        plt.tight_layout()
        plt.savefig(kwargs.get("filename", "figure.png"))
        plt.close(fig)

    return wrapper


class Plotter:
    """Definit la classe de tracé."""
    def __init__(self, om, q):
        self.omega = om
        self.ql = q

    @staticmethod
    def fun(omega_i, q):
        """Compute phi."""
        xi = ((1 - omega_i**2) ** 2 + omega_i**2 / q**2) ** (-0.5)
        phi = ((np.arctan(q * (1 / omega_i - omega_i))
                - np.pi / 2) * 180 / np.pi)
        return [xi, phi]

    @staticmethod
    def fun2(omega_i, q):
        """Compute psi."""
        xi = (q**2 * (omega_i - 1.0 / omega_i) ** 2 + 1) ** (-0.5)
        psi = np.arctan(q * (1.0 / omega_i - omega_i)) * 180 / np.pi
        return [xi, psi]

    @configure_plot
    def plot_figure_1(self, filename):
        """Plot the first set of figures."""
        xi_max = [(1 - i**4) ** (-0.5) for i in self.omega if i < 1]
        nx = len(xi_max)
        a_list = [self.fun(self.omega, qi) for qi in self.ql]
        array_i = np.array(a_list)
        label = ["$\\xi = \\frac{X}{X_0}$", "$\\Phi$ (deg)"]

        fig, axs = plt.subplots(2, figsize=(6, 10), dpi=200)
        for i in range(2):
            if i == 0:
                axs[i].plot(self.omega[:nx], xi_max, c="red", ls="--",
                            label="$\\xi_m$")
            for k in range(len(self.ql)):
                axs[i].plot(
                    self.omega, array_i[k, i, :],
                    label=str(np.around(self.ql[k], 3))
                    )
            axs[i].grid(True, which="both")
            axs[i].set_ylabel(label[i])
            axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
            axs[i].legend(loc="best")
        return fig, axs

    @configure_plot
    def plot_figure_2(self, filename):
        """Plot the second set of figures."""
        list2 = [self.fun2(self.omega, q) for q in self.ql]
        array2 = np.array(list2)
        label2 = ["$\\xi = \\frac{V}{V_M}$", "$\\Psi$ (deg)"]

        fig, axs = plt.subplots(2, figsize=(6, 10), dpi=200)
        for i in range(2):
            for k, q in enumerate(self.ql):
                axs[i].plot(self.omega, array2[k, i, :],
                            label=str(np.around(q, 3)))
            axs[i].grid(True, which="both")
            axs[i].set_ylabel(label2[i])
            axs[i].set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
            axs[i].legend(loc="best")
        return fig, axs

    @configure_plot
    def plot_figure_3(self, filename):
        """Plot the third figure."""
        list2 = [self.fun2(self.omega, q) for q in self.ql]
        array2 = np.array(list2)

        fig, ax = plt.subplots(dpi=200)
        for k, q in enumerate(self.ql):
            ax.plot(self.omega, array2[k, 0, :] ** 2,
                    label=str(np.around(q, 3)))
        ax.grid(True, which="both")
        ax.set_ylabel("$\\tau = \\frac{P}{P_M}$")
        ax.set_xlabel("$\\Omega = \\frac{\\omega}{\\omega_0}$")
        ax.legend(loc="best")
        return fig, ax


# Utilisation des classes et fonctions
omega = np.linspace(0.01, 3, 300)
ql = [1 / 4, 1 / np.sqrt(2), 1, 2, 4]

plotter = Plotter(omega, ql)
plotter.plot_figure_1(filename="Fig17.png")
plotter.plot_figure_2(filename="Fig17-2.png")
plotter.plot_figure_3(filename="Fig17-3.png")
