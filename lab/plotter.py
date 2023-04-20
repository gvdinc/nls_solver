import matplotlib.pyplot as plt
import numpy as np


def plot_function(fholder, a, b):
    x = np.linspace(a - 1, b + 1, 1000)
    y = [fholder.f(xi) for xi in x]
    plt.plot(x, y)
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
