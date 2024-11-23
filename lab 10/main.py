"""
Шагаев Андрей ИУ7-14Б

Лабораторная работа №10 “Вычисление
приближённого значения интеграла”

Требуется написать программу для вычисления приближённого значения интеграла
известной, заданной в программе, функции двумя разными методами (по варианту).
Программа должна позволять задать начало и конец отрезка интегрирования, а также
N1 и N2 - количества участков разбиения.
Далее построить таблицу следующего вида:

         N1  N2
Метод 1  I1  I2
Метод 2  I3  I4

Далее на основе известной, заданной в программе, первообразной определить, какой
метод является наиболее точным. Для этого требуется вычислить и отобразить
абсолютную и относительную погрешности каждого из четырёх измерений. Метод,
измерение которого с одним из разбиений дало самое близкое к первообразной
значение, считается наиболее точным.
Затем для другого, менее точного метода, итерационно вычислить количество участков
разбиения, для которого интеграл будет вычислен с заданной точностью, на основе
формулы:

|𝐼(𝑁) − 𝐼(2𝑁)| < ε

Вывести приближенное значение интеграла и количество отрезков, необходимых для
его вычисления.
Интегрируемую функцию и первообразную необходимо описать в виде программных
функций, чтобы их можно было легко заменить на произвольные и убедиться, что
программа работает корректно.
Для методов интегрирования, использующих более двух точек на одной итерации
вычислений, считать все отрезки между соседними точками за отдельные участки
разбиения.
Если один из методов невозможно применить на заданном количестве участков
разбиения, в таблице ставится прочерк, однако сама таблица с остальными данными
выводится.
"""
from functions import *

while True:
    try:
        start = float(input("Введите начальное значение интегрирования: "))
        end = float(input("Введите конечное значение интегрирования: "))

        eps = 1e-6

        while end <= start or abs(end - start) < eps:
            print("Наччальное значение должно быть меньше, чем конечное")
            start = float(input("Введите начальное значение интегрирования: "))
            end = float(input("Введите конечное значение интегрирования: "))

        n1 = int(input("Введите первое целое количество участков разбиения: "))
        while n1 <= 0:
            print("Количества участков разбиения не может быть неположительным ")

        n2 = int(input("Введите второе целое  количество участков разбиения: "))
        while n1 <= 0:
            print("Количества участков разбиения не может быть неположительным ")

    except ValueError:
        print(">Некорректный ввод данных. Убедитесь что вводите числа. \n>При вводе количиества участков на ввод должно подаваться целое число.\n")
    else:
        break

i1, i2, i3, i4 = right_rectangle_method(start,end,n1), right_rectangle_method(start,end,n2), trapezoid_method(start,end,n1), trapezoid_method(start,end,n2)

print("\nОсновная таблица\n")
output_table(i1,i2,i3,i4,n1,n2)

true_integral = primitive_func(end) - primitive_func(start) 
print(true_integral)

abs_inaccuracy_i1, abs_inaccuracy_i2, abs_inaccuracy_i3, abs_inaccuracy_i4, = absolute_inaccuracy(i1, true_integral), absolute_inaccuracy(i2, true_integral),\
absolute_inaccuracy(i3, true_integral), absolute_inaccuracy(i4, true_integral)

print("\nТаблица абсолютных погрешностей \n")
output_table(abs_inaccuracy_i1, abs_inaccuracy_i2, abs_inaccuracy_i3, abs_inaccuracy_i4 ,n1 ,n2)

print("\nТаблица относительных погрешностей \n")
output_table(relative_inaccuracy(i1, true_integral),relative_inaccuracy(i2, true_integral),\
             relative_inaccuracy(i3, true_integral),relative_inaccuracy(i4, true_integral),n1,n2)

#Определение наиболее точного метода
#Используется переменная с not, так как в дальнейшем нам понадобиться наименее точный метод, чтобы узнать для него лучший исход
if min(abs_inaccuracy_i1,abs_inaccuracy_i2) < min(abs_inaccuracy_i3, abs_inaccuracy_i4):
    not_perfect_method , perfect_value = trapezoid_method, min(abs_inaccuracy_i1,abs_inaccuracy_i2)# метод прямоугольников лучше
else:
    not_perfect_method , perfect_value = right_rectangle_method, min(abs_inaccuracy_i3,abs_inaccuracy_i4)# метод трапеций лучше

if not_perfect_method == trapezoid_method:
    print(f"Наиболее точный метод: Метод правых прямоугольников с значением : {perfect_value}")
else:
    print(f"\nНаиболее точный метод: Метод трапеций с значением {perfect_value}")

while True:
    try:
        eps = float(input("Введите значение погрешности: "))
    except ValueError:
        print(">Некорректный ввод данных. Убедитесь что вводите числа.\n")
    else:
        break

better_n = find_better_amount_n(not_perfect_method, start, end, eps, max(n1, n2))
print(f"\nКоличетсво участков разбиения при заданной погрешности {eps:.6g}: {better_n}\n")

if not_perfect_method == right_rectangle_method:
    approximate_value = right_rectangle_method(start, end, better_n)
else:
    approximate_value = trapezoid_method(start, end, better_n)

print(f"Пoлученное приближенное значение интеграла: {approximate_value:10g}")

