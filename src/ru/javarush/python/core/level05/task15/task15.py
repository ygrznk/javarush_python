# Сортировки
import random

# Напишите программу, которая создает список из 10
# случайных чисел в диапазоне от 1 до 100.
# Затем сортирует его по возрастанию и убыванию.
# Программа должна вывести исходный список,
# отсортированный по возрастанию и по убыванию списки.

# Напишите тут ваш код

my_list = [random.randint(1, 100) for _ in range(10)]
my_sorted_list_asc = sorted(my_list, reverse=False)
my_sorted_list_desc = sorted(my_list, reverse=True)
print(my_list)
print(my_sorted_list_asc)
print(my_sorted_list_desc)
