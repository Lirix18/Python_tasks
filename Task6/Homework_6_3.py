from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as file_users:
    users = file_users.readlines()

with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:
    hobbys = file_hobby.readlines()

if len(users) < len(hobbys):
    exit(1)

dictionary = {}

for fio, hobby in zip_longest(users, hobbys):
    fio = fio.replace('\n', '')
    dictionary[fio] = hobby.replace('\n', '') if hobby else None

with open('result.txt', 'w+', encoding='utf-8') as result:
    json.dump(dictionary, result)

with open('result.txt', 'r+', encoding='utf-8') as result:
    print(json.load(result))
