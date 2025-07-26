# Пользовательский кортеж

# Напишите программу, которая создает кортеж из произвольного
# количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести последний элемент кортежа.
# Если кортеж пустой, программа должна вывести сообщение об
# этом.

# Напишите тут ваш код


my_list  = []
while True:
    element = str(input('Enter data: '))
    if element != '':
        my_list.append(element)
        continue
    else:
        break

my_tuple = tuple(my_list)


if len(my_tuple) != 0:
    print(my_tuple[-1])
else:
    print('Tuple empty')
