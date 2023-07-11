numbers = set()
print(type(numbers))
sample = input("Введите элементы списка через запятую: ")
for i in sample:
    if not i.isdigit():
        end = sample.find(i)
        number = sample[:end]
        sample = sample.replace(f'{number},', '', 1)
        numbers.add(number)
numbers.add(sample)
print('Результат:', numbers)