# Нашли кота

# Напишите функцию create_cat_profile(name, age, breed="Неизвестно"), которая принимает имя, возраст и
# необязательный параметр "порода" (по умолчанию "Неизвестно").
# Функция должна выводить профиль кота в формате "Имя: [name], Возраст: [age], Порода: [breed]".
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код

def create_cat_profile(name, age, breed="Неизвестно"):
    print(f'Имя: {name}, Возраст: {age}, Порода: {breed}')
    return

create_cat_profile('rex', 3)
create_cat_profile(name='gosha', age= 4, breed= 'collie')
create_cat_profile('boka', 12, 'terrier')