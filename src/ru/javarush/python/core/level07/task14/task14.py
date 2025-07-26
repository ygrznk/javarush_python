# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о
# человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более
# глубокого уровня вложенности.
# Добавить новый элемент во вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

# Напишите тут ваш код

person = {
    "name": "Alice",
    "details": {
        "age": 25,
        "city": "New York",
        "address": {
            "street": "123 Main St",
            "zip": "10001"
        },
        "mother": "Jane Smith"
    },
    "gender": "female"
}

person['name'] = 'Andre'
person['details']['city'] = 'LA'
person['details']['address']['street2'] = '122 Main St'
del person['details']['address']['zip']
del person['gender']
print(person)
