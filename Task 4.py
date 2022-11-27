# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

elem_count = int(input("Введите кол-во элементов: "))
index_numbers = input("Введите номера индексов: ")
index_numbers = index_numbers.replace(' ', '')
index_numbers = map(int, index_numbers)
index_numbers = list(index_numbers)
num_list = list()
product_numbers = 1

for i in range(-elem_count, elem_count + 1):
    num_list.append(i)
for j in range(len(index_numbers)):
    if index_numbers[j] < len(num_list):
        product_numbers *= num_list[index_numbers[j]]
    else:
        print(f"В списке нет элемента с индексом {index_numbers[j]}!")

print(num_list)
print(index_numbers)
print(f"Произведение элементов списка = {product_numbers}")