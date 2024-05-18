#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trace les reponses aux impulsions."""
import numpy as np
import matplotlib.pyplot as plt
import control

dt = 0.01
t = np.arange(0, 40, dt)
u = np.sin(2*t)

# Définition de la fonction de transfert
numerator = [1]  # Numérateur de la fonction de transfert
denominator = [1, 2*0.5, 1.25**2]  # Dénominateur de la fonction de transfert

# Création de l'objet de la fonction de transfert
sys = control.TransferFunction(numerator, denominator)

# Calcul et traçage de la réponse impulsionnelle
t_imp, y_imp = control.impulse_response(sys, T=t)
plt.plot(t, y_imp, label='Réponse impulsionnelle')

# Calcul et traçage de la réponse indicielle
t_step, y_step = control.step_response(sys, T=t)
plt.plot(t, y_step, label='Réponse indicielle')

# Calcul et traçage de la réponse à une rampe
# Convolution de t avec y_step, puis échantillonnage
# y_ramp = np.convolve(t, y_step, 'full')[:len(t)/4] * dt
# t_ramp = t
t_ramp, y_ramp = control.forced_response(sys, T=t, U=u)
plt.plot(t, y_ramp, label='Réponse à une rampe')

# Réglages du tracé
plt.xlabel('Temps')
plt.ylabel('Réponse')
plt.title('Réponses du système')
plt.legend()
plt.grid()
plt.show()
