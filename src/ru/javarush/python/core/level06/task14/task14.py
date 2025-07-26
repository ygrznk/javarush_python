# Разность множеств
import random

# Напишите программу, которая создает два множества из случайных чисел.
# Первое множество содержит 10 случайных чисел в диапазоне от
# 1 до 20, а второе множество содержит 10 случайных чисел в
# диапазоне от 10 до 30.
# Программа должна найти разность первого множества со вторым с
# использованием метода difference().
# И симметрическую разность с использованием метода
# symmetric_difference().
# Программа должна вывести оба результата.

# Напишите тут ваш код

my_set1 = {random.randint(1,20) for _ in range(10)}
my_set2 = {random.randint(10,30) for _ in range(10)}

my_set_diff = my_set1.difference(my_set2)
print(my_set_diff)

my_set_symmetric_diff = my_set1.symmetric_difference(my_set2)
print(my_set_symmetric_diff)
