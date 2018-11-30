# EASY

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
def make_dir_i():
    dirs = ['dir_'+str(i) for i in range(1,10)]
    print(dirs)
    for dir_ in dirs:
        os.mkdir(os.path.join(dir_))
    return 0

# make_dir_i()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path):
    print(path)
    return 0

p = os.listdir(os.getcwd())
list_dir(p)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
import sys

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл ", newfile, " был успешно создан")
            return True
        else:
            print("Возникли проблемы копирования")
            return False

destdir = os.path.abspath('destdir')
if not os.path.exists(destdir):
    os.makedirs(destdir)
duplicate_file(os.system('copy %s %s' % (sys.argv[0],destdir)))