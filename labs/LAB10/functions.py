import math as m


def func(x):  # функция для интегрирования
    y = x**2
    return y


def antiderivative_func(x):  # первообразная
    y = x**3/3
    return y


def right_rectangle(start, stop, n, eps):  # функция вычисления интеграла методом правых прямоугольников
    start, stop = min(start, stop), max(start, stop)
    delta = (stop - start)/n
    s = 0.0
    while abs(stop - start) > eps:
        s += func(stop)*delta
        stop -= delta
    return s


def trapeze(start, stop, n, eps):  # функция вычисления интеграла методом трапеций
    start, stop = min(start, stop), max(start, stop)
    delta = (stop - start) / n
    s = 0.0
    while abs(stop - start) > eps:
        start += delta
        s += ((func(start) + func(start - delta))/2) * delta
    return s


def integral(start, stop):  # вычисление интеграла через первообразную
    return antiderivative_func(stop) - antiderivative_func(start)


def absolute_error(value, true_value):  # вычисление абсолютной погрешности
    return abs(true_value - value)


def relative_error(value, true_value):  # вычисление относительной погрешности
    if true_value != 0:
        return (absolute_error(value, true_value)/true_value) * 100
    else:
        return (absolute_error(value, true_value) / 0.01) * 100


def print_out(a, b, n1, n2, eps):  # вывод таблицы значений методов интегрирования
    print("_" * 64)
    s = "|{:^20s}|{:^20.5g}|{:^20.5g}|".format("", n1, n2)
    print(s)
    s = "|{:^20s}|{:^20.7g}|{:^20.7g}|".format("Right rects", right_rectangle(a, b, n1, eps),
                                               right_rectangle(a, b, n2, eps))
    print(s)
    s = "|{:^20s}|{:^20.7g}|{:^20.7g}|".format("Trapeze", trapeze(a, b, n1, eps), trapeze(a, b, n2, eps))
    print(s)
    print("‾" * 64)


def print_errors(true_value, n1, n2, values):  # вывод таблиц значений погрешностей методов интегрирования
    print("True value of integral: {:<20.7g}".format(true_value))

    print("Errors:")
    print("Right rects: ")
    print("_" * 64)
    s = "|{:^20s}|{:^20s}|{:^20s}|".format("", "Absolute error", "Relative error")
    print(s)
    s = "|{:^20.7g}|{:^20.7g}|{:^20.7g}|".format(n1, absolute_error(values[0], true_value),
                                                 relative_error(values[0], true_value))
    print(s)
    s = "|{:^20.7g}|{:^20.7g}|{:^20.7g}|".format(n2, absolute_error(values[1], true_value),
                                                 relative_error(values[1], true_value))
    print(s)
    print("‾" * 64)
    print("Trapeze: ")
    print("_" * 64)
    s = "|{:^20s}|{:^20s}|{:^20s}|".format("", "Absolute error", "Relative error")
    print(s)
    s = "|{:^20.7g}|{:^20.7g}|{:^20.7g}|".format(n1, absolute_error(values[2], true_value),
                                                 relative_error(values[2], true_value))
    print(s)
    s = "|{:^20.7g}|{:^20.7g}|{:^20.7g}|".format(n2, absolute_error(values[3], true_value),
                                                 relative_error(values[3], true_value))
    print(s)
    print("‾" * 64)


def count_of_iter(error, method, start, stop, eps):
    count = 2
    if method:
        while abs(trapeze(start, stop, count, eps) - trapeze(start, stop, count//2, eps)) >= error:
            count *= 2
    else:
        while abs(right_rectangle(start, stop, count, eps) - right_rectangle(start, stop, count//2, eps)) >= error:
            count *= 2
    return count
