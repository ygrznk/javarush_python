# Самый главный кортеж

# Напишите программу, которая создает кортеж, содержащий несколько
# вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для поиска максимального
# элемента во вложенных кортежах и вывести результат.

# Напишите тут ваш код

my_tuple = ((1, 3, 4), (5, 4, 7), (6, 7, 4))
max_element = my_tuple[0][0]

for subtuple in my_tuple:
   for  element in subtuple:
        if element > max_element:
            max_element = element

print(max_element)