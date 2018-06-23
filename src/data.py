from enum import Enum

# Passive or Active
class MoleculeType(Enum):
    PASSIVE = 1
    ACTIVE = 2

# データを格納するクラス
class Data:
    def __init__(self):
        self.rtt_data = None
        self.adjust_data = None
        self.collision_data = None
        self.retransmission_data = None

    def is_rtt(self):
        if self.rtt_data is None:
            return False
        else:
            return True

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
adjust: True(数) or False(0)
is_fec: True or False
fecRequirePacket:必要数
fecRate:レート
packetStepLength: 1stepで移動する距離
packetDiameter: 分子の半径
outputFile: 出力ファイル名
"""
class DatData:
    def __init__(self, file_name):
        self.dat_file_name = file_name

class RTTData:
    def __init__(self):
        pass

class AdjustData:
    def __init__(self):
        pass

class CollisionData:
    def __init__(self):
        pass

class RetransmissionData:
    def __init__(self):
        pass
