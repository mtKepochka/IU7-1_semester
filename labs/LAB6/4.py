# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Удалить элемент с заданным индексом алгоритмически.
n = int(input("Введите длину массива: "))  # ввод длины массива
if n > 0:
    a = []
    for i in range(n):
        a.append(int(input("Введите {} элемент массива: ".format(i))))  # ввод массива

    index = int(input("Введите индекс элемента, который надо удалить: "))
    if index >= len(a) or (index < 0 and abs(index) > len(a)):
        print("Проверьте вводимый индекс")
    else:
        if index >= 0:
            for i in range(index, len(a) - 1):
                a[i] = a[i + 1]
            a.pop()
        else:
            index_n = len(a) + index
            for i in range(index_n, len(a) - 1):
                a[i] = a[i + 1]
            a.pop()
        print(a)
else:
    print("Проверьте длину массива.")
