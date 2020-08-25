#!/usr/bin/env python3
import os


def gen_row(show_name: str, show_path: str, level: int):
    return "{}* [{}]({})\n".format("  " * level, show_name, show_path)


def get_file_title(file_path):
    if not os.path.exists(file_path):
        raise Exception('{}: not found the file！'.format(file_path))
    with open(file_path) as fd:
        for line in fd:
            line = line.strip('#').strip()
            if line:
                show_name = line
                break
    if os.path.isfile(file_path):
        dir_name = file_path.split('/')[-2]
        file_name = file_path.split('/')[-1]
        if file_name.startswith('p') and str.isdigit(file_name[1]):
            chapter_num = int(''.join(filter(str.isdigit, dir_name)))
            file_idx = int(''.join(filter(str.isdigit, file_name.split('_', 1)[0])))
            show_name = '{}.{} '.format(chapter_num, file_idx) + show_name
        return show_name


def list_files(path, level):
    ls_dir = sorted(os.listdir(path))
    dirs = [i for i in ls_dir if os.path.isdir(os.path.join(path, i))]
    files = [i for i in ls_dir if os.path.isfile(os.path.join(path, i))]
    for d in dirs:
        if d in ['.git', '.idea', 'venv']:
            continue
        d_path = os.path.join(path, d)
        d_path_readme = os.path.join(d_path, 'README.md')
        show_name = get_file_title(d_path_readme)
        show_path = d_path.split('/', 1)[-1] + '/'
        print(gen_row(show_name, show_path, level), end='')
        list_files(os.path.join(path, d), level + 1)
    for f in files:
        if f.startswith('.') or f.startswith('_'):
            continue
        if f == 'readme.md' or f == 'README.md':
            continue
        if not f.endswith('.md'):
            continue
        f_path = os.path.join(path, f)
        show_name = get_file_title(f_path)
        show_path = f_path.split('/', 1)[-1]
        print(gen_row(show_name, show_path, level), end='')


def main():
    list_files('.', 0)
    # for name in list_files('.', 0):
    #     print(name)


if __name__ == '__main__':
    main()
