import matplotlib.pyplot as plt
import numpy as np


def plot_function(fholder, x):
    fig, ax = plt.subplots()

    # Определяем область построения графика
    x_min = -5
    x_max = 5
    y_min = -5
    y_max = 5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    # Создаем сетку точек для построения графика
    x_vals = np.linspace(x_min, x_max, 500)
    y_vals = np.linspace(y_min, y_max, 500)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z1, Z2 = fholder.f(X, Y)

    # Строим график
    ax.contour(X, Y, Z1, levels=[0], colors='blue')
    ax.contour(X, Y, Z2, levels=[0], colors='red')
    ax.scatter(x[0], x[1], marker='o', color='green')

    ax.set_xlabel('x')
    ax.set_ylabel('y')

    plt.show()
