# Поиск строки
import random
# Напишите программу, которая создает список из 10 элементов.
# Программа просит пользователя ввести строку, а потом проверяет -
# есть она в списке или нет.

# Напишите тут ваш ко
#
my_list = [str(random.randint(1,1000)) for _ in range(10)]
print(my_list)
my_value = input('Enter a number: ')
if my_value in my_list:
    print('the number is in the list')
else:
    print('the number is not in the list')