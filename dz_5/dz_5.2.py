
n = int(input("Введите число: "))
print(*[i for i in range(1, n) if i % 2 != 0])
