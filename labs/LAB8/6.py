# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Выполнить транспонирование квадратной матрицы.
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
    for i in range(n):
        for j in range(i):
            a[j][i], a[i][j] = a[i][j], a[j][i]
    print("Измененная матрица: ")
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
