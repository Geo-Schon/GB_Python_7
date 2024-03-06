"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""

import os
from first_task import random_fill, gen_pseudoname, create_files_with_extension, create_dif_files, group

if __name__ == '__main__':
    random_fill(10, 'file_fill.txt')
    gen_pseudoname(10, 'pseudoname.txt')
    create_files_with_extension('doc')
    create_dif_files(txt=1, mkv=2, jpg=3)
    group(os.getcwd())
