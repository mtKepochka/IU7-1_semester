# ФИО: Тюликов Максим Вячеславович
# Группа: ИУ7-13Б
# Найти значение K-го экстремума в списке.
n = int(input("Введите длину массива: "))  # ввод длины массива
if n > 0:
    a = []
    for i in range(n):
        a.append(int(input("Введите {} элемент массива: ".format(i))))  # ввод массива

    k = int(input("Введите номер экстремума: "))

    count = 0
    element = "NONE"
    for i in range(1, len(a) - 1):
        if (a[i-1] > a[i] and a[i] < a[i+1]) or (a[i-1] < a[i] and a[i] > a[i + 1]):
            count += 1
            if count == k:
                element = a[i]
    if element != "NONE":
        print("Значение {} экстремума в списке: {}".format(k, element))
    else:
        print("{} экстремум не найден, проверьте массив или номер экстремума.".format(k))
else:
    print("Проверьте длину массива.")
