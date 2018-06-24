from src.draw_graph import Target

def get_value(data, target_type):
    if target_type is Target.Mean:
        return data.rtt_data.mean
    elif target_type is Target.Median:
        return data.rtt_data.median
    elif target_type is Target.Jitter:
        return data.rtt_data.std

def dict_to_adjust_plot_data(data_dict, target_type):
    X = []
    Y = []
    labels = []

    from src.classify import classify_by_duplication_for_plot_data
    for adjust, datas in data_dict.items():
        classify_dict = classify_by_duplication_for_plot_data(datas)
        for duplication, datas in classify_dict.items():
            label = "adjust {} duplication {}".format(adjust, duplication)
            labels.append(label)
            y = []
            for data in datas:
                x = data.dat_data.distance
                if not x in X:
                    X.append(x)
                y.append(get_value(data, target_type))
            Y.append(y)

    return X, Y, labels
