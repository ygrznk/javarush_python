# Сортировка строк по длине

# Напишите программу, которая создает список из 5
# строк, запрашиваемых у пользователя.
# Затем программа должна отсортировать список по
# длине строк и вывести отсортированный список.

# Напишите тут ваш код

my_string_list = [str(input('enter string: ')) for _ in range(5)]

def string_len(string):
    return len(string)

my_string_list.sort(key=string_len)

print(my_string_list)