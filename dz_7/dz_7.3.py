#3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#|--my_project
#   ...
#  |--templates
#   |   |--mainapp
#   |   |  |--base.html
#   |   |  |--index.html
#   |   |--authapp
#   |      |--base.html
#   |      |--index.html
#Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён);
#предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.





# Задача в том, чтобы создать директорию templates, чтобы она была на равне с authapp, mainapp, settings
# содержимое templates было скопировано как в подпапке authapp и mainapp

from os import path, walk, listdir
import shutil

project_name = "my_project_1"

try:
    for root, dirs, files in walk(project_name):
#my_project_1 ['authapp', 'mainapp', 'settings'] []
#my_project_1\authapp ['templates'] ['models.py', 'views.py', '__init__.py']
#my_project_1\authapp\templates ['authapp'] []
#my_project_1\authapp\templates\authapp [] ['base.html', 'index.html']
#my_project_1\mainapp ['templates'] ['models.py', 'views.py', '__init__.py']
#my_project_1\mainapp\templates ['mainapp'] []
#my_project_1\mainapp\templates\mainapp [] ['base.html', 'index.html']
#my_project_1\settings [] ['dev.py', 'prod.py', '__init__.py']
        if "templates" in dirs and root != project_name:
       # print("содержится")
    #else:
     #   print("не содержиться")

    # содержиться в строчке 2 и 5
#my_project_1\authapp ['templates'] ['models.py', 'views.py', '__init__.py']
#my_project_1\mainapp ['templates'] ['models.py', 'views.py', '__init__.py']
            for i in listdir(path.join(root, "templates")):  # он посморел что в папках authapp и mainapp есть templates
           # print(i)
            #authapp
            #mainapp

           #shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)
           # - рекурсивно копирует всё дерево директорий с корнем в src, возвращает директорию назначения.
                shutil.copytree(path.join(root, "templates", i), path.join(project_name, "templates", i))
except FileExistsError:
    print("Уже работает с templates в директории!")










