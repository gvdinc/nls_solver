from FMenu import FMenu
from lab.plotter import plot_function
from phrases import *
from singleMethods import *
import FunctionHolder


def main():  # START input
    auto_mode = input("включить ввод из файла? Y/N ") == 'Y'
    if auto_mode:
        menu = FMenu()
        a, b, e = menu.choose_file()
        input()  # перехват нажатого enter
    else:
        a, b, e = map(float, input(phrase_params_input).split())
    is_valid = a is not None and b is not None and e is not None
    print((a, b, e) if is_valid else "неверный ввод")
    if not is_valid:
        return 1
    # Prompt user to select an equation
    print(phrase_func_vars)
    eq_id = int(input("Ваш выбор: "))
    # END input
    # TODO single solve logic
    fholder = FunctionHolder.FunctionHolder(eq_id)
    # метод половинного деления
    res, iters = None, 0
    try:
        res, iters = bisection(fholder, a, b, e, 50)
        print("ответ: ", round(res, len(str(e)) - 2), " получен за ", iters, " шагов", sep='')
    except Exception as e:
        print(":( Метод половинного деления sucks")
    # метод Ньютона
    try:
        res, iters = newton(fholder, (a + b) / 2, e, 50)  # За нач. приближение берём середину отрезка
        print("ответ: ", round(res, len(str(e)) - 2), " получен за ", iters, " шагов", sep='')
    except Exception as e:
        print(":( Метод Ньютона sucks")
    # метод Простой итерации
    try:
        res, iters = simple_iteration(fholder, a, b, e, 50)  # За нач. приближение берём середину отрезка
        print("ответ: ", round(res, len(str(e)) - 2), " получен за ", iters, " шагов", sep='')
    except Exception as e:
        print(":( Метод Простой итерации sucks")
    # TODO запись
    if input("Записать результат? Y/N ") == 'Y':
        file = open("result.txt", "w")
        file.write(str("ответ: " + str(res) + " получен за " + str(iters) + " шагов"))
        file.flush()
        file.close()
    # TODO graphic logic
    plot_function(fholder, a, b)


if __name__ == "__main__":
    main()
