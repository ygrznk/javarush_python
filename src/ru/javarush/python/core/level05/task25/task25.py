# Добавление элемента

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя новый элемент и добавить его в конец кортежа,
# создавая новый кортеж.
# Программа должна вывести обновленный кортеж.

# Напишите тут ваш код

my_tuple = tuple(input('enter data: ') for _ in range(5))
new_element = str(input('enter new element: '))
my_list = list(my_tuple)
my_list.append(new_element)
my_new_tuple = tuple(my_list)
print(my_new_tuple)
