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


def print_out(multistring):
    print(*multistring, sep="\n")
    print()
    print("""Меню:
    1. Выровнять текст по левому краю.
    2. Выровнять текст по правому краю.
    3. Выровнять текст по ширине.
    4. Удаление всех вхождений заданного слова.
    5. Замена одного слова другим во всём тексте.
    6. Вычисление арифметических выражений над целыми числами внутри текста(умножение и деление).
    7. Найти (вывести на экран) и затем удалить предложение с самым длинным словом.
    8. Выход из программы.
    """)


def menu(multistring):  # вывод меню
    print_out(multistring)
    command = input("Введите следующую команду: ")
    while check_command(command) == -1:
        command = input("Введите следующую команду: ")
    command = check_command(command)
    while True:
        if command == 1:
            multistring = left(multistring)
            print_out(multistring)
        elif command == 2:
            multistring = rigth_string(multistring)
            print_out(multistring)
        elif command == 3:
            multistring = width(multistring)
            print_out(multistring)
        elif command == 4:
            multistring = delete_word(multistring)
            print_out(multistring)
        elif command == 5:
            multistring = change_word(multistring)
            print_out(multistring)
        elif command == 6:
            multistring = math_operations(multistring)
            print_out(multistring)
        elif command == 7:
            multistring = delete_max_sentence(multistring)
            print_out(multistring)
        elif command == 8:
            exit()
        command = input("Введите следующую команду: ")
        while check_command(command) == -1:
            command = input("Введите следующую команду: ")
        command = check_command(command)


def left_(multistring):  # Возвращает обратно список строк выровненный по левому краю
    for i in range(len(multistring)):
        tmp = multistring[i].split()
        multistring[i] = ' '.join(tmp)
    return multistring


def left(multistring):  # Выровнять текст по левому краю.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    for i in range(len(multistring)):
        tmp = multistring[i].split()
        multistring[i] = ' '.join(tmp)
    return multistring


def rigth_string(multistring):  # Выровнять текст по правому краю.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    max_len = 0
    for i in range(len(multistring)):
        tmp = multistring[i].split()
        multistring[i] = ' '.join(tmp)
        if len(multistring[i]) > max_len:
            max_len = len(multistring[i])
    for i in range(len(multistring)):
        multistring[i] = " " * (max_len - len(multistring[i])) + multistring[i]
    return multistring


