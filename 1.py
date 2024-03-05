import csv

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter=','))
    sum_score = {}
    count_scores = {}
    for row in reader:
        if 'Хадаров Владимир' in row['Name']:   # Если ученик - Владимир Хадаров
            print(f'Ты получил: {row["score"]}, за проект - {row["titleProject_id"]}')  # Выводим ответ

        sum_score[row['class']] = sum_score.get(row['class'], 0) + (int(row['score']) if row['score'] != 'None' else 0)
        count_scores[row['class']] = count_scores.get(row['class'], 0) + 1

    for row in reader:
        if row['score'] == 'None':
            row['score'] = round(sum_score[row['class']] / count_scores[row['class']], 3)

with open('students_new.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['id', 'Name', 'titleProject_id', 'class', 'score'])
    writer.writeheader()
    writer.writerows(reader)