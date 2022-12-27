# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Сформировать матрицу C путём построчного перемножения матриц A и B
# одинаковой размерности (элементы в i-й строке матрицы A умножаются на
# соответствующие элементы в i-й строке матрицы B), потом сложить все
# элементы в столбцах матрицы C и записать их в массив V. Напечатать матрицы
# A, B, C и массив V.
n, m = map(int, input("Введите количество строк и столбцов для матриц A и B через пробел: ").split(" "))
while n <= 0 or m <= 0:
    print("Проверьте вводимые значения.")
    n, m = map(int, input("Введите количество строк и столбцов для матрицы через пробел: ").split(" "))

a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input("Введите {} строку {} столбец матрицы A: ".format(i + 1, j + 1))))  # ввод матрицы A
    a.append(b)

b = []
for i in range(n):
    f = []
    for j in range(m):
        f.append(int(input("Введите {} строку {} столбец матрицы B: ".format(i + 1, j + 1))))  # ввод матрицы B
    b.append(f)

c = []
for i in range(n):
    f = []
    for j in range(m):
        f.append(a[i][j]*b[i][j])  # создание матрицы С
    c.append(f)

v = []
for i in range(m):
    v.append(0)
    for j in range(n):
        v[i] += c[j][i]  # сощдание массива V


print("\nМатрица A: ")  # вывод матрицы А
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(a[i][h])
    print(s)
print("¯"*7*(m + 1))


print("\nМатрица B: ")  # вывод матрицы А
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(b[i][h])
    print(s)
print("¯"*7*(m + 1))


print("\nМатрица C: ")  # вывод матрицы А
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(c[i][h])
    print(s)
print("¯"*7*(m + 1))


print("\nМассив V: ")  # вывод массива V
print("_"*7*(len(v) + 1))
s = "|  i  |"
for i in range(len(v)):
    s += "|{:^5.7s}|".format(" ")
print(s)
for i in range(1):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(len(v)):
        s += "|{:^5.5g}|".format(v[h])
    print(s)
print("¯"*7*(len(v) + 1))
