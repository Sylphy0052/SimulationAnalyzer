# データをなんやかんやするクラス
from src.common import get_file_list
from src.parser import parse_dat
from src.draw_graph import draw_rtt
from src.data import Data
import sys

# Mainから生成される
class Analyzer:
    def __init__(self):
        self.data_dict = {}
        # ファイル一覧を取得
        self.all_file_list = get_file_list()
        # Dat fileを解析する
        self.parse_dat_file()

    def parse_dat_file(self):
        self.dat_dict = {}

        count = 0
        for file_name in self.all_file_list:
            count += 1
            print("{}/{} Reading... {}".format(count, len(self.all_file_list), file_name))
            data = Data()
            dat = parse_dat(file_name)
            self.dat_dict[file_name] = dat
            data.dat_data = dat
            self.data_dict[file_name] = data

    def draw_rtt_graph(self):
        for _, data in self.data_dict.items():
            draw_rtt(data)
