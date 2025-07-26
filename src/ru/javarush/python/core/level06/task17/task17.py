# Поиск подстроки.

# Напишите программу, которая принимает строку и подстроку от
# пользователя.
# Программа должна проверить, входит ли подстрока в строку с
# использованием оператора in,
# найти первое вхождение подстроки с использованием метода find() и
# подсчитать количество вхождений подстроки с использованием
# метода count().
# Программа должна вывести все результаты.

# Напишите тут ваш код

my_string = input('Enter a string: ')
my_substring = input('Enter a substring: ')
if my_substring in my_string:
    print('substring is in the string')
else:
    print('substring is not in the string')

index = my_string.find(my_substring)
if index == -1:
    print('substring is not in the string')
else:
    print(f'position of the substring is {index}')

counter = my_string.count(my_substring)
if counter == 0:
    print('substring is not in the string')
else:
    print(f'{counter} substring is in the string')


