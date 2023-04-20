import FunctionHolder
from lab_s import plotter
from lab_s.singleMethods import simple_iteration
from phrases import *


def main():
    print(phrase_func_vars)
    eq_id = int(input("Ваш выбор: "))

    fholder = FunctionHolder.FunctionHolder(eq_id)

    print("Введите начальное приближение:")
    x = [float(val) for val in input().split()]
    while len(x) != fholder.get_number_of_equations():
        print("Количество начальных приближений не совпадает с количеством уравнений!")
        print("Введите начальное приближение:")
        x = [float(val) for val in input().split()]

    eps = float(input("Введите критерий сходимости: "))

    if fholder.is_jacobi_convergent(x):
        print("Достаточное условие сходимости метода простых итераций выполнено!")
    else:
        print("Достаточное условие сходимости метода простых итераций НЕ выполнено!")
        return


    print("Решение системы методом простых итераций:")
    solution, iters = simple_iteration(x, fholder, eps)
    print("x =", solution, " за ", iters, "шагов")

    plotter.plot_function(fholder, solution)

    # Check the correctness of the solution
    print("Проверка правильности решения:")
    f_x = fholder.f(*solution)
    for i in range(len(f_x)):
        if abs(f_x[i]) > eps:
            print(f"Значение {f_x[i]} для уравнения {i + 1} не близко к 0 (дельта ", abs(f_x[i])," ), решение неверно")
            return
    print("Решение верно")


if __name__ == "__main__":
    main()
