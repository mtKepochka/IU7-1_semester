# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Дана матрица символов. Заменить в ней все гласные английские буквы на
# точки. Напечатать матрицу до и после преобразования.
n, m = map(int, input("Введите количество строк и столбцов для матрицы через пробел: ").split(" "))
while n <= 0 or m <= 0:
    print("Проверьте вводимые значения.")
    n, m = map(int, input("Введите количество строк и столбцов для матрицы через пробел: ").split(" "))
d = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(input("Введите {} строку {} столбец матрицы D: ".format(i + 1, j + 1)))  # ввод матрицы D
    d.append(b)

for i in range(n):
    for j in range(m):
        for k in "aeiouyAEIOUY":
            d[i][j] = d[i][j].replace(k, ".")  # замена символа

print("\nМатрица D: ")  # вывод матрицы D
print("_"*7*(m + 1))
s = "| i/j |"
for i in range(m):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(n):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(m):
        s += "|{:^5.5s}|".format(d[i][h])
    print(s)
print("¯"*7*(m + 1))
