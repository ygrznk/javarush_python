# Заморозка

# Напишите программу, которая создает несколько объектов типа
# frozenset из различных итерируемых объектов (список, строка).
# Программа должна:
# Создать frozenset из списка.
# Создать frozenset из строки.
# Выполнить объединение, пересечение, разность и симметрическую разность
# двух frozenset множеств.
# Вывести результаты каждой операции.

# Напишите тут ваш код

fset1 = frozenset([1,2,3])
fset2 = frozenset('zalupa')

fset_union = fset1.union(fset2)
print(fset_union)
fset_intersection = fset1.intersection(fset2)
print(fset_intersection)
fset_difference = fset1.difference(fset2)
print(fset_difference)
fset_symmetric_difference = fset1.symmetric_difference(fset2)
print(fset_symmetric_difference)

