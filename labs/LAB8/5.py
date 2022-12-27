# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Найти максимальное значение в квадратной матрице над главной диагональю и
# минимальное - под побочной диагональю.
n = int(input("Введите количество строк в квадратной матрице: "))
if n <= 0:
    print("Проверьте вводимые значения")
else:
    a = []
    for i in range(n):
        b = []
        for j in range(n):
            b.append(int(input("Введите элемент {} строки и {} столбца: ".format(i + 1, j + 1))))
        a.append(b)
    print("Исходная матрица: ")
    print("_"*7*(n+1))
    s = "| i/j |"
    for i in range(n):
        s += "|{:^5.7g}|".format(i + 1)
    print(s)
    for i in range(n):
        s = "|{:^5.7g}|".format(i + 1)
        for j in range(n):
            s += "|{:^5.7g}|".format(a[i][j])
        print(s)
    print("¯"*7*(n+1))
    mx_el = a[0][0]
    mn_el = a[-1][0]
    for i in range(n):
        for j in range(n):
            if j >= i:
                mx_el = max(mx_el, a[i][j])
            if j >= n - i - 1:
                mn_el = min(mn_el, a[i][j])
    print("Максимальный элемент выше(либо лежит на) главной диагонали: {:^5.7g}"
          "\nМинимальный элемент ниже(либо лежит на) побочной диагонали: {:^5.7g}".format(mx_el, mn_el))
