# Детектив
from copyreg import pickle

# Напиши функцию set_detector, которая проходится по
# списку(кортежу) своих аргументов и определяет -
# есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами
# параметров (с множеством и без).

# Напишите тут ваш код

my_tuple1 = (1, 2, 3, {3, 4, 5})
my_tuple2 = (3, 4, 6)

def set_detector(array):
    for element in array:
        if type(element) is set:
            print('True')
            return True
    print('False')
    return False

set_detector(my_tuple1)
set_detector(my_tuple2)
