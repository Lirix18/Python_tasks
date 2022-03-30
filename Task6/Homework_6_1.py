def parsing_nginx():
    with open('./nginx_logs.txt', 'r', encoding='utf-8') as file:
        for line in file:
            ip = line.split(' - - ')[0]
            response_path = line.split('"')[1]
            response = response_path.split()[0]
            path = response_path.split()[1]
            yield ip, response, path


print(next(parsing_nginx()))
print(next(parsing_nginx()))



