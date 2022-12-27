# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Найти столбец, имеющий определённое свойство по варианту.
# Наибольшее количество нулевых элементов.
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
    c = []
    mx_count = 0
    for i in range(m):
        count = 0
        d = []
        for j in range(n):
            d.append(a[j][i])
            if a[j][i] == 0:
                count += 1
        if mx_count <= count:
            mx_count = count
            c = d
    if mx_count == 0:
        print("Нулевый элементов в матрице не найдено.")
    else:
        print("Найденный столбец: ")
        """
        for i in range(m):
            print(c[i], end = " ")
        """
        print(*c, sep=" ")
