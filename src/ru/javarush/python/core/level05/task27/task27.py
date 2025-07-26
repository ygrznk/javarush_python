# Сумма кортежей

# Напишите программу, которая создает кортеж, содержащий несколько вложенных
# кортежей из целых чисел.
# Программа должна использовать цикл for для вычисления суммы всех
# элементов во вложенных кортежах и
# вывести результат.

# Напишите тут ваш код

my_tuple = ((1, 3, 4), (5, 4, 7), (6, 7, 4))
my_tuple_sum = 0
my_list = []
for subtuple in my_tuple:
    my_subtuple_sum = 0
    for element in subtuple:
        my_subtuple_sum += element
    my_list.append(my_subtuple_sum)
my_summed_tuple = tuple(my_list)
print(my_summed_tuple)

for element in my_summed_tuple:
    my_tuple_sum += element
print(my_tuple_sum)


