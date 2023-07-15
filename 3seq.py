sample = input("Введите элементы 1-го списка: ")
numbers = list(sample.split(','))

sample = input("Введите элементы 2-го списка: ")
second_numbers = list(sample.split(','))

cloned_numbers = numbers
for i in numbers:
    if i in second_numbers:
        cloned_numbers.remove(i)
        second_numbers.remove(i)
print('result:', cloned_numbers)