def width(multistring):  # Выровнять текст по ширине.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    max_len = 0
    for i in range(len(multistring)):
        tmp = multistring[i].split()
        multistring[i] = ' '.join(tmp)
        max_len = max(max_len, len(multistring[i]))
    for i in range(len(multistring)):
        count = max_len - (len(multistring[i]) - multistring[i].count(" "))
        tmp = multistring[i].split(" ")
        multistring[i] = ""
        for j in range(len(tmp) - (count % (len(tmp) - 1)) - 1):
            multistring[i] += tmp[j] + " " * (count // (len(tmp) - 1))
        for j in range(len(tmp) - (count % (len(tmp) - 1)) - 1, len(tmp) - 1):
            multistring[i] += tmp[j] + " " * ((count // (len(tmp) - 1)) + 1)
        multistring[i] += tmp[-1]
    return multistring


def delete_word(multistring):  # Удаление всех вхождений заданного слова.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    multistring = left_(multistring)
    try:
        word = input("Введите слово для удаления: ")
    except ValueError:
        print("Проверьте вводимое значение.")
        return multistring
    if word.find(" ") != -1:
        print("Проверьте вводимое слово, это должна быть строка без пробелов")
        return multistring
    for s in ".?!0123456789-+*/:":
        if word.find(s) != -1:
            print("Провеьте вводимое слово, оно должно состоять из букв.")
            return multistring
    for i in range(len(multistring)):
        count = 0
        prev = multistring[i].find(word) + len(word)
        count_string = multistring[i].count(word)
        while count < count_string:
            if prev < len(multistring[i]):
                if prev - len(word) - 1 >= 0:
                    if multistring[i][prev] in " .!?,:" and multistring[i][prev - len(word) - 1] in " .!?,:":
                        multistring[i] = multistring[i][:prev - len(word)] + multistring[i][prev:]
                        count += 1
                    else:
                        count += 1
                else:
                    if multistring[i][prev] in " .!?,:":
                        multistring[i] = multistring[i][:prev - len(word)] + multistring[i][prev:]
                        count += 1
                    else:
                        count += 1
            else:
                multistring[i] = multistring[i][:prev - len(word)]
            if prev < multistring[i].find(word, prev - len(word) + 1) + len(word):
                prev = multistring[i].find(word, prev - len(word) + 1) + len(word)
            else:
                break
    return left(multistring)


def change_word(multistring):  # Замена одного слова другим во всём тексте.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    multistring = left_(multistring)
    try:
        word, word2 = map(str, input("Введите слово, которое надо заменить"
                                     " и слово для замены через пробел: ").split(" "))
    except ValueError:
        print("Проверьте вводимые слова.")
        return multistring
    for s in ".?!0123456789-+*/:":
        if word.find(s) != -1:
            print("Провеьте вводимое слова, они должны состоять из букв.")
            return multistring
        if word2.find(s) != -1:
            print("Провеьте вводимое слова, они должны состоять из букв.")
            return multistring
    for i in range(len(multistring)):
        count = 0
        prev = multistring[i].find(word) + len(word)
        count_string = multistring[i].count(word)
        while count < count_string:
            if prev < len(multistring[i]):
                if prev - len(word) - 1 >= 0:
                    if multistring[i][prev] in " .!?,:" and multistring[i][prev - len(word) - 1] in " .!?,:":
                        multistring[i] = multistring[i][:prev - len(word)] + word2 + multistring[i][prev:]
                        count += 1
                    else:
                        count += 1
                else:
                    if multistring[i][prev] in " .!?,:":
                        multistring[i] = multistring[i][:prev - len(word)] + word2 + multistring[i][prev:]
                        count += 1
                    else:
                        count += 1
            else:
                multistring[i] = multistring[i][:prev - len(word)] + word2
            if prev < multistring[i].find(word, prev - len(word) + len(word2)) + len(word):
                prev = multistring[i].find(word, prev - len(word) + len(word2)) + len(word)
            else:
                break
    return left(multistring)


def delete_max_sentence(multistring):  # Найти (вывести на экран) и затем удалить предложение с самым длинным словом.
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    multistring = left_(multistring)
    mas = []
    s = ""
    for i in range(len(multistring)):
        for j in multistring[i]:
            if j != ".":
                s += j
            else:
                s += j
                mas.append(s.lstrip(" "))
                s = ""
        if s != "":
            s += " "
    max_index = 0
    max_len = 0
    for i in range(len(mas)):
        tmp = mas[i].split(" ")
        for j in tmp:
            j = j.strip(".,:!?")
            count = 0
            for h in j:
                if h not in ".?!0123456789-+*/":
                    count += 1
            if count > max_len:
                max_index = i
                max_len = len(j)
    print(mas[max_index])
    k = 0
    s = ""
    for i in range(len(multistring)):
        for j in multistring[i]:
            if k != max_index:
                s += j
            if j == ".":
                k += 1
        multistring[i] = s
        s = ""
    line_number = 0
    while line_number < len(multistring):
        if len(multistring[line_number]) == 0:
            multistring.pop(line_number)
            line_number -= 1
        line_number += 1
    print()
    return left(multistring)


def math_operations(multistring):
    # Вычисление арифметических выражений над целыми числами внутри текста(умножение и деление).
    if len(multistring) == 0:
        print("Здесь пусто, делать нечего, пока!")
        exit()
    multistring = left_(multistring)
    n1 = 0
    countn1 = 0
    n2 = 0
    countn2 = 0
    flag = 0
    k = 1
    k2 = 1
    for i in range(len(multistring)):
        if flag == -1:
            break
        j = 0
        while j < len(multistring[i]):
            if multistring[i][j] in "-":
                if flag == 0:
                    k *= -1
                    countn1 += 1
                elif flag == 1 or flag == 2:
                    k2 *= -1
                    countn2 += 1
            elif multistring[i][j] in "0123456789":
                if flag == 0:
                    n1 = n1 * 10 + int(multistring[i][j])
                    countn1 += 1
                elif flag == 1 or flag == 2:
                    n2 = n2 * 10 + int(multistring[i][j])
                    countn2 += 1
            elif multistring[i][j] in "*/":
                if flag == 0:
                    if multistring[i][j] == "*":
                        flag = 1
                    elif multistring[i][j] == "/":
                        flag = 2
                    if j + 1 == len(multistring[i]):
                        multistring[i] = multistring[i][:j - countn1]
                        j = j - countn1
                        continue
                    elif j + 1 != len(multistring[i]):
                        multistring[i] = multistring[i][:j - countn1] + multistring[i][j + 1:]
                        j = j - countn1
                        continue
                elif flag == 1:
                    result = (n1 * k) * (n2 * k2)
                    multistring[i] = multistring[i][:j - countn2] + str(result) + multistring[i][j:]
                    flag = -1
                    break
                elif flag == 2:
                    if n2 != 0:
                        result = (n1 * k) // (n2 * k2)
                        multistring[i] = multistring[i][:j - countn2] + str(result) + multistring[i][j:]
                        flag = -1
                        break
                    else:
                        multistring[i] = multistring[i][:j - countn2] + "1" + multistring[i][j:]
                        flag = -1
                        break
            else:
                if flag == 1:
                    result = (n1 * k) * (n2 * k2)
                    multistring[i] = multistring[i][:j - countn2] + str(result) + multistring[i][j:]
                    j = j - countn2 + len(str(result))
                    flag = 0
                    k = 1
                    k2 = 1
                    n1 = 0
                    n2 = 0
                    countn1 = 0
                    countn2 = 0
                elif flag == 2:
                    if n2 != 0:
                        result = (n1 * k) // (n2 * k2)
                        multistring[i] = multistring[i][:j - countn2] + str(result) + multistring[i][j:]
                        j = j - countn2 + len(str(result))
                    else:
                        multistring[i] = multistring[i][:j - countn2] + "NONE" + multistring[i][j:]
                        j = j - countn2 + 4
                    flag = 0
                    k = 1
                    k2 = 1
                    n1 = 0
                    n2 = 0
                    countn1 = 0
                    countn2 = 0
                else:
                    k = 1
                    k2 = 1
                    n1 = 0
                    n2 = 0
                    countn1 = 0
                    countn2 = 0
            j += 1
        if flag == 0 and countn1 != 0:
            multistring[i] = multistring[i][:(len(multistring[i]) - countn1)]
            countn1 = 0
    if flag == -1:
        return math_operations(multistring)
    else:
        return left(multistring)
