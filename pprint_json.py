import json


def load_data(filepath):
    list_info_alcos = json.load(filepath)
    for list_info_alco in list_info_alcos:
        pretty_print_json(list_info_alco)


def pretty_print_json(data):
    print(json.dumps(data, skipkeys = True, ensure_ascii = False, sort_keys = False, indent = 4))


if __name__ == '__main__':
    load_data(open('vodka.json','r'))
