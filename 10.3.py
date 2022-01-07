#3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
# Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.
#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
#Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
#Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется
# как целочисленное деление количества ячеекэтих двух клеток.
#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5.
# В этом случае метод make_order() вернёт строку: *****\n*****\n**.
#Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5.
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
#Подсказка: подробный список операторов для перегрузки доступен по ссылке.



class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return "\n".join(["#" * rows for i in range(self.nums // rows)]) + "\n" + "#" * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("Sum of cell is: ")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("Subtraction of cell is: ")
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else "Ячеек в первой клетки меньше, чем во второй. Вычитание не возможно!"

    def __mul__(self, other):
        print("Multiply of cell is: ")
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print("Floordiv of cell is: ")
        return Cell(self.nums // other.nums)

cell_1 = Cell(28)
cell_2 = Cell(15)
print(cell_1.make_order(5))
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)

















