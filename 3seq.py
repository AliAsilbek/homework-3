sample = input("Введите элементы 1-го списка: ")
numbers = list(sample.split(','))
sample = input("Введите элементы 2-го списка: ")
second_numbers = list(sample.split(','))
print(second_numbers)
for i in numbers:
    for b in second_numbers:
        if i == b:
            numbers[numbers.index(i)] = 'none'
            second_numbers[second_numbers.index(b)] = 'none1'
a = []
for i in numbers:
    if i.isdigit():
        a.append(i)
print('result:', a)

