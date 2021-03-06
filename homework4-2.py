# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

def gen_list():
    """Функция генерирует список заданной длинны из случайных целых чисел из
    диапазона, заданного пользователем"""
    from random import randint
    lst = []
    try:
        n = int(
            input('Введите нижнюю границу для генерации случайных чисел для '
                  'заполнения списка: '))
        m = int(
            input('Введите верхнюю границу для генерации случайных чисел для '
                  'заполнения списка: '))
        for i in range(int(input('Введите длинну исходного списка: '))):
            lst.append(randint(n, m))
        return lst
    except ValueError:
        lst = []
        print('Ошибка! Введите целое число!')
        return lst

try:
    l = gen_list()
    if len(l)== 0:
        raise ValueError
    print(f'Ваш список: {l}')
    print(f'Результат: {[l[k] for k in range(1, len(l)) if l[k] > l[k - 1]]}')
except ValueError:
    print('Ошибка при создании списка. Введены некорректные значения.')
