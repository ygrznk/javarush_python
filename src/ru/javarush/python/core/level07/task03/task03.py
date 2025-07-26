# Проверка на пустоту.

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

# Напишите тут ваш код

my_dict1 = {1: 'one', 2: 'two', 3: 'three'}
my_dict2 = {4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
my_dict3 = {}

print(f'{len(my_dict1)}, {len(my_dict2)}, {len(my_dict3)}')

def check_empty(dick):
    if len(dick) == 0:
        return 'the dictionary is empty'
    else:
       return 'the dictionary not empty'

dicts = [my_dict1, my_dict2, my_dict3]

for i, d in enumerate(dicts):
    print(f'{i}: {check_empty(d)}')

