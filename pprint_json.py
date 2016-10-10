import json
import sys
import os


def input_file_name():
    if len(sys.argv) == 1:
        file_name = input("Введите название файла  ")
    else:
        file_name = sys.argv[1]
    return file_name


def file_exists(filepath):
    return os.path.exists(filepath) and os.path.isfile(filepath)


def check_json(file_name):
    return file_name.endswith('.json')


def load_data(filepath):
    pretty_print_json(json.load(filepath))


def pretty_print_json(data):
    print(json.dumps(data, skipkeys=True, ensure_ascii=False,
          sort_keys=True, indent=4))


def open_file(file_name):
    with open(file_name, 'r') as file_data:
        load_data(file_data)


if __name__ == '__main__':
    file_name = input_file_name()
    if not check_json(file_name):
        print("Формат файла должен быть .json")
    elif not file_exists(file_name):
        print("Ошибка открытия файла")
    else:
        open_file(file_name)
