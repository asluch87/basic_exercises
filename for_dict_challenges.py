# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_name = {}

for student in students:  # лучше назвать student вместо names
    name = student['first_name']  # обращаемся к текущему студенту
    
    if name in count_name:
        count_name[name] += 1
    else: 
        count_name[name] = 1

# Вывод делаем ПОСЛЕ цикла, когда все посчитано
for name, count in count_name.items():
    print(f"{name}: {count}")
 


















# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
all_names = [student['first_name'] for student in students]
count_name = {}
for stud in students:
    name = stud["first_name"]
    if name in count_name:
        count_name[name] +=1
    else:
        count_name[name] = 1

print(count_name)
max_count = 0
most_common_name = ""

for name in set(all_names):  # set() убирает дубликаты
    count = all_names.count(name)
    if count > max_count:
        max_count = count
        most_common_name = name

print(f"Самое частое имя среди учеников: {most_common_name}")
   



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]



for class_index in range(len(school_students)):
    count_name = {}
    
  
    for student in school_students[class_index]:
        name = student['first_name']
        if name in count_name:
            count_name[name] += 1
        else:
            count_name[name] = 1
    
    
    max_count = 0
    most_common_name = ""
    for name, count in count_name.items():
        if count > max_count:
            max_count = count
            most_common_name = name
    
    print(f"Самое частое имя в классе {class_index + 1}: {most_common_name}")
   







# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
# ???

def get_gender_text(name):
    """Возвращает текстовое описание пола"""
    if name in is_male:
        return "мальчик" if is_male[name] else "девочка"
    return "пол неизвестен"


for class_info in school:
    print(f"Класс: {class_info['class']}")
    for student in class_info['students']:
        name = student['first_name']
        print(f"  {name} - {get_gender_text(name)}")


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}


# Создаем словари для подсчета
boys_by_class = {}
girls_by_class = {}

# Подсчитываем мальчиков и девочек по классам
for class_info in school:
    class_name = class_info['class']
    boys_count = 0
    girls_count = 0
    
    for student in class_info['students']:
        name = student['first_name']
        if name in is_male:
            if is_male[name]:
                boys_count += 1
            else:
                girls_count += 1
    
    boys_by_class[class_name] = boys_count
    girls_by_class[class_name] = girls_count

# Находим класс с максимальным количеством мальчиков
max_boys_class = max(boys_by_class, key=boys_by_class.get)
max_boys_count = boys_by_class[max_boys_class]

# Находим класс с максимальным количеством девочек
max_girls_class = max(girls_by_class, key=girls_by_class.get)
max_girls_count = girls_by_class[max_girls_class]

# Выводим результаты
print(f"Больше всего мальчиков в классе {max_boys_class}")
print(f"Больше всего девочек в классе {max_girls_class}")





