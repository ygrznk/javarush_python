# Использование глобальной переменной

# Напишите программу, в которой есть глобальная переменная counter, равная 0.
# Напишите функцию increment_counter(), которая увеличивает значение этой переменной на 1 каждый раз, когда она вызывается.
# Затем вызовите эту функцию несколько раз и выведите значение глобальной переменной counter.

# Напишите тут ваш код

counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print(increment_counter())
print(increment_counter())
print(increment_counter())