# Удаление элемента
import random

# Напишите программу, которая создает список из 5 элементов,
# запрашивает у пользователя индекс элемента для удаления
# и удаляет элемент по этому индексу с использованием метода pop().
# Программа должна вывести обновленный список и удаленный элемент.
# Если индекс не существует, программа должна вывести сообщение об этом.

# Напишите тут ваш код

my_list = [random.randint(1,100) for _ in range(5)]
print(my_list)
my_index = int(input("Enter index: "))
if my_index >= len(my_list) or my_index < 0:
    print("Index out of range")
else:
    popped_item = my_list.pop(my_index)
    print(my_list)
    print(popped_item)


