# Группировка кортежей

# Напишите программу, которая создает кортеж из 6 элементов, запрашиваемых у пользователя.
# Затем программа должна сгруппировать их в 3 кортежа по 2 элемента.
# Затем объединить 1 и 3 кортежи и вывести обновленный кортеж на экран.

# Напишите тут ваш код

my_tuple = tuple(input('enter data: ') for _ in range(6))
my_tuple1 = my_tuple[0:2]
my_tuple2 = my_tuple[2:4]
my_tuple3 = my_tuple[4:6]

my_new_tuple = tuple(list(my_tuple1) + list(my_tuple3))
print(my_new_tuple)