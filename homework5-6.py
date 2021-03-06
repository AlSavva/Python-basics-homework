# Необходимо создать (не программно) текстовый файл, где каждая строка
# описывает учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий
# название предмета и общее количество занятий по нему. Вывести словарь на
# экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
try:
    with open('text_6.txt', 'r', encoding='utf-8') as in_file:
        hour = []
        time = str()
        my_dict = {}
        for line in in_file:
            for word in line.split():
                time += ''.join(ch for ch in word if ch.isdigit())
                if time.isdigit():
                    hour.append(int(time))
                    time = str()
            my_dict[line.split()[0][:-1]] = sum(hour)
            hour = []
        print(my_dict)
except IOError:
    print('IOError')
