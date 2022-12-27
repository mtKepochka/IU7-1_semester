# Тюликов Максим Вячеславович ИУ7-13Б
"""
Требуется написать программу для вычисления приближённого значения интеграла
известной, заданной в программе, функции двумя разными методами (по варианту).
Программа должна позволять задать начало и конец отрезка интегрирования, а также
N1 и N2 - количества участков разбиения.
Далее на основе известной, заданной в программе, первообразной определить, какой
метод является наиболее точным. Для этого требуется вычислить и отобразить
абсолютную и относительную погрешности каждого из четырёх измерений. Метод,
измерение которого с одним из разбиений дало самое близкое к первообразной
значение, считается наиболее точным.
Затем для другого, менее точного метода, итерационно вычислить количество участков
разбиения, для которого интеграл будет вычислен с заданной точностью, на основе
формулы:
|𝐼(𝑁) − 𝐼(2𝑁)| < ε
"""
# правых прямоугольников
# трапеций
import functions as f

eps = 10 ** -7
a, b = 0, 0
n1, n2 = 1, 1
try:
    a, b = map(float, input("Введите начало и конец через пробел: ").split(" "))  # ввод начала и конца интеграла
except:
    print("Проверьте вводимые значения.(значения должны быть типа float)")
    exit()

try:
    n1, n2 = map(int, input("Введите количество участков разбиения через пробел: ").split(" "))
    # ввод участков разбиения
except:
    print("Проверьте вводимые значения.(значения должны быть положительными целыми числами)")
    exit()
if n1 <= 0 or n2 <= 0:
    print("Проверьте вводимое значение разбиений, оно должно быть положительным.")
    exit()

values = [f.right_rectangle(a, b, n1, eps), f.right_rectangle(a, b, n2, eps),
          f.trapeze(a, b, n1, eps), f.trapeze(a, b, n2, eps)]
true_value = f.integral(a, b)
f.print_out(a, b, n1, n2, eps)
f.print_errors(true_value, n1, n2, values)
if n1 >= n2:
    error1 = f.absolute_error(values[0], true_value)
    error2 = f.absolute_error(values[2], true_value)
    if abs(error1 - error2) <= eps:
        print("Наиболее точным способом вычисления является метод правых прямоугольников.")
        error = -1.0
        try:
            error = float(input("Введите точность вычисления для менее точного метода: "))
        except:
            print("Проверьте вводимое значение.(значение должно быть типа float)")
            exit()
        if error < 0:
            print("Проверьте вводимое значение точности, оно должно быть положительным числом.")
            exit()
        count = f.count_of_iter(error, 1, a, b, eps)
        print("Необходимое количество разбиений для достижения точности методом трапеций:", count)
    else:
        print("Наиболее точным способом вычисления является метод трапеций.")
        error = -1.0
        try:
            error = float(input("Введите точность вычисления для менее точного метода: "))
        except:
            print("Проверьте вводимое значение.(значение должно быть типа float)")
            exit()
        if error < 0:
            print("Проверьте вводимое значение точности, оно должно быть положительным числом.")
            exit()
        count = f.count_of_iter(error, 0, a, b, eps)
        print("Необходимое количество разбиений для достижения точности методом правых прямоугольников:", count)
else:
    error1 = f.absolute_error(values[1], true_value)
    error2 = f.absolute_error(values[3], true_value)
    if abs(error1 - error2) <= eps:
        print("Наиболее точным способом вычисления является метод правых прямоугольников.")
        error = -1.0
        try:
            error = float(input("Введите точность вычисления для менее точного метода: "))
        except:
            print("Проверьте вводимое значение.(значение должно быть типа float)")
            exit()
        if error < 0:
            print("Проверьте вводимое значение точности, оно должно быть положительным числом.")
            exit()
        count = f.count_of_iter(error, 1, a, b, eps)
        print("Необходимое количество разбиений для достижения точности методом трапеций:", count)
    else:
        print("Наиболее точным способом вычисления является метод трапеций.")
        error = -1.0
        try:
            error = float(input("Введите точность вычисления для менее точного метода: "))
        except:
            print("Проверьте вводимое значение.(значение должно быть типа float)")
            exit()
        if error < 0:
            print("Проверьте вводимое значение точности, оно должно быть положительным числом.")
            exit()
        count = f.count_of_iter(error, 0, a, b, eps)
        print("Необходимое количество разбиений для достижения точности методом правых прямоугольников:", count)
