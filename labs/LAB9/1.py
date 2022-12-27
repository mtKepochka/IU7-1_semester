# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Даны массивы D и F. Сформировать матрицу A по формуле
# ajk = sin(dj+fk).
# Определить среднее арифметическое положительных чисел каждой строки
# матрицы и количество элементов, меньших среднего арифметического.
# Результаты записать соответственно в массивы AV и L. Напечатать матрицу A в
# виде матрицы и рядом столбцы AV и L.
import math as m
d = []
f = []
a = []
eps = 10**(-8)
j, k = map(int, input("Введите длины массива d и f через пробел: ").split(" "))  # ввод значений
for i in range(j):
    d.append(int(input("Введите {} элемент списка d: ".format(i + 1))))
for i in range(k):
    f.append(int(input("Введите {} элемент списка f: ".format(i + 1))))

for i in range(j):
    b = []
    for h in range(k):
        b.append(m.sin(d[i]+f[h]))  # создание матрицы A
    a.append(b)

av = []
l = []

for i in range(j):
    g = 0
    count = 0
    for h in range(k):
        if a[i][h] > eps:
            g += a[i][h]
            count += 1
    if count != 0:
        av.append(g/count)  # подсчет среднего арифметического
    else:
        av.append(0)
for i in range(j):
    count = 0
    for h in range(k):
        if a[i][h] < av[i]:  # подсчет количества элементов меньших ср. арифметического
            count += 1
    l.append(count)

print("_"*7 + "_"*10*(k + 2))
s = "| i/j |"
for i in range(k):
    s += "|{:^8.7g}|".format(i + 1)
print(s + "|{:^8.7s}|".format("AV") + "|{:^8.7s}|".format("L"))
for i in range(j):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(k):
        s += "|{:^8.5g}|".format(a[i][h])
    print(s + "|{:^8.5g}|".format(av[i]) + "|{:^8.5g}|".format(l[i]))
print("¯"*7 + "¯"*10*(k + 2))
