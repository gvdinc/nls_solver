def simple_iteration(x0, fholder, eps=1e-6, max_iter=100):
    x_old = x0.copy()
    n = fholder.get_number_of_equations()
    x_new = [0] * n
    for i in range(max_iter):
        for j in range(n):
            s = 0
            for k in range(n):
                if k != j:
                    s += fholder.df(*x_old)[j][k] * x_old[k]
            if fholder.df(*x_old)[j][j] != 0:
                x_new[j] = x_old[j] - fholder.f(*x_old)[j] / fholder.df(*x_old)[j][j] - s / fholder.df(*x_old)[j][j]
            else:
                x_new[j] = x_old[j]
        if max([abs(x_new[i] - x_old[i]) for i in range(n)]) < eps:
            return x_new, i
        x_old = x_new.copy()
    raise ValueError("Failed to converge in {} iterations".format(max_iter))

