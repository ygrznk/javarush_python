# Лига Плюща

# Напишите программу, которая создает словарь с информацией о
# студенте (имя, возраст, университет).
# Программа должна:
# Проверить наличие значения "MIT" с использованием метода values().
# Проверить наличие значения "Harvard" с использованием функции set().
# Проверить наличие значения 22 с использованием генератора.

# Напишите тут ваш код

my_dict = {'name' : 'john', 'age' : 22, 'university' : 'MIT'}
if 'MIT' in my_dict.values():
    print('mit is in values of my_dict')
else:
    print('mit is not in values of my_dict')

if 'Harvard' in set(my_dict.values()):
    print('harvard is in values of my_dict')
else:
    print('harvard is not in values of my_dict')


if any(value == 22 for value in my_dict.values()):
    print('22 is in values of my_dict')
else:
    print('22 is not in values of my_dict')