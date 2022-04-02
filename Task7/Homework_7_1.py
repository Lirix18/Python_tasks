import os
import yaml


folders = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
with open('./first_config.yaml', 'w') as w_file:
    yaml.dump(folders, w_file)

with open('./first_config.yaml', 'r') as r_file:
    data = yaml.safe_load(r_file)

for root, folders in data.items():
    if not os.path.exists(root):
        for folder in folders:
            direct = os.path.join(root, folder)
            os.makedirs(direct)


#    '''Решение в лоб'''
# path = os.getcwd()
# project = 'my_project'
# folders = ['settings', 'mainapp', 'adminapp', 'authapp']
# '''Проверяем наличие папки и создаем'''
# def create_folder(path):
#     if not os.path.exists(path):
#         os.mkdir(path)
#
# '''Создаем основную папку'''
# end_path = os.path.join(path, project_name)
# create_folder(end_path)
#
# '''Создаем вложенные папки'''
# for f in folders:
#     folder = os.path.join(end_path, f)
#     create_folder(folder)
