"""
Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

"""

from pathlib import Path


def rename_files(target_ext, source_ext, num_digits, desired_name, name_range=None):
    path = Path().cwd()
    files = Path(path).iterdir()
    file_number = 1
    for file in files:
        if file.suffix == '.' + source_ext:
            if name_range:
                file.name = file.name[name_range[0] - 1:name_range[1]]
            file.rename(f'{path}\{desired_name}{str(file_number).zfill(num_digits)}.{target_ext}')
            file_number += 1


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
