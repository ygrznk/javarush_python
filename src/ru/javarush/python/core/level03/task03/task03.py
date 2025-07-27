# Рост в футах и дюймах

# Напишите программу, которая переводит рост пользователя, заданный в сантиметрах, в футы и дюймы.
# Значение роста задано в переменной height_cm. Один дюйм равен 2.54 см, один фут равен 12 дюймам.
# Ваша задача — вычислить количество полных футов в данном росте и остаток перевести в дюймы.
# Результат выведите на экран.

height_cm = float(input("Введите рост в сантиметрах: "))

# Константы
cm_per_inch = 2.54
inch_per_foot = 12

# Напишите тут ваш код

height_inch = height_cm / cm_per_inch
height_foot = height_inch // inch_per_foot
height_inch -= height_foot*inch_per_foot

print (f'height is {height_foot} foot, and {height_inch} inches')