# Лабораторная работа №6 “Списки. Часть 1”
# Шагаев Андрей ИУ7-14Б
# Задача 3:
# Найти значение K-го экстремума в списке.

arr = list(map(int,input("Введите элементы списка через пробел: ").split()))
while not arr:
    print('Список не может быть пустым')
    arr = list(map(int,input("Введите элементы списка через пробел: ").split()))

k = int(input('Введите индекс экстремума, значение которого надо найти: '))
while 0 >= k or k > len(arr) - 2:
    print('Индекс экстремума не может быть неположительным ')
    k = int(input('Введите индекс экстремума, значение которого надо найти: '))

count = 0
for i in range(1, len(arr) - 1):
    if (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
        count += 1
    if k == count:
        print('Элемент, являющийся {:d}-ым экстремумом:'.format(k),arr[i])
        break
else:
    print('{:d}-ого экстремума в заданном списке нет'.format(k))