# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("Введите число: ")
if '.' in num:
    num = num.replace('.', '')
if ',' in num:
    num = num.replace(',', '')
print(sum(map(int, num)))
