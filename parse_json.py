import json
import os
import shutil

from params import labels


def create_dir(dir_name):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.makedirs(dir_name)


def parse_bundle(bundle_type):
    bundle_path = os.path.join(os.getcwd(), f'{bundle_type}_bundle')
    create_dir(bundle_path)
    for label in labels:
        create_dir(os.path.join(bundle_path, label))

    for item in data[f'{bundle_type}_bundle']:
        file_path = item['file']
        file_name = file_path.split('/')[1]
        if item['subcategory'] is not None and item['subcategory']['name'] == 'Cars':
            # only looking for cars, not all the vehicles
            label = 'Cars'
        elif item['category'] is not None and item['category']['name'] == 'Plants':
            # looking for all the plants
            label = 'Plants'
        else:
            label = 'Stuff'
        destination_path = os.path.join(bundle_path, label, file_name)
        shutil.copy2(file_path, destination_path)


if __name__ == '__main__':
    with open('data.json', 'r') as f:
        data = json.load(f)
    parse_bundle('initial')
    parse_bundle('test')
