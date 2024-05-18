"""Trace les portrais de phase."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


class PortraitPhase:
    """Définit la classe objet Portrait de phase."""

    def __init__(
        self,
        nom: str,
        func,
        l_param: list,
        param_name: str,
        titre: str,
        t0: int = 0,
        tinf: int = 50,
    ):
        """Init the class."""
        self.nom = nom
        self.func = func
        self.l_param = l_param
        self.t0 = t0
        self.tinf = tinf
        self.param_name = param_name
        self.titre = titre

    def calc(self):
        """Compute the solution of differential equation."""
        time = np.linspace(self.t0, self.tinf, 1000)
        y0 = [1.0, 0.0]
        return [
            solve_ivp(
                lambda t, y: self.func(t, y, p), [time[0], time[-1]], y0, t_eval=time
            )
            for p in self.l_param
        ]

    def plot_portrait(self):
        """Affiche le portrait de phase."""
        sols = self.calc()
        plt.figure()
        for sol, param in zip(sols, self.l_param):
            plt.plot(sol.y[0], sol.y[1], label=f"{self.param_name}={param:.3f}")

        plt.xlabel("ξ")
        plt.ylabel("ξ'")
        plt.title(self.titre)
        plt.legend()
        plt.grid(True)
        plt.savefig(f"{self.nom}.png", dpi=250)


def oscillator(t, y, omega0):
    """Return the pure oscillator."""
    xi, xi_prime = y
    xi_double_prime = -(omega0**2) * xi
    return [xi_prime, xi_double_prime]


def damped_oscillator(t, y, Qu):  # Définition de l'équation différentielle
    """Return the damped oscillator."""
    xi, xi_prime = y
    xi_double_prime = -xi_prime / Qu - xi
    return [xi_prime, xi_double_prime]


oscillateur_pur = PortraitPhase(
    "portrait_de_phase_osc_pur",
    oscillator,
    [1.0 / 3, 1.0 / 2, 1, 2, 3],
    "omega_0",
    "oscillateur pur",
)
oscillateur_pur.plot_portrait()

oscillateur_amorti = PortraitPhase(
    "portrait_de_phase_osc_amt",
    damped_oscillator,
    [
        1.5,
        1.25,
        1,
        (0.5) ** 0.5,
        0.5,
    ],
    "Q",
    "oscillateur amorti",
)
oscillateur_amorti.plot_portrait()
