import matplotlib.pyplot as plt
import numpy as np


def draw_tree(x, y, length, angle, level, ax):
    if level == 0:
        return

    x1 = x + length * np.cos(angle)
    y1 = y + length * np.sin(angle)

    ax.plot([x, x1], [y, y1], color="brown")

    new_length = length / np.sqrt(2)

    draw_tree(x1, y1, new_length, angle + np.pi / 4, level - 1, ax)
    draw_tree(x1, y1, new_length, angle - np.pi / 4, level - 1, ax)


if __name__ == "__main__":
    level = int(input("Enter the recursion level (e.g. 10): "))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    draw_tree(0, 0, 100, np.pi / 2, level, ax)

    plt.show()
