# データをなんやかんやするクラス
from src.common import get_file_list
from src.parser import parse_dat
from src.draw_graph import draw_rtt, draw_many_line_graph, Target, Parameter
from src.data import Data
from src.classify import classify_dict
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

        # ディレクトリ作成
        dir_path = "./adjust_fig/"
        if not os.path.isdir(dir_path):
                os.makedirs(dir_path)

        # Mean
        fig_name = dir_path + "mean.png"
        X, Y, labels = classify_dict(self.data_dict, Parameter.Distance, Target.Mean, [Parameter.Duplication, Parameter.AdjustNum])
        location = "upper left"
        ax_labels = ["Tx Rx distance (um)", "Mean of RTT (s)"]
        draw_many_line_graph(X, Y, labels, ax_labels, location, fig_name)

        # Median
        fig_name = dir_path + "median.png"
        X, Y, labels = classify_dict(self.data_dict, Parameter.Distance, Target.Median, [Parameter.Duplication, Parameter.AdjustNum])
        location = "upper left"
        ax_labels = ["Tx Rx distance (um)", "Median of RTT (s)"]
        draw_many_line_graph(X, Y, labels, ax_labels, location, fig_name)

        # Jitter
        fig_name = dir_path + "jitter.png"
        X, Y, labels = classify_dict(self.data_dict, Parameter.Distance, Target.Jitter, [Parameter.Duplication, Parameter.AdjustNum])
        location = "upper left"
        ax_labels = ["Tx Rx distance (um)", "Jitter of RTT (s)"]
        draw_many_line_graph(X, Y, labels, ax_labels, location, fig_name)
