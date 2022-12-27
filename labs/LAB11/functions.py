import random as r
import time


def selection_sort(k, x):  # функция сортировки
    for i in range(k-1):
        mini = i
        for j in range(i+1, k):
            if x[j] < x[mini]:
                mini = j
        if i != mini:
            x[i], x[mini] = x[mini], x[i]
    return x


def selection_sort_time(k, x):  # функция замера времени сортировки
    start = time.time()
    count = 0
    for i in range(k-1):
        mini = i
        for j in range(i+1, k):
            if x[j] < x[mini]:
                mini = j
        if i != mini:
            x[i], x[mini] = x[mini], x[i]
            count += 1
    stop = time.time()
    return (stop - start), count


def rand_massive(k):  # создание рандомного массива заданой длины
    a = []
    for i in range(k):
        a.append(r.randint(-100, 100))
    return a


def create_massives(n1, n2, n3):  # создание массива массивов для таблицы замеров
    massives = []
    for k in range(3):
        b = []
        if k == 0:
            x = rand_massive(n1)
            b.append(selection_sort(len(x), x))
            x = rand_massive(n2)
            b.append(selection_sort(len(x), x))
            x = rand_massive(n3)
            b.append(selection_sort(len(x), x))
        elif k == 1:
            x = rand_massive(n1)
            b.append(x)
            x = rand_massive(n2)
            b.append(x)
            x = rand_massive(n3)
            b.append(x)
        else:
            x = rand_massive(n1)
            b.append(selection_sort(len(x), x)[::-1])
            x = rand_massive(n2)
            b.append(selection_sort(len(x), x)[::-1])
            x = rand_massive(n3)
            b.append(selection_sort(len(x), x)[::-1])
        massives.append(b)
    return massives
