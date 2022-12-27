# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Подсчитать в каждой строке матрицы D количество элементов, превышающих
# суммы элементов соответствующих строк матрицы Z. Разместить эти
# количества в массиве G, умножить матрицу D на максимальный элемент
# массива G. Напечатать матрицу Z, матрицу D до и после преобразования, а
# также массив G.
n, m = map(int, input("Введите количество строк и столбцов для матриц D и Z через пробел(2 числа): ").split(" "))
while n <= 0 or m <= 0:
    print("Проверьте вводимые значения.")
    n, m = map(int, input("Введите количество строк и столбцов для матриц D и Z через пробел(2 числа): ").split(" "))
d = []
z = []

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input("Введите {} строку {} столбец матрицы D: ".format(i + 1, j + 1))))  # ввод матрицы D
    d.append(b)

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input("Введите {} строку {} столбец матрицы Z: ".format(i + 1, j + 1))))  # ввод матрицы Z
    z.append(b)

print("Исходный вид матрицы D: ")  # вывод исходной матрицы D
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

print("\nИсходный вид матрицы Z: ")  # вывод исходной матрицы Z
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(z[i][h])
    print(s)
print("¯"*7*(m + 1))

f = []
for i in range(m):
    count = 0
    for j in range(n):
        count += z[j][i]
    f.append(count)
g = []
for i in range(n):
    count = 0
    for j in range(m):
        if d[i][j] > f[j]:
            count += 1
    g.append(count)

print("\nИзмененный вид матрицы D: ")  # вывод измененной матрицы D
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        d[i][h] *= max(g)
        s += "|{:^5.5g}|".format(d[i][h])
    print(s)
print("¯"*7*(m + 1))

print("\nИзмененный вид матрицы Z: ")  # вывод измененной матрицы Z
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5g}|".format(z[i][h])
    print(s)
print("¯"*7*(m + 1))

print("\nМассив G: ")  # вывод массива G
print("_"*7*(n + 1))
s = "|  i  |"
for i in range(n):
    s += "|{:^5.7s}|".format(" ")
print(s)
for i in range(1):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(n):
        s += "|{:^5.5g}|".format(g[h])
    print(s)
print("¯"*7*(n + 1))
