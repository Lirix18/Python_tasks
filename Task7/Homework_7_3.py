import os
import yaml
import shutil
from Homework_7_2 import create

with open('./config.yaml', 'r') as file:
    data_in_file = yaml.safe_load(file)

create(data_in_file)


def search_html(root):
    """ Делала по примеру преподавателя, но доработала,
        новая папка внутри проекта и добавила исключения.
        Постаралась разобраться, но пока рука не набита. """
    os.chdir(root)
    new_dir = 'templates'
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    new_files = []
    for roots, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if '.html' in file:
                new_files.append(os.path.join(roots, file))

    for path in new_files:
        folder = os.path.join(new_dir, os.path.basename(os.path.dirname(path)))
        if not os.path.exists(folder):
            os.mkdir(folder)
        result_path = os.path.join(folder, os.path.basename(path))
        """ Ловим ошибку одинаковых файлов """
        try:
            shutil.copy(path, result_path)
        except shutil.SameFileError as e:
            print(f'Ошибка: {e}')

if __name__ == '__main__':
    search_html('my_project')
