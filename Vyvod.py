from random import shuffle
tasks = []

while True:
    task = input('Введите задачу: ')
    if task == '':
        break
    else:
        tasks.append(task)
print('')
print('Вывод задач: ')
shuffle(tasks)
for i in tasks:
    print(i)