# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести
# каждое слово с новой строки. Строки необходимо пронумеровать. Если в слово
# длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку из нескольких слов, разделённых '
                    'пробелами: ').split()
for num, word in enumerate(user_string):
    print(num+1, word[:10], sep='. ')
