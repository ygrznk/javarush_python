# Лес

# Напишите программу, которая создает список из
# названий деревьев, затем с использованием цикла и
# функции enumerate() выводит каждый элемент
# списка и его индекс.

# Напишите тут ваш код

tree_list = ['sosna', 'bereza', 'topol', 'vishnja']
for index, tree in enumerate(tree_list):
    print(f'on index {index} - the tree is {tree}')