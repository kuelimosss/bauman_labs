# Лабораторная работа №7 “Списки. Часть 2”
# Шагаев Андрей ИУ7-14Б
# После каждого элемента целочисленного списка, имеющего свойство по варианту, добавить его удвоенное значение,
# без использования вложенных циклов. Без insert append срезов
# Вариант №2: Чётные элементы
#ввод списка
arr = list(map(int,input("Введите целочисленные элементы списка через пробел: ").split()))
while not arr:
    print('Список не может быть пустым')
    arr = list(map(int,input("Введите целочисленные элементы списка через пробел: ").split()))
#подсчёт количества четных чисел
count_even = len([x for x in arr if x % 2 == 0])
#добавление необходимых нулевых элементов в список
arr += [0] * count_even

index = -1
for i in range(len(arr)-count_even-1,-1,-1):
    if arr[i] % 2 == 0:
        arr[index] = arr[i] * 2
        arr[index - 1] = arr[i]
        index -= 2
    else:
        arr[index] = arr[i]
        index -= 1

print(*arr, sep  = ', ')