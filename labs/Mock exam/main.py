"""
В первом файле записано N целых чисел со значениями от 1 до 3000 по одному в строке. Во втором файле записаны целые числа от 1 до N в произвольном порядке - номера строк в первом файле.
Требуется сформировать файл out1.txt, в который записать числа из файла in1.txt, переведённые в римскую систему счисления, с выравниванием по центру (на основе длины числа с самым большим количеством цифр в римской с/с).
Далее требуется сформировать файл out2.txt, переписав в него строки из файла out1.txt на основе порядка, заданного в файле in2.txt.
Не разрешается считывать в память более одной строки каждого файла одновременно.
"""
def dec_to_roma(integer: int):  # function made by Kirill Vorobyov

    thous = integer // 1000
    thous = "M" * thous

    cent = integer % 1000 // 100
    if cent < 4:
        cent = "C" * cent
    elif cent == 4:
        cent = "CD"
    elif cent < 9:
        cent = "D" + ("C" * (cent - 5))
    else:
        cent = "CM"

    decs = integer % 1000 % 100 // 10
    if decs < 4:
        decs = "X" * decs
    elif decs == 4:
        decs = "XL"
    elif decs < 9:
        decs = "L" + ("X" * (decs - 5))
    else:
        decs = "XC"

    single = integer % 1000 % 100 % 10
    if single < 4:
        single = "I" * single
    elif single == 4:
        single = "IV"
    elif single < 9:
        single = "V" + ("I" * (single - 5))
    else:
        single = "IX"

    return thous + cent + decs + single

        

with open("in1.txt", "r") as file:
    with open("out1.txt", "w") as file2:
        file.seek(0, 2)
        max_size = file.tell()
        file.seek(0)
        max_len = 0
        while file.tell() < max_size:
            s = file.readline()
            s = str(dec_to_roma(int(s)))
            max_len = max(len(s), max_len)
        file.seek(0)
        while file.tell() < max_size:
            s = file.readline()
            s = str(dec_to_roma(int(s)))
            s = s.center(max_len)
            print(s, file=file2)

with open("out1.txt", "r") as file:
    with open("in2.txt", "r") as file2:
        with open("out2.txt", "w") as file3:
            file2.seek(0, 2)
            max_size = file2.tell()
            file2.seek(0)
            while file2.tell() < max_size:
                line_number = int(file2.readline())
                file.seek(0)
                for i in range(line_number):
                    current_line = file.readline()
                    if i == line_number - 1:
                        print(current_line, file=file3, end='')
