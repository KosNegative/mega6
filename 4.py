import random, csv
from string import ascii_letters, digits


def create_password():  # Функция создания паролей
    letter_digit = ascii_letters + digits
    password = ''.join(random.choices(letter_digit, k=8))
    return password


def create_login(name): # Функция создания логинов
    name = name.split()
    return f'{name[0]}_{name[1][0]}{name[2][0]}'


with open('students.csv', encoding='utf-8') as file:    # Открываем файл
    reader = csv.DictReader(file, delimiter=',')    # Считываем
    reader = list(reader)
    for person in reader:
        person['login'] = create_login(person['Name'])
        person['password'] = create_password()

with open('students_password.csv', 'w', encoding='utf-8') as file:  # Открываем файл на запись
    names = ['id', 'Name', 'titleProject_id', 'class', 'score', 'login', 'password']    # Задаём заголовки
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writerows(reader)