'''
Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
Выведите три найденных числа в формате, приведенном в примере.

Пример входного файла:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Пример выходного файла:
Input file contains:
108 letters
20 words
4 lines
'''
import re

try:
    with open('text.txt') as my_file, open('output.txt', 'w') as out:
        data = my_file.read()
        letters = str(len(re.findall(r'[a-zA-Z]', data))) + " letters\n"
        words = str(len(re.findall(r'\w+', data))) + " words\n"
        out.write("Input file contains:\n")
        out.write(letters)
        out.write(words)
        my_file.seek(0)
        lines = str(len(my_file.readlines())) + " lines"
        out.write(lines)
except FileNotFoundError:
    print("Упс! А файла-то нет такого")
