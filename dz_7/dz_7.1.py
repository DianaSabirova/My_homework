#1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#|--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
#Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок
# под конкретный проект; можно ли будет при этом расширять конфигурацию
# и хранить данные о вложенных папках и файлах (добавлять детали)?

import os
dir_name = os.path.join("my_project", "settings")
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

dir_name_one = os.path.join("my_project", "mainapp")
if not os.path.exists(dir_name_one):
    os.makedirs(dir_name_one)

dir_name_two = os.path.join("my_project", "adminapp")
if not os.path.exists(dir_name_two):
    os.makedirs(dir_name_two)

dir_name_three = os.path.join("my_project", "authapp")
if not os.path.exists(dir_name_three):
    os.makedirs(dir_name_three)
