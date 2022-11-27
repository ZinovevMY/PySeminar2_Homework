# Реализуйте алгоритм перемешивания списка.

import random

num_count = int(input("Введите количество элементов в списке: "))
num_list = list()

for _ in range(num_count):
    num_list.append(random.randint(-10, 25))
print(num_list)
print("А теперь попробуем перемешать список!")
for _ in range(int(len(num_list)/2)):
    elem1 = random.randint(0, num_count - 1)
    elem2 = random.randint(0, num_count - 1)
    tmp = num_list[elem2]
    num_list[elem2] = num_list[elem1]
    num_list[elem1] = tmp
print("Получилось так: ")
print(num_list)