import sys
from itertools import zip_longest


def reader(users_path, hobby_path):
    with open(users_path, 'r', encoding='utf-8') as file_users, open(hobby_path, 'r', encoding='utf-8') as file_hobby:
        for user, hobby in zip_longest(file_users, file_hobby):
            yield (user.removesuffix('\n'), hobby.removesuffix('\n')) if hobby else None


def resulting(result_path, users_path, hobby_path):
    with open(result_path, 'w', encoding='utf-8') as file_result:
        for i in reader(users_path, hobby_path):
            print(f'{i[0]}: {i[1]}', file=file_result)


if __name__ == "__main__":

    users_name = ""
    hobby_name = ""
    result_name = ""

    if len(sys.argv[1:]) >= 3:
        user_name = sys.argv[1]
        hobby_name = sys.argv[2]
        output_name = sys.argv[3]

    if not users_name:
        users_name = "./users.csv"

    if not hobby_name:
        hobby_name = "./hobby.csv"

    if not result_name:
        result_name = "./result.txt"

    exit(resulting(users_path=users_name, hobby_path=hobby_name, result_path=result_name))
