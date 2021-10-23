#3. Написать декоратор для логирования типов позиционных аргументов функции, например:
#def type_logger...
#    ...

#@type_logger
#def calc_cube(x):
#   return x ** 3

#>>> a = calc_cube(5)
#5: <class 'int'>
#Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#>>> a = calc_cube(5)
#calc_cube(5: <class 'int'>)

from functools import wraps

def type_logger(func):# функция type_logger - это декоратор,
    # его задача определять тип аргумента в функции calc_cube для каждого значения в корректный вид
    @wraps(func) # далее идет внутренняя локальная функция
    def wrapper(*args, **kwargs): #аргументами может быть любое значение
        num_list = [i for i in (*args, *kwargs.values())] # в с
        #[9, 5.5, {'number': 3}, (2, 'name'), {9}, [19, 3], 'str', 'Diana']
        # подготовка инфо, распоковываем кортежи с помощью звездочек
           ## нужно получить в ответе:     calc_cube(5: <class 'int'>)

        n = [f"{func.__name__}({i}: {type(i)})" for i in num_list] # формируем строки, с помощью форматирования
      #  ["calc_cube(9: <class 'int'>)", "calc_cube(5.5: <class 'float'>)", "calc_cube({'number': 3}: <class 'dict'>)",
      #   "calc_cube((2, 'name'): <class 'tuple'>)", "calc_cube({9}: <class 'set'>)",
      #   "calc_cube([19, 3]: <class 'list'>)", "calc_cube(str: <class 'str'>)", "calc_cube(Diana: <class 'str'>)"]
        print(*n, "Результат: ", *func(*args, **kwargs), sep="\n")
    return wrapper


@type_logger
def calc_cube(*x, **y): #основная функция calc_cube должна возводить в куб переданный параметр,
    # только если он имеет тип float или int
    #(9, 5.5, {'number': 3}, (2, 'name'), {9}, [19, 3], 'str')
    #{'firstname': 'Diana'}
    num_list = [i for i in (*x, *y.values()) if isinstance(i, int) or isinstance(i, float)] # сюда зайдет только 9 и 5.5
    return [i ** 3 for i in num_list]
calc_cube(9, 5.5, {"number": 3}, (2, "name"), {9, 9, 9}, [19, 3], "str", firstname= "Diana")



