import random


def check_command(command):
    try:
        command = int(command)
    except ValueError:
        print("Проверьте вводимое значение, оно должно быть целочисленным(1-7)\n")
        return -1
    if not(1 <= command <= 7):
        print("Проверьте вводимое значение, оно должно быть целочисленным(1-7)\n")
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
    while len(name) > 15:
        print("Вводимое имя не должно превышать 15 символов.")
        name = input("Введите имя: ")

    age = input("Введите возраст: ")
    while check_age(age) == -1:
        age = input("Введите возраст: ")
    age = check_age(age)

    city = input("Введите название города: ")
    while len(city) > 15:
        print("Вводимое название города не должно превышать 15 символов.")
        city = input("Введите название города: ")
    return name, age, city


def menu():
    path = ""
    print("""1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями).
3. Вывести содержимое базы данных.
4. Добавить запись в конец базы данных.
5. Поиск по одному полю.
6. Поиск по двум полям.
7. Выйти из программы.""")
    command = input("Введите следующую команду: ")
    while check_command(command) == -1:
        command = input("Введите следующую команду: ")
    command = check_command(command)
    while True:
        if command == 1:
            string = input("Введите путь до файла: ")
            tmp = string.split("\\")
            if (tmp[-1].rfind(".txt") != len(tmp[-1]) - 4 or tmp[-1].find(".txt") == -1) or tmp[-1] == ".txt":
                print("Проверьте вводимый путь.")
            else:
                try:
                    path = choose_file(string)
                except FileNotFoundError or PermissionError:
                    print("Проверьте вводимый путь и, что задаваемый файл является БД.")
        elif command == 2:
            string = input("Введите путь до файла: ")
            tmp = string.split("\\")
            if (tmp[-1].rfind(".txt") != len(tmp[-1]) - 4 or tmp[-1].find(".txt") == -1) or tmp[-1] == ".txt":
                print("Проверьте вводимый путь.")
            else:
                try:
                    path = init_db(string)
                except FileNotFoundError or PermissionError:
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
                    word = input("Какой город ищем: ")
                    tmp = one_field_search(path, word)
                    if len(tmp) != 0:
                        namings = "Индекс|Имя|Возраст|Город"
                        tmp1 = namings.split("|")
                        print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp1[0], tmp1[1], tmp1[2], tmp1[3].strip()))
                        print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp[0], tmp[1], tmp[2], tmp[3].strip()))
                    else:
                        print("Строки с такими значениями не найдено")
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 6:
            if len(path) == 0:
                print("Файл БД не выбран")
            else:
                try:
                    word = input("Какое имя ищем: ")
                    word2 = input("Сколько лет человеку: ")
                    while check_age(word2) == -1:
                        word2 = input("Сколько лет человеку: ")
                    word2 = str(check_age(word2))
                    tmp = two_field_search(path, word, word2)
                    if len(tmp) != 0:
                        namings = "Индекс|Имя|Возраст|Город"
                        tmp1 = namings.split("|")
                        print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp1[0], tmp1[1], tmp1[2], tmp1[3].strip()))
                        print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp[0], tmp[1], tmp[2], tmp[3].strip()))
                    else:
                        print("Строки с такими значениями не найдено")
                except FileNotFoundError or PermissionError:
                    path = ""
                    print("Введите путь еще раз и проверьте, что задаваемый файл является БД.")
        elif command == 7:
            print("Пока-пока!")
            exit()
        print()
        print("""1. Выбрать файл для работы
2. Инициализировать базу данных (создать либо перезаписать файл и заполнить его записями).
3. Вывести содержимое базы данных.
4. Добавить запись в конец базы данных.
5. Поиск по одному полю.
6. Поиск по двум полям.
7. Выйти из программы.""")
        command = input("Введите следующую команду: ")
        while check_command(command) == -1:
            command = input("Введите следующую команду: ")
        command = check_command(command)


def choose_file(string):
    with open(string, "r", encoding="UTF-8") as file:
        for s in file:
            tmp = s.split("|")
            if len(tmp) != 4:
                raise FileNotFoundError
    return string


def init_db(string):
    names = ["Вася", "Петя", "Коля", "Сережа"]
    cities = ["Москва", "Саратов", "Геленджик", "Сочи"]
    with open(string, "w+", encoding="UTF-8") as file:
        s = "Индекс|Имя|Возраст|Город\n"
        file.write(s)
        for i in range(5):
            s = str(i) + "|" + names[random.randint(0, len(names) - 1)] + "|" + str(random.randint(10, 18)) \
                + "|" + cities[random.randint(0, len(cities) - 1)] + "\n"
            file.write(s)
        s = str(5) + "|" + names[random.randint(0, len(names) - 1)] + "|" + str(random.randint(10, 18)) \
            + "|" + cities[random.randint(0, len(cities) - 1)]
        file.write(s)
    return string


def print_db(path):
    with open(path, "r", encoding="UTF-8") as file:
        for s in file:
            tmp = s.split("|")
            if len(tmp) == 4:
                print("|{:10s}|{:15s}|{:8s}|{:15s}|".format(tmp[0], tmp[1], tmp[2], tmp[3].strip()))
            else:
                raise FileNotFoundError
    print()


def append_string(path, name, age, city):
    with open(path, "r+", encoding="UTF-8") as file:
        for s in file:
            tmp = s.split("|")
            if len(tmp) != 4:
                raise FileNotFoundError
        tmp = s.split("|")
        string = "\n" + str(int(tmp[0]) + 1) + "|" + name + "|" + str(age) + "|" + city
        file.write(string)


def one_field_search(path, word):
    with open(path, "r", encoding="UTF-8") as file:
        for s in file:
            tmp = s.strip("\n").split("|")
            if len(tmp) == 4:
                if tmp[3] == word:
                    return tmp
            else:
                raise FileNotFoundError
    return []


def two_field_search(path, word, word2):
    with open(path, "r", encoding="UTF-8") as file:
        for s in file:
            tmp = s.strip("\n").split("|")
            if len(tmp) == 4:
                if tmp[1] == word and tmp[2] == word2:
                    return tmp
            else:
                raise FileNotFoundError
    return []
