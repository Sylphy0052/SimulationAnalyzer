from src.formatter import dict_to_adjust_plot_data

def classify_by_adjust(data_dict):
    return_arr = {}
    for data in data_dict.values():
        adjust = data.dat_data.adjust_num
        if not adjust in return_arr.keys():
            return_arr[adjust] = []
        return_arr[adjust].append(data)

    return dict_to_adjust_plot_data(return_arr)

def classify_by_distance():
    pass
