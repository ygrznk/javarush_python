# Обход словаря.

# Напишите программу, которая создает словарь с информацией о
# человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с
# использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и
# вывода ключей и значений.

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

def print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        print("\t" * indent + str(key) + ': ', end='')
        if isinstance(value, dict):
            print()
            print_dict(value, indent + 1)
        else:
            print(value)

print_dict(person)