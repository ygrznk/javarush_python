# Первый на выход
import random

# Напишите программу, которая создает список из 5 элементов, запрашивает у пользователя элемент для удаления
# и удаляет первый найденный элемент из списка с использованием метода remove().
# Программа должна вывести обновленный список.

# Напишите тут ваш код

my_list = [random.randint(1,100) for _ in range(5)]
print(my_list)
my_element = int(input('Enter a number: '))
my_list.remove(my_element)
print(my_list)