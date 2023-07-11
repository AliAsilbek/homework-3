values = []
questions = []
amount = input('Введите количество элементов: ')
print(type(amount))

while not amount.isdigit() is True:
    amount = input('Введите число: ')

for question in range(int(amount) + 1):
    questions.append(question)

del questions[0]

for question in questions:
    value = input(f"Введите {question} элемент: ")
    if not value.isdigit():
        value = input(f"Введите число: ")
    values.append(int(value))
print(sorted(values))
