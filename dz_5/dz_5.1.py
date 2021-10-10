#1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
#>>> odd_to_15 = odd_nums(15)
#>>> next(odd_to_15)
#1
#>>> next(odd_to_15)
#3
#...
#>>> next(odd_to_15)
#15
#>>> next(odd_to_15)
#...StopIteration...
from itertools import islice
list_1 = []
n = int(input("Введите число: "))
def my_gen(): # собираем генератор из нечетных чисел от 1 до значения, который введет пользователь.
    for i in range(1, n):
        if i % 2 != 0:
            list_1.append(i)
            yield
for n in my_gen():   # так как yield запомнить только первое значение, то мы переберем еще раз их и выведем
    a = list(islice(list_1, n))[-1]
    print(a)













