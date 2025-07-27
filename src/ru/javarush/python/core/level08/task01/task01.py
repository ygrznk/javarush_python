# Системные функции.

# Напишите программу, которая создает несколько объектов различных типов и
# использует функции id(), hash(), и dir() для выполнения следующих операций:
# Определить и вывести уникальные идентификаторы объектов с помощью id().
# Вывести хеш-значения хешируемых объектов с помощью hash().
# Вывести список атрибутов и методов объекта с помощью dir().

# Напишите тут ваш код

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {'a', 'b', 'c'}
my_string = 'yollo'

print(f'my_list id is:\t{id(my_list)}\n'
      f'my_tuple id is:\t{id(my_tuple)}\n'
      f'my_dict id is:\t{id(my_dict)}\n'
      f'my_set id is:\t{id(my_set)}\n'
      )

print(f'my_tuple hash is:\t{hash(my_tuple)}\n'
      f'my_string hash is:\t{hash(my_string)}\n'
      )

print(f'my_list dir is:\t{dir(my_list)}\n'
      f'my_tuple dir is:\t{dir(my_tuple)}\n'
      f'my_dict dir is:\t{dir(my_dict)}\n'
      f'my_set dir is:\t{dir(my_set)}\n'
      f'my_string dir is:\t{dir(my_string)}\n'
      )