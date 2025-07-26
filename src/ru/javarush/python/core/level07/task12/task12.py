# Словарь из списка кортежей.

# Напишите программу, которая создает список кортежей с
# информацией о сотрудниках (например, имя и должность).
# Программа должна:
# Использовать dictionary comprehension для создания
# словаря из списка кортежей.
# Вывести созданный словарь.

# Напишите тут ваш код

my_list = [('ivan', 'sales'), ('joe', 'cocksucker'), ('donald', 'whore')]
print(my_list)
my_dict = {key: value for key, value in my_list}
print(my_dict)