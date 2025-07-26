# Четкий но случайный
import random

# Напишите программу, которая создает множество из 10 случайных чисел
# в диапазоне от 1 до 100.
# Программа должна получить подмножество всех четных чисел из этого
# множества и вывести его.

# Напишите тут ваш код

my_set = {random.randint(1,100) for _ in range(10)}
print(my_set)
my_even_set = set()
for element in my_set:
    if element % 2 == 0:
        my_even_set.add(element)
print(my_even_set)
