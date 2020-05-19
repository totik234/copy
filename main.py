import os
import shutil
import time
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        prog="Копирование фйлов с ротацией по дням.",
        description="Копирует файлы из одной папки в другую.",
        epilog="(c) Май 2020 Автор Шульц Денис.",
        add_help=False
    )

    parent_group = parser.add_argument_group(title="Параметры")
    parent_group.add_argument("-h", "--help", action="help", help="Справка")

    parent_group.add_argument("-src", "--src-path", required=True, help="Путь из которого будем копировать")
    parent_group.add_argument("-dst", "--dst-path", required=True, help="Путь куда будем копировать")
    parent_group.add_argument("-m", "--mask", required=True, help="Маска файлов. Например '.bak'")
    parent_group.add_argument("-d", "--days", type=int, default=30, help="Количество дней. По умолчанию 30")

    return parser


def copy_files(src_path, dst_path, mask, days):
    files = os.listdir(src_path)
    files_list = filter(lambda x: x.endswith(mask), files)
    for file in files_list:
        now_time = time.time()
        file_time = os.path.getctime(os.path.join(src_path, file))
        delta_time = (now_time - file_time) // 3600 // 24
        # print(delta_time)
        if delta_time > days:
            shutil.copyfile(os.path.join(src_path, file), os.path.join(dst_path, file))
            print(f"delta = {delta_time}, {file} скопирован!")


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    copy_files(namespace.src_path, namespace.dst_path, namespace.mask, namespace.days)
