# Тюликов Максим Вячеславович ИУ7-13Б
# умножение и деление 7
# Написать программу для выполнения некоторых операций с текстом.
"""
1. Выровнять текст по левому краю.
2. Выровнять текст по правому краю.
3. Выровнять текст по ширине.
4. Удаление всех вхождений заданного слова.
5. Замена одного слова другим во всём тексте.
6. Вычисление арифметических выражений над целыми числами внутри текста(умножение и деление).
7. Найти (вывести на экран) и затем удалить предложение с самым длинным словом.
8. Выход из программы.
"""
import functions as f
given_text = ["Every inch of wall 65 space 7 is covered by a bookcase. Each bookcase has shelves, 5",
              "*6going almost to the ceiling. Some bookshelves 3/0 are stacked to the brim with hardback books",
              "science, maths, history-555*100, and -10*-10 everything else. Other shelves have two layers",
              "of paperback science fiction, with the back layer of books propped up on old tissue-10/",
              "0boxes or lengths of wood, so that you can see the back layer of books above the books in",
              "front. And it still isn't enough. Books 2*2/7 are overflowing onto the tables",
              "and the sofas and making little heaps under the windows-5*-5."]
f.menu(given_text)
