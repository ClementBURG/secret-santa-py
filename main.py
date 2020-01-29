import os
import sys
from random import choice


DEFAULT_OUTPUT_PATHNAME = './output_files/result.txt'


def display_help():
    print('Usage: {} <path_to_input_file> [<path_to_output_file>]'.format(os.path.basename(__file__)))


def file_to_list(pathname):
    line_list = None

    try:
        line_list = [line.rstrip('\n') for line in open(pathname, mode='r', encoding='utf-8')]
    except Exception as e:
        print(e)
    return line_list


def pair_names(name_list):
    to_list = name_list.copy()
    result_list = []

    for name in name_list:
        to = choice([x for x in to_list if x != name])
        result_list.append('{} -> {}'.format(name, to))
        to_list.remove(to)
    return result_list


def list_to_file(pathname, input_list):
    if not os.path.exists(os.path.dirname(pathname)):
        os.makedirs(os.path.dirname(pathname))

    try:
        with open(pathname, mode='w+', encoding='utf-8') as f:
            for item in input_list:
                f.write('{}\n'.format(item))
            f.close()
    except Exception as e:
        print(e)


def main(argv):
    input_pathname = None
    output_pathname = None

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        display_help()
        return

    if len(sys.argv) >= 2:
        input_pathname = argv[1]

    if len(sys.argv) == 3:
        output_pathname = argv[2]
    else:
        output_pathname = DEFAULT_OUTPUT_PATHNAME
    name_list = file_to_list(input_pathname)
    result_list = pair_names(name_list)
    list_to_file(output_pathname, result_list)


if __name__ == "__main__":
    main(sys.argv)
