import os
import yaml

with open('./config.yaml', 'r') as file:
    data_in_file = yaml.safe_load(file)


def create(data):
    for folder, data_items in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for d in data_items:
            if isinstance(d, dict):
                create(d)
            else:
                if not os.path.exists(d):
                    if '.' in d:
                        with open(d, 'w') as w_file:
                            w_file.write('')
    else:
        os.chdir('../')

if __name__ == 'main':
    create(data_in_file)
