from src.data import DatData, RTTData, MoleculeType
from src.common import split_complex_string
import sys, math
from statistics import mean, variance, stdev, median
import numpy as np

# ファイルを読み込む関数たち

# dat fileを解析する
def parse_dat(fname):
    dat_data = DatData(fname)
    with open(fname, 'r') as f:
        for line in f:
            if line == '\n' or line[0] == '*':
                continue
            key, value = line.split(' ', 1)
            # ここからkeyで場合分け
            # distance
            if key == "transmitter":
                # ["(" ")" "," " "]の4つで区切る
                distance = abs(int(split_complex_string(value)[0])) * 2
                dat_data.distance = distance

            # duplication
            elif key == "moleculeParams":
                values = value.split(' ')
                if values[1] == "INFO":
                    dat_data.duplication = int(values[0])
                    dat_data.molecule_type = MoleculeType(1) if values[2] == "PASSIVE" else MoleculeType(2)
                    dat_data.adjust_num = int(values[3])
                    dat_data.diameter = float(values[4])

            # message_num
            elif key == "numMessages":
                dat_data.message_num = int(value)

            # rto
            elif key == "retransmitWaitTime":
                dat_data.rto = int(value)

            # stepLength
            elif key == "stepLengthX":
                dat_data.step_length = float(value)

            # decomposing
            elif key == "decomposing":
                dat_data.decomposing = int(value)

            # fec
            elif key == "assembling":
                dat_data.is_fec = int(value)

            # outputFile
            elif key == "outputFile":
                dat_data.output_file_name = value.rstrip()

    return dat_data

# RTT file を解析する
def parse_rtt(fname):
    rtt_data = RTTData()
    with open(fname, 'r') as f:
        for line in f:
            rtt_data.rtt.append(int(line))
    rtt_data.rtt.sort()
    rtt_data.mean = mean(rtt_data.rtt)
    rtt_data.median = median(rtt_data.rtt)
    rtt_data.var = np.var(rtt_data.rtt)
    rtt_data.std = np.std(rtt_data.rtt)
    rtt_data.num = len(rtt_data.rtt)
    rtt_data.minimum = rtt_data.rtt[0]
    rtt_data.maximum = rtt_data.rtt[-1]

    return rtt_data
