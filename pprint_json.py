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
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return True


def check_json(file_name):
    if file_name.endswith('.json'):
        return True
    return False


def load_data(filepath):
    market_list = json.load(filepath)
    for info_from_one_market in market_list:
        pretty_print_json(info_from_one_market)


def pretty_print_json(data):
    print(json.dumps(data, skipkeys=True, ensure_ascii=False,
          sort_keys=True, indent=4))


if __name__ == '__main__':
    file_name = input_file_name()
    if check_json(file_name) is False:
        print("Формат файла должен быть .json")
    elif file_exists(file_name) is None:
        print("Ошибка открытия файла")
    else:
        load_data(open(file_name, 'r'))
