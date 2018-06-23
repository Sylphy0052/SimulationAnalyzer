# グラフを描く関数

def draw_rtt(data):
    # RTT fileを読み込んでなかったら
    if not data.is_rtt():
        fname = "./result/batch_" + data.dat_data.output_file_name
        print(fname)
