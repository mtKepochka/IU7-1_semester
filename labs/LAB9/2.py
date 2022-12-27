# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Повернуть квадратную целочисленную матрицу на 90 градусов по часовой
# стрелке, затем на 90 градусов против часовой стрелки. Вывести исходную,
# промежуточную и итоговую матрицы. Дополнительных матриц и массивов не
# вводить. Транспонирование не применять.
n = int(input("Введите размер квадратной матрицы: "))
while n <= 0:
    print("Проверьте размер матрицы.")
    n = int(input("Введите размер квадратной матрицы: "))
a = []
for i in range(n):
    b = []
    for j in range(n):
        b.append(int(input("Введите элемент {} строки и {} столбца: ".format(i + 1, j + 1))))  # ввод матрицы
    a.append(b)

print("Исходная матрица:")  # вывод исходной матрицы
print("_"*7*(n + 1))
s = "| i/j |"
for i in range(n):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(n):
        s += "|{:^5.5g}|".format(a[i][h])
    print(s)
print("¯"*7*(n + 1))

# a = list(zip(*a[::-1]))  # поворот матрицы на 90 градусов по часовой
for i in range(int(n/2)):  # поворот матрицы на 90 градусов по часовой
    for j in range(i, n - i - 1):
        temp = a[n - 1 - j][i]
        a[n - 1 - j][i] = a[n - 1 - i][n - 1 - j]
        a[n - 1 - i][n - 1 - j] = a[j][n - 1 - i]
        a[j][n - i - 1] = a[i][j]
        a[i][j] = temp

print("Промежуточная матрица:")  # вывод промежуточной матрицы
print("_"*7*(n + 1))
s = "| i/j |"
for i in range(n):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(n):
        s += "|{:^5.5g}|".format(a[i][h])
    print(s)
print("¯"*7*(n + 1))

# for i in range(3):
#     a = list(zip(*a[::-1]))  # поворот матрицы на 90 градусов против часовой
for i in range(int(n/2)):  # поворот матрицы на 90 градусов против часовой
    for j in range(i, n - i - 1):
        temp = a[i][j]
        a[i][j] = a[j][n - i - 1]
        a[j][n - 1 - i] = a[n - 1 - i][n - 1 - j]
        a[n - 1 - i][n - 1 - j] = a[n-1-j][i]
        a[n - 1 - j][i] = temp

print("Конечная матрица:")  # вывод конечной матрицы
print("_"*7*(n + 1))
s = "| i/j |"
for i in range(n):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(n):
        s += "|{:^5.5g}|".format(a[i][h])
    print(s)
print("¯"*7*(n + 1))
