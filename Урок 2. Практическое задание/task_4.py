"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def row_sum(num, row_start = 1):
    if num == 1:
        return row_start
    else:
        row_next = - row_start / 2
        return row_start + row_sum(num - 1, row_next)

if __name__ == '__main__':
    x = int(input('Введите число элементов ряда: '))
    print(f'Сумма элементов ряда: {row_sum(x):}')