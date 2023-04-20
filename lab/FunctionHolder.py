from math import cos, sin


class FunctionHolder:
    def __init__(self, func_id=1):
        self.id = func_id if (4 > func_id > 0) else 1

    def f(self, x):  # возвращает значение ф-ции
        if self.id == 1:
            return x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76  # из вар-та
        elif self.id == 2:
            return float(cos(x) + 2 * x - 0.5)
        else:
            return x ** 2 + x - 1

    def df(self, x):  # Возвращает знач. Производной f(x)
        if self.id == 1:
            return 3 * x ** 2 - 3.78 * x - 2
        elif self.id == 2:
            return float(-sin(x) + 2)
        else:
            return 2 * x + 1

    def ddf(self, x):  # Возвращает знач. 2ой Производной f(x)
        if self.id == 1:
            return 6 * x - 3.78
        elif self.id == 2:
            return float(-cos(x))
        else:
            return 2
