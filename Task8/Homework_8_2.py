import re

"""Файл очень большой, так что сократила его до 3к+ строк и последним вставила частный случай"""
def valid_log():
    with open('./nginx_logs.txt', 'r', encoding='utf-8') as r_file, open('./nginx_logs_validate.txt', 'w', encoding='utf-8') as w_file:
        for raw in r_file:
            validate = re.compile(r'(^\S+)[\s-]*\[(.*)\]\s*\"(\w*)\s*(/\S*)[^\"]+\"\s+(\d+)\s+(\d+)')
            if validate.match(raw):
                text = str(validate.findall(raw))+'\n'
                w_file.writelines(text)
            else:
                print(validate.findall(raw), 'Error')


valid_log()
