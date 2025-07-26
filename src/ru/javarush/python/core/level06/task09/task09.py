# Котовасия

# Напиши программу, которая хранит множество из 5 самых популярных имен котов.
# Пользователь должен пытаться угадать их. Когда он угадывает имя кота, оно удаляется из множества.
# Цель игры - угадать всех котов за как можно меньшее число попыток.

# Напишите тут ваш код

my_set = {'belyash', 'zalupa', 'koreandr', 'mucek', 'hummer'}
count = 0
while my_set:
    count += 1
    string = input('Enter cats name: ')
    if string in my_set:
        my_set.remove(string)
print(f'you win from {count} tries')