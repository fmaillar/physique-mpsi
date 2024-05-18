#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trace un schema mecanique."""
import matplotlib.pyplot as plt
import numpy as np


class ForceVector:
    """Definit la classe force_vecteur."""
    def __init__(self, name, start, force, **kwargs):
        self.name = name
        self.start = start
        self.force = force
        self.kwargs = kwargs

    def draw(self, ax):
        """Dessine le vecteur."""
        ax.quiver(
            self.start[0],
            self.start[1],
            self.force[0],
            self.force[1],
            angles="xy",
            scale_units="xy",
            scale=1,
            **self.kwargs
            )
        ax.text(
            self.start[0] + self.force[0] * 0.5,
            self.start[1] + self.force[1] * 0.5,
            self.name,
            fontsize=10,
            ha="center",
            )


def draw_mechanical_diagram(vectors):
    """Dessines le diagramme."""
    fig, ax = plt.subplots()
    ax.set_aspect("equal")

    for vector in vectors:
        vector.draw(ax)

    # Get the min and max values for x and y coordinates
    x_values = ([vector.start[0] for vector in vectors] +
                [vector.start[0] + vector.force[0] for vector in vectors])
    y_values = ([vector.start[1] for vector in vectors] +
                [vector.start[1] + vector.force[1] for vector in vectors])
    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    # Set the limits for plotting with some padding
    padding = 1
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(min_y - padding, max_y + padding)

    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, which="both")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Mechanical Diagram")

    plt.show()


# Example usage:
if __name__ == "__main__":
    # Define vectors
    list_vectors = [
        ForceVector("F1", (0, 0), (0, -4), color="r", linewidth=2),
        ForceVector("F2", (0, 0), (2, 2), color="b", linewidth=2),
        ForceVector("F3", (0, 0), (-2, 2), color="g", linewidth=2),
        ]

    # Draw diagram
    draw_mechanical_diagram(list_vectors)
