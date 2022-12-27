# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Ввести трёхмерный массив (массив матриц размера X*Y*Z), вывести из него i-й
# срез (матрицу - фрагмент трёхмерного массива) по второму индексу (нумерация
# индексов начинается с 1).
x, y, z = map(int, input("Введите X, Y и Z через пробел: ").split())
while x <= 0 or y <= 0 or z <= 0:
    print("Проверьте вводимые значения.")
    x, y, z = map(int, input("Введите X, Y и Z через пробел: ").split())
h = int(input("Введите номер среза: "))
while h >= y:
    print("Проверьте вводимое значение.")
    h = int(input("Введите номер среза: "))

a = []
for i in range(x):
    b = []
    for j in range(y):
        c = []
        for k in range(z):  # ввод 3х мерной матрицы
            c.append(int(input("Введите элемент на {} {} {} позиции: ".format(i + 1, j + 1, k + 1))))
        b.append(c)
    a.append(b)
c = []
for i in range(x):
    b = []
    for k in range(z):
        b.append(a[i][h][k])
    c.append(b)

print("Матрица C: ")  # вывод матрицы С
print("_"*7*(z + 1))
s = "| i/j |"
for i in range(z):
    s += "|{:^5.7g}|".format(i + 1)
print(s)
for i in range(x):
    s = "|{:^5.7g}|".format(i + 1)
    for h in range(z):
        s += "|{:^5.5g}|".format(c[i][h])
    print(s)
print("¯"*7*(z + 1))

