import csv


def hash(s):    # Функция хеширование по данным из задания
    p = 67
    m = 10 ** 9 + 9  # это взяла из задания
    alph = ''.join([chr(i) for i in range(ord('А'), ord('я') + 1)])
    alph += 'ёЁ '
    hash_code = 0
    j = 0
    for i in s:
        hash_code += ((alph.index(i) + 1) * p ** j) % m
        j += 1
    return hash_code    # Возвращаем хеш-код


students_with_hash = []
with open('students.csv', encoding='utf-8') as f:   # Открываем файл
    reader = list(csv.DictReader(f, delimiter=',')) # Считываем
    for row in reader:
        row['id'] = hash(row['Name'])   # Меняем id на хеш-имя
        students_with_hash.append(row)
with open('students_with_hash.csv', 'w', encoding='utf-8') as f:    # Открываем файл на запись
    writer = csv.DictWriter(f, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])  # Задаём заголовки
    writer.writeheader()
    writer.writerows(students_with_hash)