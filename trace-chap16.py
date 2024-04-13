# -*- coding: utf-8 -*-
"""Trace les figures du chap16."""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import signal

# use latex for font rendering
mpl.rcParams["text.usetex"] = True

H0 = 10

sys = signal.TransferFunction([-H0], [1, 1])
L = 1000
f = np.logspace(-2, 2, num=L)
w, mag, phase = signal.bode(sys, f)

# Cherche l'index de la coupure (1)
# IC = np.where(w == 1)[0][0]
IC = int(L / 2)

# Definition des asymptotes
G1 = 20 * np.log10(H0) * np.ones(IC + 1)
Phi1 = 180 * np.ones(IC + 1)

G2 = 20 * np.log10(H0 / w[IC:])
Phi2 = 90 * np.ones(len(w) - IC)

fig, axs = plt.subplots(2, 1, sharex=True)
axs[0].semilogx(w, mag)
axs[0].semilogx(w[: (IC + 1)], G1, c="red", ls="--")
axs[0].semilogx(w[IC:], G2, c="red", ls="--")
axs[0].annotate(
    "Cutoff, $G =$" + str(np.around(mag[IC], decimals=0)),
    xy=(w[IC], mag[IC]),
    xytext=(w[IC] + 3, mag[IC]),
    arrowprops=dict(facecolor="black", shrink=0.05, width=0.2, frac=0.2),
)
axs[0].grid(True, which="both")
# axs[0].set_xlabel("$x = \omega/\omega_0$")
axs[0].set_ylabel("$G = 20\log(H)$ (dB)")
axs[1].semilogx(w, phase)
axs[1].semilogx(w[: (IC + 1)], Phi1, c="red", ls="--")
axs[1].semilogx(w[IC:], Phi2, c="red", ls="--")
axs[1].annotate(
    "Cutoff, $\Phi =$" + str(np.around(phase[IC], decimals=0)),
    xy=(w[IC], phase[IC]),
    xytext=(w[IC] + 3, phase[IC]),
    arrowprops=dict(facecolor="black", shrink=0.05, width=0.2, frac=0.2),
)

axs[1].grid(True, which="both")
axs[1].set_xlabel("$x = \omega/\omega_0$")
axs[1].set_ylabel("$\Phi = Arg(H)$ (deg)")
plt.suptitle("Magnitude and phase Bode Plot of $H=H_0/(1+jx)$")
plt.tight_layout()
plt.savefig("Fig12.png", dpi=300)
# plt.close(fig)
