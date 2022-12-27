import random
import struct as st


SIZE_ = 38


def check_command(command):
    try:
        command = int(command)
    except ValueError:
        print("Проверьте вводимое значение, оно должно быть целочисленным(1-8)\n")
        return -1
    if not(1 <= command <= 8):
        print("Проверьте вводимое значение, оно должно быть целочисленным(1-8)\n")
        return -1
    return command


def check_age(age):
    try:
        age = int(age)
    except ValueError:
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-116)\n")
        return -1
    if not(0 <= age <= 116):
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-116)\n")
        return -1
    return age


def read_values():
    name = input("Введите имя: ")
    count = 0
    while len(name) > 15 and count < 5:
        count += 1
        print("Вводимое имя не должно превышать 15 символов.")
        name = input("Введите имя: ")
    if count == 5:
        print("Превышено количество попыток ввода.")
        return -1, -1, -1
    count = 0
    age = input("Введите возраст: ")
    while check_age(age) == -1 and count < 5:
        count += 1
        age = input("Введите возраст: ")
    age = check_age(age)
    if count == 5:
        print("Превышено количество попыток ввода.")
        return -1, -1, -1
    count = 0
    city = input("Введите название города: ")
    while len(city) > 15 and count < 5:
        count += 1
        print("Вводимое название города не должно превышать 15 символов.")
        city = input("Введите название города: ")
    if count == 5:
        print("Превышено количество попыток ввода.")
        return -1, -1, -1
    return name, age, city


def menu():
    path = ""
    print("""1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных
5. Удалить произвольную запись из базы данных
6. Поиск по одному полю
7. Поиск по двум полям
8. Выход""")
    command = input("Введите следующую команду: ")
    while check_command(command) == -1:
        command = input("Введите следующую команду: ")
    command = check_command(command)
    while True:
        if command == 1:
            string = input("Введите путь до файла: ")
            try:
                path = choose_file(string)
            except FileNotFoundError or PermissionError:
                print("Проверьте вводимый путь и, что задаваемый файл является БД.")
            except:
                print("Проверьте вводимый путь.")
        elif command == 2:
            string = input("Введите путь до файла: ")
            try:
                path = init_db(string)
            except FileNotFoundError or PermissionError:
                print("Проверьте вводимый путь.")
            except:
                print("Проверьте вводимый путь.")
        elif command == 3:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                try:
                    print_db(path)
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 4:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                name, age, city = read_values()
                if not(name == -1 and age == -1 and city == -1):
                    try:
                        append_string(path, name, age, city)
                    except FileNotFoundError or PermissionError:
                        path = ""
                        print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 5:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                try:
                    delete_string(path)
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 6:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                try:
                    word = input("Какой город ищем: ")
                    one_field_search(path, word)
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 7:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                try:
                    word = input("Какое имя ищем: ")
                    word2 = input("Сколько лет человеку: ")
                    count = 0
                    while check_age(word2) == -1 and count < 5:
                        count += 1
                        word2 = input("Сколько лет человеку: ")
                    if count == 5:
                        print("Превышено количество попыток для ввода.")
                    else:
                        word2 = str(check_age(word2))
                        two_field_search(path, word, word2)
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 8:
            print("Пока-пока!")
            exit()
        print()
        print("""1. Выбрать файл для работы
2. Инициализировать базу данных
3. Вывести содержимое базы данных
4. Добавить запись в произвольное место базы данных
5. Удалить произвольную запись из базы данных
6. Поиск по одному полю
7. Поиск по двум полям
8. Выход""")
        command = input("Введите следующую команду: ")
        while check_command(command) == -1:
            command = input("Введите следующую команду: ")
        command = check_command(command)


def choose_file(string):
    with open(string, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
        try:
            while file.tell() != max_pos:
                d = file.read(SIZE_)
                s = list(st.unpack("=l15sl15s", d))
                s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
                s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
        except Exception:
            raise FileNotFoundError
    return string


def init_db(string):
    names = ["Вася", "Петя", "Коля", "Сережа"]
    cities = ["Москва", "Саратов", "Сочи", "Геленджик"]
    with open(string, "wb") as file:
        # "Индекс|Имя|Возраст|Город"
        for i in range(5):
            s = [i, names[random.randint(0, len(names) - 1)], random.randint(10, 18),
                 cities[random.randint(0, len(cities) - 1)]]
            file.write(st.pack("=l15sl15s", s[0], s[1].encode(encoding="cp1251"), s[2], s[3].encode(encoding="cp1251")))
    return string


def print_db(path):  # вывод БД
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if max_pos == 0:
            print("БД пуста и ждет, когда ее заполнят важной информацией.")
            return
        file.seek(0)
        print("|{:10s}|{:15s}|{:8s}|{:15s}|".format("Индекс", "Имя", "Возраст", "Город"))
        while file.tell() != max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
            print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(str(s[0]), s[1], str(s[2]), s[3]))


