# Четкий список
import random

# Напишите программу, которая создает список из 10 целых чисел.
# С использованием цикла for замените все четные
# элементы списка на строку "четное".
# Программа должна вывести обновленный список.

# Напишите тут ваш код

my_list = [random.randint(1,1000) for _ in range(10)]
print(my_list)
for index, element in enumerate(my_list):
    if element % 2 == 0:
        my_list[index] = 'четное'
print(my_list)
