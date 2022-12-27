# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Добавить элемент в заданное место списка (по индексу) алгоритмически
n = int(input("Введите длину массива: "))  # ввод длины массива
if n > 0:
    a = []
    for i in range(n):
        a.append(int(input("Введите {} элемент массива: ".format(i))))  # ввод массива

    index, element = map(int, input("Введите индекс и элемент, который надо добавить через пробел: ").split())
    if index >= len(a):
        a.append(element)
    else:
        if index >= 0:
            a.append(0)
            for i in range(len(a) - 1, index - 1, -1):
                a[i] = a[i-1]
            a[index] = element
        else:
            if abs(index) <= len(a):
                index_n = len(a) + index
                a.append(0)
                for i in range(len(a) - 1, index_n - 1, -1):
                    a[i] = a[i - 1]
                a[index_n] = element
            else:
                a.append(0)
                for i in range(len(a) - 1, 0, -1):
                    a[i] = a[i - 1]
                a[0] = element
    print(a)
else:
    print("Проверьте длину массива.")
