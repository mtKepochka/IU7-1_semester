# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Наибольшее количество подряд идущих одинаковых элементов.
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
    for i in range(n):
        count = 0
        for j in range(1, m):
            if a[i][j] == a[i][j-1]:
                count += 1
        if mx_count <= count:
            mx_count = count
            c = a[i]
    if mx_count == 0:
        print("Строки с идущими подряд одинаковыми элементами не найдено.")
    else:
        print("Найденная строка: ")
        """
        for i in range(m):
            print(c[i], end = " ")
        """
        print(*c, sep=" ")
