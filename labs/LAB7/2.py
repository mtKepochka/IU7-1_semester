# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# после каждого положительного элемента вставить его удвоенное значение без вложенных циклов (алгоритмически)
n = int(input("Введите количество элементов в массиве: "))  # ввод длины списка
if n >= 1:
    a = []
    l_ind = -1
    count_z = 0
    k = 0
    for i in range(n):
        d = int(input("Введите {} элемент в массиве: ".format(i)))  # ввод значений для списка
        if d > 0:
            count_z += 1
        a.append(d)
    for i in range(count_z):
        a.append(0)
    step = count_z
    for i in range(n - 1, -1, -1):
        if a[i] <= 0:
            a[i + step] = a[i]
        else:
            a[i + step] = 2 * a[i]
            step -= 1
            a[i + step] = a[i]

    print("Измененный список: ")  # вывод массива
    print(*a, sep="\n")
else:
    print("Проверьте вводимое количество элементов.")
