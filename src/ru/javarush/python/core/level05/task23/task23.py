# Обратный кортеж

# Напишите программу, которая создает кортеж из произвольного количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести кортеж в обратном порядке с использованием среза.

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
print(my_tuple[::-1])
