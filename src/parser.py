from src.data import DatData, MoleculeType
from src.common import split_complex_string
import sys
# ファイルを読み込む関数

# dat fileを解析する
def parse_dat(file_name):
    dat_data = DatData(file_name)
    with open(file_name, 'r') as f:
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
