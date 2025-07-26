# Номер кортежа
import random

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя индекс элемента и вывести значение элемента
# по этому индексу.
# Если индекс выходит за пределы кортежа, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код

my_tuple = tuple(input('enter data: ') for _ in range(5))
my_index = int(input('enter index: '))
if my_index >= 0 and my_index < len(my_tuple):
    print(my_tuple[my_index])
else:
    print('index out of range')