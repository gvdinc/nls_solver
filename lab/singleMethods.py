import numpy as np

import FunctionHolder


# Implement numerical methods as separate functions
def bisection(fholder, a, b, e, max_iter):
    print("Метод половинного деления")
    if fholder.f(a) * fholder.f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs")
        return None
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(fholder.f(c)) < e:
            return c, i + 1
        elif fholder.f(a) * fholder.f(c) < 0:
            b = c
        else:
            a = c
    print("Error: maximum number of iterations reached")
    return None


def newton(fholder, x0, e, max_iter):
    print("Метод Ньютона")
    for i in range(max_iter):
        fx = fholder.f(x0)
        if abs(fx) < e:
            return x0, i + 1
        fpx = fholder.df(x0)
        if fpx == 0:
            print("Error: f'(x) is zero")
            return None
        x0 = x0 - fx / fpx
    print("Error: достигнуто макс. кол-во операций")
    return None


def simple_iteration(fholder, a, b, e, max_iter):
    print("Метод простой итерации")
    x0 = (a + b) / 2
    # проверяем достаточное условие сходимости на интервале [a, b]
    df = fholder.df(a)
    for x in np.linspace(a, b, 100):
        df = max(df, abs(fholder.df(x)))
    if df >= 1:
        print("Не выполнено дост. усл. сх. на [{}, {}]!".format(a, b))

    phi = lambda x: x - fholder.f(x) / fholder.df(x)  # определяем phi как функцию x - f(x) / f'(x)
    for i in range(max_iter):
        x1 = phi(x0)
        if abs(x1 - x0) < e:
            return x1, i + 1
        x0 = x1
    print("Error: достигнуто макс. кол-во операций")
    return None
