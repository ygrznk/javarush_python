# Просто и сложно одновременно

# Создай 5 кортежей с разной длинной:
# 0 элементов, 1 элемент, 5 элементов,
# 100 элементов, 1000 элементов.
# Выведи их на экран.

# Напишите тут ваш код
import random

my_tuple0 = ()
my_tuple1 = (1,)
my_tuple5 = (1, 2, 3, 4, 5)
my_tuple100 = tuple([random.randint(1,100) for _ in range(100)])
my_tuple1000 = tuple([random.randint(1,100) for _ in range(1000)])

print(my_tuple0)
print(my_tuple1)
print(my_tuple5)
print(my_tuple100)
print(my_tuple1000)