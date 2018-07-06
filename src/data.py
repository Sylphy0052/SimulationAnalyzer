from enum import Enum
import pandas as pd
import sys

# Passive or Active
class MoleculeType(Enum):
    PASSIVE = 1
    ACTIVE = 2

# データを格納するクラス
class Data:
    def __init__(self):
        self.dat_data = None
        self.rtt_data = None
        self.adjust_data = None
        self.collision_data = None
        self.retransmission_data = None

    def get_value(self, target_type):
        from src.draw_graph import Target, Parameter
        # Target
        # if type(target_type) is Target:
        if self.rtt_data is None:
            from src.parser import parse_rtt
            fname = "./result/batch_" + self.dat_data.output_file_name
            self.rtt_data = parse_rtt(fname)

        if isinstance(target_type, Target):
            if target_type is Target.Mean:
                return self.rtt_data.mean
            elif target_type is Target.Median:
                return self.rtt_data.median
            elif target_type is Target.Jitter:
                return self.rtt_data.std
            elif target_type is Target.CollisionNum:
                if self.collision_data is None:
                    from src.parser import parse_coll
                    fname = "./result/collision_batch_" + self.dat_data.output_file_name
                    self.collision_data = parse_coll(fname)
                return self.collision_data.collision_num
            elif target_type is Target.DecomposingNum:
                if self.collision_data is None:
                    from src.parser import parse_coll
                    fname = "./result/collision_batch_" + self.dat_data.output_file_name
                    self.collision_data = parse_coll(fname)
                return self.collision_data.decomposing_num

        # Parameter
        elif isinstance(target_type, Parameter):
            if target_type is Parameter.Distance:
                return self.dat_data.distance
            elif target_type is Parameter.Duplication:
                return self.dat_data.duplication
            elif target_type is Parameter.AdjustNum:
                return self.dat_data.adjust_num
            elif target_type is Parameter.MessageNum:
                return self.dat_data.message_num
            elif target_type is Parameter.Decomposing:
                return self.dat_data.decomposing
            else:
                print("isinstance in data not defined {}...".format(target_type.name))
                sys.exit(1)

    def get_column(self):
        return ["File Name", "Mean", "Median", "Var", "Std", "Min", "Max"]

    def to_array(self):
        if self.rtt_data is None:
            from src.parser import parse_rtt
            self.rtt_data = parse_rtt("./result/batch_" + self.dat_data.output_file_name)
        fname = self.dat_data.dat_file_name.split('/')[1]
        mean = self.rtt_data.mean
        median = self.rtt_data.median
        var = self.rtt_data.var
        std = self.rtt_data.std
        minimum = self.rtt_data.minimum
        maximum = self.rtt_data.maximum
        return [fname, mean, median, var, std, minimum, maximum]


## Parameter ##
"""
# 環境
distance: 距離
duplication: 複製数
message_num: メッセージ数
rto: retransmitWaitTime(タイムアウト待ち時間)

# 分子
step_length: 1stepで移動する距離
diameter: 分子の半径

# オプション
molecule_type: PASSIVE or ACTIVE
decomposing: 0 ~ 3
adjust_num: True(数) or False(0)
is_fec: True or False
fecRequirePacket:必要数
fecRate:レート
packetStepLength: 1stepで移動する距離
packetDiameter: 分子の半径
outputFile: 出力ファイル名
"""
class DatData:
    def __init__(self, fname):
        self.dat_file_name = fname

"""
rtt: 全ての結果を格納
mean: 平均
median: 中央値
var: 分散
std: 標準偏差
num: シミュレーション回数
minimum: 最小値
maximum: 最大値
"""
class RTTData:
    def __init__(self):
        self.rtt = []

    def create_plot_data(self):
        X = [0]
        Y1 = [0]
        Y2 = [0]
        count = 0
        prob = 0.0
        cum_prob = 0.0

        plot_range = self.maximum / 100.0
        head = 0
        tail= plot_range

        index = 0

        while(index < len(self.rtt)):
            # 範囲内の時
            if self.rtt[index] < tail:
                count += 1
            # 範囲外になったら
            else:
                prob = float(count) / len(self.rtt) * 100
                cum_prob += prob
                X.append(tail)
                Y1.append(prob)
                Y2.append(cum_prob)
                count = 0
                head += plot_range
                tail += plot_range
            index += 1

        return X, Y1, Y2

class AdjustData:
    def __init__(self):
        pass

"""
collision_num: 衝突回数
"""
class CollisionData:
    def __init__(self):
        pass

class RetransmissionData:
    def __init__(self):
        pass
