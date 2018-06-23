# なんか使える関数の詰め合わせ
from natsort import natsorted
import glob

DAT_PATH = "dat/*.dat"

# datファイル一覧を取得する
# in:None, out:list
def get_file_list():
    return natsorted(glob.glob(DAT_PATH))
