# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Переставить местами строки с наибольшим и наименьшим количеством
# отрицательных элементов.
n, m = map(int, input("Введите количество строк и столбцов матрицы через пробел: ").split())
if n <= 0 or m <= 0:
    print("Проверьте вводимые значения")
else:
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(int(input("Введите элемент {} строки и {} столбца: ".format(i + 1, j + 1))))
        a.append(b)
    print("Исходная матрица: ")
    print("_"*7*(m+1))
    s = "| i/j |"
    for i in range(m):
        s += "|{:^5.7g}|".format(i + 1)
    print(s)
    for i in range(n):
        s = "|{:^5.7g}|".format(i + 1)
        for j in range(m):
            s += "|{:^5.7g}|".format(a[i][j])
        print(s)
    print("¯"*7*(m+1))
    mx_it = 0
    mn_it = 0
    mx_count = 0
    mn_count = m
    for i in range(n):
        count = 0
        for j in range(m):
            if a[i][j] < 0:
                count += 1
        if mx_count <= count:
            mx_count = count
            mx_it = i
        if mn_count >= count:
            mn_count = count
            mn_it = i
    a[mx_it], a[mn_it] = a[mn_it], a[mx_it]
    print("Измененная матрица: ")
    print("_"*7*(m+1))
    s = "| i/j |"
    for i in range(m):
        s += "|{:^5.7g}|".format(i + 1)
    print(s)
    for i in range(n):
        s = "|{:^5.7g}|".format(i + 1)
        for j in range(m):
            s += "|{:^5.7g}|".format(a[i][j])
        print(s)
    print("¯"*7*(m+1))
