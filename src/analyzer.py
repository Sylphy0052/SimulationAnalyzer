# データをなんやかんやするクラス
from src.common import get_file_list
from src.parser import parse_dat
from src.draw_graph import draw_rtt, draw_two_line_graph
from src.data import Data
from src.classify import classify_by_adjust
import sys, os
import pandas as pd

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
        for fname in self.all_file_list:
            count += 1
            print("{}/{} Reading... {}".format(count, len(self.all_file_list), fname))
            data = Data()
            dat = parse_dat(fname)
            self.dat_dict[fname] = dat
            data.dat_data = dat
            self.data_dict[fname] = data

    # CSV fileに結果書き込み
    def write_info_csv(self):
        tmp_data = None
        csv_data = []
        for data in self.data_dict.values():
            csv_data.append(data.to_array())
            tmp_data = data
        df = pd.DataFrame(csv_data, columns=tmp_data.get_column())

        df.to_csv("result.csv")

    def draw_rtt_graph(self):
        for _, data in self.data_dict.items():
            draw_rtt(data)

    def draw_adjust_graph(self):
        # Mean Graph
        # X: distance or duplication
        # Y1: no adjust
        # Y2: adjust
        dir_path = "./adjust_fig/"
        if not os.path.isdir(dir_path):
                os.makedirs(dir_path)

        fig_name = dir_path + "mean.png"

        X, Y, labels = classify_by_adjust(self.data_dict)

        location = "upper right"
        sys.exit(1)

        draw_two_line_graph(X, Y1, Y2, labels, location, fig_name)
