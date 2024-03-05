import csv

with open('students.csv', encoding='utf-8') as file:    # Открываем ффайл
    reader = csv.DictReader(file, delimiter=',')    # Считываем
    reader = list(reader)
    request = input()   # Запрашиваем ввод
    while request != 'СТОП':    # Пока ввод не равен СТОП
        is_real_project = False
        for i in range(len(reader)):
            if reader[i]['titleProject_id'] == request: # Если id равен id проекта
                project_id = reader[i]['titleProject_id']
                name = reader[i]['Name'].split()
                score = reader[i]['score']
                print(f'Проект № {project_id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}')
                is_real_project = True  # Проект найден
                break
        if not is_real_project: # Проект не найден
            print('Ничего не найдено')
        request = input()