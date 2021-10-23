#1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
# извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError. Пример:
#>>> email_parse('someone@geekbrains.ru')
#{'username': 'someone', 'domain': 'geekbrains.ru'}
#>>> email_parse('someone@geekbrainsru')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  ...
#    raise ValueError(msg)
#ValueError: wrong email: someone@geekbrainsru
#Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?
import re
def email_parse(email_address):
    re_email = re.compile(r'(?P<username>([\w\.?]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_address): #если нет адреса с начала, то выводи исключение
        raise ValueError(f'wrong email: {email_address}')
    print(re_email.match(email_address).groupdict())

for i in [input("Enter email address:  ")]:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)


#Match.groupdict(default=None):
#Метод Match.groupdict() возвращает словарь, содержащий все именованные подгруппы совпадения, помеченные именем подгруппы name. Аргумент default используется для групп, которые не смогли захватить какой либо результат при сканировании строки и по умолчанию будут равны None.

#>>> import re
#>>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
#>>> m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}


