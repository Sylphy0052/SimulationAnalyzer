# ファイルを読み込む関数

def parse_config(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            print(line)
