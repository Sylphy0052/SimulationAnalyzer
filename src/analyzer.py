# データをなんやかんやするクラス
from src.common import get_file_list
from src.parser import parse_config

class Analyzer:
    def __init__(self):
        self.all_file_list = get_file_list()
        self.parse_dat_file()

    def parse_dat_file(self):
        config_dict = {}

        count = 0
        for file_name in self.all_file_list:
            count += 1
            print("{}/{} Reading... {}".format(count, len(self.all_file_list), file_name))
            config_dict[file_name] = parse_config(file_name)
