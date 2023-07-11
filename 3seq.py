numbers1 = []
sample1 = input("Введите элементы 1-го списка: ")
for i in sample1:
    if not i.isdigit():
        end = sample1.find(i)
        number1 = sample1[:end]
        sample1 = sample1.replace(f'{number1},', '', 1)
        numbers1.append(number1)
numbers1.append(sample1)

numbers = []
sample = input("Введите элементы 2-го списка: ")
for i in sample:
    if not i.isdigit():
        end = sample.find(i)
        number = sample[:end]
        sample = sample.replace(f'{number},', '', 1)
        numbers.append(number)
numbers.append(sample)

for i in numbers1:
    for b in numbers:
        if i == b:
            numbers1[numbers1.index(i)] = 'none1'
            numbers[numbers.index(b)] = 'none'

a = []
for i in numbers1:
    if i.isdigit():
        a.append(i)

print("Result:", a)
