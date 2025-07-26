# НДС

# Напишите функцию calculate_total_cost(price, tax=0.2), которая принимает цену товара и необязательный параметр
# налог (по умолчанию 20%).
# Функция должна вычислять и выводить общую стоимость товара с учетом налога.
# Затем напишите программу, которая вызывает эту функцию с различными параметрами.

# Напишите тут ваш код

def calculate_total_cost(price, tax=0.2):
    total_price = price * (1 + tax)
    print(total_price)
    return total_price


calculate_total_cost(10)
calculate_total_cost(price = 13.2, tax = 0.1)
calculate_total_cost(10, 0.3)