#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#* Решить задачу под пунктом b, не создавая новый список.


kub_list = []  # список, в который сформируются числа возведенные в куб
kub_list_two = [] # список, в которые попадут числа к которым прибавится 17
all_sum = 0 # сумма тех чисел, которые пройдут фильтрацию


# собираем список

for i in range(1, 1000, 2): # так как мы начали с 1, а нам нужны не четные числа, то шаг будет 2.
    kub_list.append(i ** 3) # возводим в куб


# перебираем элементы списка

for ind, val in enumerate(kub_list):
    sum_digits = 0 # сюда пойдут все числа. обнуляем её, так как числа будут новые
    while val > 0: # при таком условии, а так же остатком от деления и целочисленным делением наше число должно стереться в 0
        sum_digits += val % 10
        val //= 10
        # затем, когда условие становиться ложно, то есть val = 0, то оно выходит из цикла
    if sum_digits % 7 == 0:
        # так как val = 0, то мы будем скаладывать индексы значений из списка в переменную all_sum
        all_sum += kub_list[ind]
print(all_sum)

for n in kub_list: # перебираем базовый список и к их значениям добавляем 17
    kub_list_two.append(n + 17)

# обнуляем значение для повторного использования
all_sum = 0
for ind, val in enumerate(kub_list_two):
    sum_digits = 0 # сюда пойдут все числа. обнуляем её, так как числа будут новые
    while val > 0: # при таком условии, а так же остатком от деления и целочисленным делением наше число должно стереться в 0
        sum_digits += val % 10
        val //= 10
        # затем, когда условие становиться ложно, то есть val = 0, то оно выходит из цикла
    if sum_digits % 7 == 0:
        # так как val = 0, то мы будем скаладывать индексы значений из списка в переменную all_sum
        all_sum += kub_list_two[ind]
print(all_sum)

