def delete_string(path):  # удаление строчки в произвольной позиции
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
    number = get_number_string_del(path)
    if number == -1:
        print("Ошибка, превышено количество попыток ввода или файл уже пустой.")
        return
    with open(path, "rb+") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if number == max_pos//SIZE_ - 1:
            file.truncate(file.tell() - SIZE_)
            return
        file.seek((number + 1)*SIZE_)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
            s[0] = s[0] - 1
            d = st.pack("=l15sl15s", s[0], s[1].encode(encoding="cp1251"), s[2], s[3].encode(encoding="cp1251"))
            file.seek(file.tell() - 2 * SIZE_)
            file.write(d)
            file.seek(file.tell() + SIZE_)
        file.truncate(file.tell() - SIZE_)


def append_string(path, name, age, city):  # вставка строчки в произвольную позицию
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
    number = get_number_string(path)
    if number == -1:
        print("Ошибка, превышено количество попыток ввода.")
        return
    with open(path, "rb+") as file:
        file.seek(0, 2)
        while file.tell() >= (number + 1) * SIZE_:
            file.seek(file.tell() - SIZE_)
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
            s[0] = s[0] + 1
            d = st.pack("=l15sl15s", s[0], s[1].encode(encoding="cp1251"), s[2], s[3].encode(encoding="cp1251"))
            file.write(d)
            file.seek(file.tell() - 2*SIZE_)
        s = [number, name, int(age), city]
        d = st.pack("=l15sl15s", s[0], s[1].encode(encoding="cp1251"), s[2], s[3].encode(encoding="cp1251"))
        file.seek(number*SIZE_)
        file.write(d)


def one_field_search(path, word):  # поиск по 1 полю
    namings = "Индекс|Имя|Возраст|Город"
    tmp1 = namings.split("|")
    print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp1[0], tmp1[1], tmp1[2], tmp1[3].strip()))
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_size = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_size:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) == 4:
                s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
                s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
                if s[3] == word:
                    s[0] = str(s[0])
                    s[2] = str(s[2])
                    print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(s[0], s[1], s[2], s[3].strip()))
            else:
                raise FileNotFoundError
    return []


def two_field_search(path, word, word2):  # поиск по 2 полям
    namings = "Индекс|Имя|Возраст|Город"
    tmp1 = namings.split("|")
    print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp1[0], tmp1[1], tmp1[2], tmp1[3].strip()))
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_size = file.tell()
        if file.tell() % SIZE_ != 0:
            raise FileNotFoundError
        file.seek(0)
        while file.tell() < max_size:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) == 4:
                s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
                s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
                if s[1] == word and str(s[2]) == word2:
                    s[0] = str(s[0])
                    s[2] = str(s[2])
                    print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(s[0], s[1], s[2], s[3].strip()))
            else:
                raise FileNotFoundError
    return []


def get_number_string_del(path):  # получение вводимого значения для вставки строки
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        numbers = max_pos // SIZE_
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
    if numbers == 0:
        return -1
    k = input(("Введите позицию строчки, которую удаляем(0 - {}): ".format(numbers - 1)))
    count = 0
    while check_number_string_del(k, numbers) == -1 and count < 5:
        count += 1
        k = input(("Введите позицию строчки, которую удаляем(0 - {}): ".format(numbers - 1)))
    else:
        if count >= 5:
            return -1
        k = check_number_string_del(k, numbers)
    return k


def check_number_string_del(k, numbers):  # проверка вводимого значения для удаления строки
    try:
        k = int(k)
    except ValueError:
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-{})\n".format(numbers - 1))
        return -1
    if not(0 <= k < numbers):
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-{})\n".format(numbers - 1))
        return -1
    return k


def get_number_string(path):  # получение вводимого значения для вставки строки
    with open(path, "rb") as file:
        file.seek(0, 2)
        max_pos = file.tell()
        numbers = max_pos // SIZE_
        file.seek(0)
        while file.tell() < max_pos:
            d = file.read(SIZE_)
            s = list(st.unpack("=l15sl15s", d))
            if len(s) != 4:
                raise FileNotFoundError
            s[1] = s[1].decode(encoding="cp1251").replace("\x00", "")
            s[3] = s[3].decode(encoding="cp1251").replace("\x00", "")
    k = input(("Введите на какую позицию вставляем строчку(0 - {}): ".format(numbers)))
    count = 0
    while check_number_string(k, numbers) == -1 and count < 5:
        count += 1
        k = input(("Введите на какую позицию вставляем строчку(0 - {}): ".format(numbers)))
    else:
        if count >= 5:
            return -1
        k = check_number_string(k, numbers)
    return k


def check_number_string(k, numbers):  # проверка вводимого значения для вставки строки
    try:
        k = int(k)
    except ValueError:
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-{})\n".format(numbers))
        return -1
    if not(0 <= k <= numbers):
        print("Проверьте вводимое значение, оно должно быть целочисленным(0-{})\n".format(numbers))
        return -1
    return k
