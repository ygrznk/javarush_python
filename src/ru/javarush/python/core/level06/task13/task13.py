# Объединение и пересечение

# Напишите программу, которая создает два множества из
# элементов, запрашиваемых у пользователя.
# Программа должна объединить эти множества с
# использованием метода union() и найти их пересечение с
# использованием метода intersection().
# Программа должна вывести оба результата

# Напишите тут ваш код



def add_element():
    my_set = set()
    while True:
        element = input('Enter a element: ')
        if element:
            my_set.add(element)
            continue
        return my_set

my_set1 = add_element()
print(my_set1)
my_set2 = add_element()
print(my_set2)

my_set_union = my_set1.union(my_set2)
print(my_set_union)

my_set_intersection = my_set1.intersection(my_set2)
print(my_set_intersection)