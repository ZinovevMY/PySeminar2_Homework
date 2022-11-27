# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input("Введите число: "))
sum_of_products = 1
result = list()
for i in range(1, num + 1):
    result.append(sum_of_products)
    sum_of_products += sum_of_products * i
print(result)