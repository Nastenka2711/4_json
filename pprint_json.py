import json
import sys
import os


def load_data(filepath):
    list_info_alcos = json.load(filepath)
    for list_info_alco in list_info_alcos:
        pretty_print_json(list_info_alco)


def pretty_print_json(data):
    print(json.dumps(data, skipkeys=True, ensure_ascii=False,
          sort_keys=True, indent=4))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        name_file = input("Введите название файла  ")
    else:
        name_file = sys.argv[1]
    if os.path.exists(name_file) and os.path.isfile(name_file):
        load_data(open(name_file, 'r'))
    else:
        print("Ошибка открытия файла")
