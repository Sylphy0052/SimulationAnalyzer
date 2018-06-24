from src.formatter import dict_to_adjust_plot_data

def classify_by_adjust(data_dict):
    return_dict = {}
    for data in data_dict.values():
        adjust = data.dat_data.adjust_num
        if not adjust in return_dict.keys():
            return_dict[adjust] = []
        return_dict[adjust].append(data)

    return dict_to_adjust_plot_data(return_dict)

def classify_by_duplication_for_plot_data(datas):
    return_dict = {}
    for data in datas:
        duplication = data.dat_data.duplication
        if not duplication in return_dict.keys():
            return_dict[duplication] = []
        return_dict[duplication].append(data)

    return return_dict
