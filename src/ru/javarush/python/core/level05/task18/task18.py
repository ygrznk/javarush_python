# Чистим список

# Напишите программу, которая создает список из
# 10 случайных чисел в диапазоне от 1 до 20.
# Затем программа должна удалить из списка все
# четные числа с использованием цикла.
# Программа должна вывести исходный и обновленный списки.

# Напишите тут ваш код

import random

my_list = [random.randint(1, 20) for _ in range(10)]
my_odd_list = my_list[:]
for i in range(len(my_odd_list)-1, -1, -1):
    if my_odd_list[i] % 2 == 0:
        del my_odd_list[i]
print(my_list)
print(my_odd_list)