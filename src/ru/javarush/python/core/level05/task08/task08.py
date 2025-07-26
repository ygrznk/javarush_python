# Стиратель
import random

# Напишите программу, которая создает список из 10 элементов,
# затем заменяет элементы с третьего по пятый на одно значение,
# запрашиваемое у пользователя.
# Программа должна вывести обновленный список.

# Напишите тут ваш код

my_list = [random.randint(1,100) for _ in range(10)]
print(my_list)
my_value = input("Enter value: ")
for i in range(3):
    my_list[2+i] = my_value
print(my_list)