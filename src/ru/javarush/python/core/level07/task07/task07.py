# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код

my_dict = {'title':'kkkd', 'author':'fdfe', 'year':1993}
if 'author' in my_dict:
    print('author key is in my_dict')
else:
    print('author key is not in my_dict')

value = my_dict.get('publisher')
if value is not None:
    print('publisher key is in my_dict')
else:
    print('publisher key is not in my_dict')

if 'title' in my_dict.keys():
    print('title key is in my_dict')
else:
    print('title key is not in my_dict')