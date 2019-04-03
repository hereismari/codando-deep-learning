import numpy as np
import matplotlib.pyplot as plt


def generate_linear_relation(a, b, x_range=(0, 10), N=100, noise=True):
    x = np.random.uniform(low=x_range[0], high=x_range[1], size=(N, 1))
    y = a * x + b + np.random.randn(N, 1)
    return np.column_stack((x, y))


def plot(x, y=None):
    if y is None:
        y = x
        x = np.zeros(x.shape) + np.random.randn(x.shape[0])
        plt.xticks([], [])
    plt.plot(x, y, 'o', alpha=0.5)


def plot_vectors(vecs, colors=['red'], alpha=1):
    """
    Plot set of vectors.

    Parameters
    ----------
    vecs : array-like
        Coordinates of the vectors to plot. Each vectors is in an array. For
        instance: [[1, 3], [2, 2]] can be used to plot 2 vectors.
    cols : array-like
        Colors of the vectors. For instance: ['red', 'blue'] will display the
        first vector in red and the second in blue.
    alpha : float
        Opacity of vectors
   """
    for i in range(len(vecs)):
        x = vecs[i]
        plt.quiver([x[0][0]],
                   [x[0][1]],
                   [x[1][0]],
                   [x[1][1]],
                   angles='xy', scale_units='xy', scale=1, color=colors[i],
                  alpha=alpha)