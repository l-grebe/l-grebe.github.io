#!/usr/bin/env python3
import os

"""
自动在生成项目根目录下._sidebar.md文件脚本
"""


class GenSideBar:

    def __init__(self, dst_file):
        self.dst_file = dst_file

    @staticmethod
    def gen_row(name: str, path: str, level: int):
        name = name.replace("`", "")
        return f'{level * "  "}* [{name}]({path})\n'

    @staticmethod
    def gen_row_name(path):

        if not os.path.exists(path):
            raise Exception('{}: not found the file or dir！'.format(path))

        with open(path) as fd:
            for line in fd:
                line = line.strip('#').strip()
                if line:
                    show_name = line
                    break

        if os.path.isfile(path):
            dir_name = os.path.basename(os.path.dirname(path))
            file_name = os.path.basename(path)
            if file_name.startswith('p') and str.isdigit(file_name[1]):
                chapter_num = int(''.join(filter(str.isdigit, dir_name)))
                file_idx = int(''.join(filter(str.isdigit, file_name.split('_', 1)[0])))
                show_name = f'{chapter_num}.{file_idx} ' + show_name
            return show_name

    def list_files(self, path: str, level: int):
        res = sorted(os.listdir(path))

        dirs = [i for i in res if os.path.isdir(os.path.join(path, i))]
        for d in dirs:
            if d in ['.git', '.idea', 'venv', 'static', 'image']:
                continue
            d_path = os.path.join(path, d)
            d_path_readme = os.path.join(d_path, 'README.md')
            row_name = self.gen_row_name(d_path_readme)
            row_path = os.path.basename(d_path) + '/'
            yield self.gen_row(row_name, row_path, level)
            for one in self.list_files(os.path.join(path, d), level + 1):
                yield one

        files = [i for i in res if os.path.isfile(os.path.join(path, i))]
        for f in files:
            if f.startswith('.') or f.startswith('_'):
                continue
            if f in ("readme.md", "README.md"):
                continue
            if not f.endswith('.md'):
                continue
            f_path = os.path.join(path, f)
            row_name = self.gen_row_name(f_path)
            row_path = f_path.split('/', 1)[-1]
            yield self.gen_row(row_name, row_path, level)

    def generator(self):
        with open(self.dst_file, 'w') as fd:
            for row in self.list_files('.', 0):
                fd.write(row)


if __name__ == '__main__':
    GenSideBar("_sidebar.md").generator()
