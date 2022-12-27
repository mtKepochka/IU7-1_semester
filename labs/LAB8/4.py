# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Переставить местами столбцы с максимальной и минимальной суммой
# элементов.
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
    for i in range(m): # поиск строки
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
    mn_count = 0
    for i in range(n):
        mn_count += a[i][0]
    mx_count = mn_count
    for i in range(m):
        count = 0
        d = []
        for j in range(n):
            d.append(a[j][i])
            count += a[j][i]
        if mx_count <= count:
            mx_count = count
            mx_it = i
        if mn_count >= count:
            mn_count = count
            mn_it = i
    for i in range(n):
        a[i][mx_it], a[i][mn_it] = a[i][mn_it], a[i][mx_it]
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
