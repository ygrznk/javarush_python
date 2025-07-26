# Замена

# Напишите программу, которая создает множество,
# содержащее названия нескольких фруктов.
# Программа должна вывести фрукты на экран.
# Затем программа должна запросить у пользователя
# индекс (с учетом порядка вывода на экран) и
# новое название фрукта для замены.
# Затем найти фрукт по индексу, заменить его новым
# названием и вывести обновленное множество.

 # Напишите тут ваш код

fruit_set = {'apple', 'banana', 'cherry', 'orange', 'strawberry', 'kiwi'}
print(fruit_set)
fruit_list = list(fruit_set)
for i, fruit in enumerate(fruit_list):
    print(f"{i}: {fruit}")

index = int(input("Input index from 0 to 5: "))
new_name = input("Input new fruit name: ")
fruit_list[index] = new_name

print(set(fruit_list))
