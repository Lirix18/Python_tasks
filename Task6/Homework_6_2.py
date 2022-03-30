def parsing_nginx():
    with open('./nginx_logs.txt', 'r', encoding='utf-8') as file:
        for line in file:
            ip = line.split(' - - ')[0]
            response_path = line.split('"')[1]
            response = response_path.split()[0]
            path = response_path.split()[1]
            yield ip, response, path


# print(next(parsing_nginx()))
# print(next(parsing_nginx()))


def spamer():
    db = {}

    for log in parsing_nginx():
        db[log[0]] = db.get(log[0], 0) + 1

    return max(db.items(), key=lambda count: count[1])


print(f'ip spamer: {spamer()[0]}, count: {spamer()[1]}')
