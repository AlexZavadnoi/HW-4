"""
3) Определить функцию - генератор fib_generator(n), которая принимает
количество элементов последовательности Фибоначчи и итерируется по
элементам последовательности. например fib_generator(3) создаст итератор
для 3 элементов последовательности 0 1 1 Чи́сла Фибона́ччи — элементы числовой
последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,
987, 1597, 2584, 4181, 6765, 10946, 17711, …, в которой первые два числа равны
0 и 1, а каждое последующее число равно сумме двух предыдущих чисел

Написать подобную ф - ю fib_list(n) которая возвращает список с элементами
последовательности.

Вызов ф - и fib_list(3) вернет список[0, 1, 1]
"""


def fib_generator(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield i
        n1, n2 = n2, n1 + n2


arg = 3
fib_list = []

gener = fib_generator(arg)
print(type(gener))

# print(gener)
# generator fibonacci
print(next(gener))
print(next(gener))
print(next(gener))

# retern list fibonacci
for x in fib_generator(arg):
    fib_list.append(x)
print("List Fib", fib_list)
