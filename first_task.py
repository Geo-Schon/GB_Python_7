import random as rnd
from random import randint, uniform
import os
import random
import string

"""
Напишите функцию, которая заполняет файл  (добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""

min_num = -1000
max_num = 1000


def random_fill(count_row, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count_row):
            f.write(f'{randint(min_num, max_num)}|{round(uniform(min_num, max_num), 2)}\n')


if __name__ == '__main__':
    random_fill(200, 'file_fill.txt')

"""
Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.
"""


def gen_pseudoname(num, name):
    literals = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    vowels = 'аеиоуэюя'
    min_lit = 4
    max_lit = 7
    with open(name, 'w', encoding='utf-8') as f:
        for _ in range(num):
            name = rnd.sample(literals, rnd.randint(min_lit, max_lit))
            if not set(name) & set(vowels):
                half = len(name) // 2
                name = name[:half] + rnd.sample(vowels, half)
                rnd.shuffle(name)
            name = ''.join(name).capitalize()
            f.write(f'{name}\n')


if __name__ == '__main__':
    gen_pseudoname(10, 'pseudoname.txt')

"""
Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.
"""


def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_byte_size=256, max_byte_size=4096,
                                num_files=1):
    for _ in range(num_files):
        name_length = random.randint(min_name_length, max_name_length)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length)) + '.' + extension

        file_size = random.randint(min_byte_size, max_byte_size)
        random_bytes = os.urandom(file_size)

        with open(file_name, 'wb') as file:
            file.write(random_bytes)


create_files_with_extension('bin')

"""
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
"""


def create_dif_files(**kwargs):
    for ext, num in kwargs.items():
        create_files_with_extension(ext, num_files=num)


if __name__ == '__main__':
    create_dif_files(txt=2, bin=4, png=8)

"""
Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""

DCT = {'videos': ('mkv', 'avi', 'mp4'),
       'images': ('png', 'jpg', 'jpeg'),
       'texts': ('txt', 'rtf', 'doc')}


def group(dir_):
    files = [file for file in os.listdir() if os.path.isfile(file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in exts:
                # os.replace(file, fold + '\\' + file)
                os.replace(file, os.path.join(os.getcwd(), fold, file))


if __name__ == '__main__':
    group(os.getcwd())
