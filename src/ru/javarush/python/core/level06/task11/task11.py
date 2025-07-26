# Индексация
import random

# Напишите программу, которая создает множество из случайных чисел в
# диапазоне от 1 до 50.
# Затем программа должна вывести все элементы множества вместе с
# их "индексами", используя функцию enumerate().

# Напишите тут ваш код

my_set = {random.randint(1,50) for _ in range(10)}
for index, element in enumerate(my_set):
    print(index, element)