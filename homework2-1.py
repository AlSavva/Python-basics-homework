# Создать список и заполнить его элементами различных
# типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки
# типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

my_list = [56, 1.45852, 'text', True, [1, 1.2], ('as', 'sd'),
           {1, 5, 6, (1, 5)}, {'False': 'Ложь', 'True': 'Правда'}]
print('Давайте посмотрим, какие типы элементов '
      'могут быть сохранены в список.')
print(f'Для примера возьмем вот такой список: {my_list}'
      f'\nи разберем его по элементам')
for n in my_list:
    print(f'Элемент {n} имеет тип {str(type(n))[8:-2]}.')
print('Список может содержать элементы произвольных типов.')
