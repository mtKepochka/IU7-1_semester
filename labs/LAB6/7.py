# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Поменять местами элементы с характеристиками по варианту
# Первый чётный и максимальный положительный.
n = int(input("Введите длину массива: "))  # ввод длины массива
if n > 0:
    a = []
    k = -1
    for i in range(n):
        a.append(int(input("Введите {} элемент массива: ".format(i))))  # ввод массива
        if a[i] % 2 == 0 and k == -1:
            k = i
    if max(a) > 0 and k != -1:
        max_a_i = a.index(max(a))
        a[max_a_i], a[k] = a[k], a[max_a_i]
        print(a)
    else:
        print("Проверьте вводимый массив.")
else:
    print("Проверьте длину массива.")
