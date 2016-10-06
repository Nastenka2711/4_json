import json
import sys
import os


def input_name_file():
    if len(sys.argv) == 1:
        name_file = input("Введите название файла  ")
    else:
        name_file = sys.argv[1]
    return name_file


def existence_file(filepath):
    if os.path.exists(filepath) and os.path.isfile(filepath):
        return 0
    else:
        return None


def checking_json(name_file):
    end_name_file = os.path.splitext(name_file)
    if end_name_file[1] != '.json':
        return 1
    return 0


def load_data(filepath):
    list_info_alcos = json.load(filepath)
    for list_info_alco in list_info_alcos:
        pretty_print_json(list_info_alco)


def pretty_print_json(data):
    print(json.dumps(data, skipkeys=True, ensure_ascii=False,
          sort_keys=True, indent=4))


if __name__ == '__main__':
    name_file = input_name_file()
    if checking_json(name_file) == 1:
        print("Формат файла должен быть .json")
    elif existence_file(name_file) is None:
        print("Ошибка открытия файла")
    else:
        load_data(open(name_file, 'r'))
