# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = input('Введите число: ')
print(f'{n}+{n+n}+{n+n+n} будет {int(n) + int(n * 2) + int(n * 3)}')
