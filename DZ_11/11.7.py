
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.img = imaginary

    def __str__(self):
        return f'{self.real}+{self.img}i' if self.img > 0 else f'{self.real}{self.img}i'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.img * other.img),
                             (self.img * other.real + self.real * other.img))


cn = ComplexNumber(-5, 7)
cn1 = ComplexNumber(3, -4)
print(cn + cn1)
print(cn * cn1)
print()
print("Check")
print(complex(-5, 7) + complex(3, -4))  # calculation check
print(complex(-5, 7) * complex(3, -4))  # calculation check