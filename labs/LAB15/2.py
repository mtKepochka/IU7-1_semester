"""
Написать 3 независимые программы для работы с бинарными файлами из целых
32-битных чисел, каждая из которых будет реализовывать ввод чисел в файл (если
файл существует - перезаписывать), соответствующее задание и вывод изменённого
содержимого файла:
1. Удалить все чётные элементы за один проход по файлу.
2. После каждого положительного элемента добавить его удвоенное
значение (допускается два прохода по файлу).
3. Сортировка методом по варианту из л/р 11.(метод простого выбора)

1. Все требования по оформлению, которые предъявлялись к прошлым лаб.
работам.
2. Файлы в память целиком не читать, выполнять обработку поэлементно.
"""
# Тюликов Максим Вячеславович ИУ7-13Б
import struct as st


SIZE_ = 4


def start():
    path = ""
    string = input("Введите путь до файла: ")
    try:
        path = init_db(string)
        print("Файл в начале: ")
        print_file(path)
        double_pos(path)
        print("Файл после выполнения задания: ")
        print_file(path)
    except (FileNotFoundError, FileExistsError, PermissionError, TypeError, st.error, ValueError):
        print("Проверьте вводимый путь или файл.")
        print("Завершение программы")
        return
    print("Завершение программы")


def check_number(number):  # проверка количества чисел
    try:
        number = int(number)
        if number < 1:
            return -1
        return number
    except (TypeError, ValueError):
        return -1


def check_value(number):  # проверка вводимого значения
    try:
        number = int(number)
        if -65536 <= number <= 65535:
            return number
        return -1
    except (TypeError, ValueError):
        return -1


def init_db(string):   # создание или перезапись файла
    with open(string, "wb") as file:
        pass
    number = input("Введите какое количество чисел требуется ввести: ")
    count = 0
    while check_number(number) == -1 and count < 5:
        count += 1
        print("Ошибка, попробуйте еще раз.")
        number = input("Введите какое количество чисел требуется ввести: ")
    if count == 5:
        raise TypeError
    number = check_number(number)
    with open(string, "wb") as file:
        for i in range(number):
            count = 0
            x = input("Введите какое число требуется добавить в файл: ")
            while count < 5 and check_value(x) == -1:
                count += 1
                print("Ошибка, попробуйте еще раз.")
                x = input("Введите какое число требуется добавить в файл: ")
            x = int(check_value(x))
            if count == 5:
                raise TypeError
            file.write(st.pack("=l", x))
    return string


def double_pos(path):  # добавление двойного значения положительных элементов в файле
    with open(path, "rb+") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        max_size = file.tell()//SIZE_
        file.seek(0, 0)
        count = 0
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = int(list(st.unpack("=l", d))[0])
            if s > 0:
                count += 1
        file.seek(0, 0)
        for i in range(max_size - 1, -1, -1):
            file.seek(i*SIZE_)
            d = file.read(SIZE_)
            s = int(list(st.unpack("=l", d))[0])
            if s <= 0:
                file.seek((i+count)*SIZE_)
                file.write(d)
            else:
                file.seek((i + count)*SIZE_)
                s *= 2
                f = st.pack("=l", s)
                file.write(f)
                count -= 1
                file.seek((i + count)*SIZE_)
                file.write(d)


def print_file(path):  # вывод файла
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = int(list(st.unpack("=l", d))[0])
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if max_pos == 0:
            print("Файл пустой.")
            return
        file.seek(0)
        print("Вывод файла:")
        while file.tell() != max_pos:
            d = file.read(SIZE_)
            s = int(list(st.unpack("=l", d))[0])
            print(s)


start()
