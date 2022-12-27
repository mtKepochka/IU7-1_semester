# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Задана матрица D и массив I, содержащий номера строк, для которых
# необходимо определить максимальный элемент. Значения максимальных
# элементов запомнить в массиве R. Определить среднее арифметическое
# вычисленных максимальных значений. Напечатать матрицу D, массивы I и R,
# среднее арифметическое значение.
n, m = map(int, input("Введите количество строк и столбцов для матрицы D через пробел: ").split(" "))
while n <= 0 or m <= 0:
    print("Проверьте вводимые значения.")
    n, m = map(int, input("Введите количество строк и столбцов для матрицы D через пробел: ").split(" "))
h = int(input("Введите размер массива I: "))
while h > n:
    print("Проверьте размер массива I")
    h = int(input("Введите размер массива I: "))
d = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input("Введите {} строку {} столбец матрицы D: ".format(i + 1, j + 1))))  # ввод матрицы D
    d.append(b)
l = set()
for i in range(h):
    f = int(input("Введите {} элемент массива I: ".format(i + 1)))  # ввод массива I
    while f >= n:
        print("Проверьте вводимое значение.")
        f = int(input("Введите {} элемент массива I: ".format(i + 1)))
    l.add(f)
l = list(l)

r = []
for i in l:
    r.append(max(d[i]))
av = sum(r)/len(r)

print("\nМатрица D: ")  # вывод матрицы D
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(d[i][h])
    print(s)
print("¯"*7*(m + 1))

print("\nМассив I: ")  # вывод массива I
print("_"*7*(len(l) + 1))
s = "|  i  |"
for i in range(len(l)):
    s += "|{:^5.7s}|".format(" ")
print(s)
for i in range(1):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(len(l)):
        s += "|{:^5.5g}|".format(l[h])
    print(s)
print("¯"*7*(len(l) + 1))

print("\nМассив R: ")  # вывод массива R
print("_"*7*(len(r) + 1))
s = "|  i  |"
for i in range(len(r)):
    s += "|{:^5.7s}|".format(" ")
print(s)
for i in range(1):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(len(r)):
        s += "|{:^5.5g}|".format(r[h])
    print(s)
print("¯"*7*(len(r) + 1))

print("\nСреднее арифмитическое: {:5.5g}".format(av))  # вывод среднего арифметического
