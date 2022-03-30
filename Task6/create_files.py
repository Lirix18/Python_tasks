import csv

data_users = [
        ['Иванов', 'Иван', 'Иванович'],
        ['Петров', 'Петр', 'Петрович'],
        ['Васильев', 'Василий', 'Васильевич']
              ]

data_hobby = [
    ['скалолазание', 'охота'],
    ['горные лыжи'],
    ['чтение книг', 'просмотр сериалов']
              ]


with open('users.csv', 'w', encoding='utf-8', newline='') as file_users:
    spamwriter1 = csv.writer(file_users)
    for i in data_users:
        spamwriter1.writerow(i)

with open('hobby.csv', 'w', encoding='utf-8', newline='') as file_hobby:
    spamwriter2 = csv.writer(file_hobby)
    for i in data_hobby:
        spamwriter2.writerow(i)
