# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

num = int(input("Введите количество элементов: "))
num_dict = dict()
summ = 0
for i in range(1, num + 1):
    summ += (1 + 1/i) ** i
    num_dict[i] = round((1 + 1 / i) ** i, 2)
print(num_dict)
print(round(summ, 2))