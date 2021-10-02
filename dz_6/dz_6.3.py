#3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
#Фрагмент файла с данными о пользователях (users.csv):
#Иванов,Иван,Иванович
#Петров,Петр,Петрович
#Фрагмент файла с данными о хобби (hobby.txt):
#скалолазание,охота


from json import dump
from itertools import zip_longest

with open("hobby.txt", "r", encoding="utf-8") as hobby:
    with open("users.txt", "r", encoding="utf-8") as users:
        if len(users.readlines()) >= len(hobby.readlines()):
            # курсор опускается вниз и поэтому важно его опять поднять на верх с помощью метода seek
            users.seek(0)
            hobby.seek(0)
            # теперь создаем файл dict.json, в режиме записи. Если закончаться имена, то выводиться None.
            with open("dict.json", "w", encoding="utf-8") as file:
                #zip_longest() объединяет фамилии и хобби в кортежи
                # для красивого принта нужно убрать запятые. В месте где запятые, склеиваем так, чтобы просто был пробел
                all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)
                # используем .strip() для того чтобы убрать переходы на след. строку.  el[0] на ключ.  el[1] на значение
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in all_list}
                # сформировался словарь. Его мы и отправим. ensure_ascii=False это для кириллицы.
                # indent=4 - для красивого отображения
                dump(my_dict, file, ensure_ascii=False, indent=4)
            print(my_dict)
                # в другом случае, если хобби будет больше чем имен, то пусть выводиться 1
        else:
            exit(1)
