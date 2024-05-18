#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trace les figures des reponses."""
import numpy as np
import matplotlib.pyplot as plt


class EquationHoraire:
    """Objet equation horaires."""

    def __init__(self, l_v, o0_v):
        self.l_v = l_v
        self.o0_v = o0_v
        self.cat = ('critique' if l_v == o0_v
                    else ('aperiodique' if l_v > o0_v else
                          'pseudo_periodique')
                    )
        self.t = np.linspace(0, 10, 1000)

    def __repr__(self):
        return f"Equation_horaire({self.l_v}, {self.o0_v})"

    def reponse(self):
        """Renvoie la réponse du système."""

        if self.cat == 'aperiodique':
            return self.regime_aperiodique()

        if self.cat == 'critique':
            return self.regime_critique()

        if self.cat == 'pseudo_periodique':
            return self.regime_pseudo_periodique()

    def regime_aperiodique(self):
        """Renvoie la réponse du régime apériodique."""
        return self.t, np.exp(-self.l_v * self.t) * (1 + self.l_v * self.t)

    def regime_critique(self):
        """Renvoie la réponse du régime critique."""
        return (self.t,
                np.exp(-self.l_v * self.t) * (1 + self.l_v * self.t +
                                              (self.l_v * self.t) ** 2 / 2))

    def regime_pseudo_periodique(self):
        """Renvoie la réponse du régime pseudo-périodique."""
        # pseudo-période
        omega = np.sqrt(self.o0_v ** 2 - self.l_v ** 2)

        return (self.t,
                np.exp(-self.l_v * self.t) * (np.cos(omega * self.t) + (
                        self.l_v / omega) * np.sin(omega * self.t)))

    def trace_reponse(self):
        """Trace la reponse en fonction du temps."""
        plt.figure()
        plt.title(f"Catégorie: {self.cat}")
        plt.xlabel('Temps')
        plt.ylabel('x(t)')


def tracer_figure_par_categorie(cat, list_eq):
    """Trace les figures pour une catégorie donnée."""
    plt.figure()
    plt.title(f"Catégorie: {cat}")
    plt.xlabel('Temps')
    plt.ylabel('x(t)')

    for eq_h in list_eq:
        t, x = eq_horaire.reponse()
        plt.plot(t, x, label=f"λ={eq_h.l_v}, ω0={eq_h.o0_v}")

    plt.legend()
    plt.grid(which='both')
    plt.savefig(f"Equation_horaires_{cat}.png")


# Définition des couples de paramètres (lambda, omega_0)
params = [
    (0.5, 1.0), (1.0, 1.5), (1.5, 2.0), (2.0, 2.5),
    (1.0, 0.5), (2.0, 1.0), (5.0, 3.0),
    (2.0, 2.0), (5.0, 5.0)
    ]

equations_horaires = [EquationHoraire(lbd_v, om0_v) for lbd_v, om0_v in params]

# Dictionnaire pour organiser les objets par catégorie
categories = {'aperiodique': [], 'critique': [], 'pseudo_periodique': []}

# Itérer sur chaque objet et les ajouter à la liste dans le dictionnaire
for equations_horaire in equations_horaires:
    categories[equations_horaire.cat].append(equations_horaire)

# Tracé des figures pour chaque catégorie non vide
for category, params in categories.items():
    tracer_figure_par_categorie(category, params)
