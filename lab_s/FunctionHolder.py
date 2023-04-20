import inspect


class FunctionHolder:
    def __init__(self, eq_id):
        self.eq_id = eq_id

    def f(self, x1, x2):
        if self.eq_id == 1:
            return [
                x1 ** 2 - x2 - 1,
                x1 - x2 ** 2 + 1
            ]
        elif self.eq_id == 2:
            return [
                x1 ** 2 + x2 ** 2 - 1,
                x1 - x2
            ]
        elif self.eq_id == 3:
            return [
                x1 ** 2 - x2 ** 2 - 2,
                x1 + x2 ** 2 - 2
            ]
        else:
            raise ValueError("Unsupported equation ID")

    def df(self, x1, x2):
        if self.eq_id == 1:
            return [
                [2 * x1, -1],
                [1, -2 * x2]
            ]
        elif self.eq_id == 2:
            return [
                [2 * x1, 2 * x2],
                [1, -1]
            ]
        elif self.eq_id == 3:
            return [
                [2 * x1, -2 * x2],
                [1, 2 * x2]
            ]
        else:
            raise ValueError("Unsupported equation ID")

    def get_number_of_equations(self):
        return 2

    def is_jacobi_convergent(self, x):
        n = self.get_number_of_equations()
        A = self.df(*x)
        B = [[-A[i][j] / A[i][i] if i != j and A[i][i] != 0 else 0 for j in range(n)] for i in range(n)]
        row_sums = [sum([abs(B[i][j]) for j in range(n)]) for i in range(n)]
        return max(row_sums) < 1
