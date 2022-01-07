
#4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#    {
#      100: 15,
#      1000: 3,
#      10000: 7,
#      100000: 2
#    }
#Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
#Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


import os
import django
from collections import defaultdict

#def dir_info():
#берем информацию из библиотеки django
root_dir = django.__path__[0]#root_dir:'C:\\Users\\Диана\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\django'
django_files = defaultdict(int)
def dir_info():
    for root, dirs, files in os.walk(root_dir):
#print(root ,dirs, files)
# например
#C:\Users\Диана\AppData\Local\Programs\Python\Python39\lib\site-packages\django\views\generic
# #['__pycache__']
# #['base.py', 'dates.py', 'detail.py', 'edit.py', 'list.py', '__init__.py']
        for file in files:
            #в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
            # а значения — общее количество файлов (в том числе и в подпапках)
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            # из файла, размер файла можно получить из атрибута .st_size объекта os.stat. Получаем размер допустим 4880 байт. Переводим в str
            # и с помощью len проверяем длину строки. Она состоит из 4 цифр и в конце возводим 10 в 4 степень это в диапозоне 10000 тысяч.
            django_files[size] += 1 # суммируется кол-во
        #print(django_files)
        #defaultdict( <class 'int'>, {10000: 631, 1000: 330, 100000: 410, 100: 7, 10: 85, 1000000: 4})


    for weight, counts in sorted(django_files.items()):
        print(f" диапозон до {weight} : количество {counts}")
dir_info()





