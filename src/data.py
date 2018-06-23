# データを格納するクラス

class Data:
    def __init__(self):
        pass

## Parameter ##
"""
# 環境
distance: 距離
duplication: 複製数
message_num: メッセージ数
rto: retransmitWaitTime(タイムアウト待ち時間)

# 分子
stepLength: 1stepで移動する距離
diameter: 分子の半径

# オプション
molecule_type: PASSIVE or ACTIVE
decomposing: 0 ~ 3
adjust: True(数) or False(0)
fec: True or False
fecRequirePacket:必要数
fecRate:レート
packetStepLength: 1stepで移動する距離
packetDiameter: 分子の半径
outputFile: 出力ファイル名
"""
class ConfigData:
    def __init__(self):


class ResultData:
    def __init__(self):
        pass

class PlotData:
    def __init__(self):
        pass
