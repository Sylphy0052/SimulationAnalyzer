
# adjust/distance/duplication
def dict_to_adjust_plot_data(data_dict):
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
                y.append(data.rtt_data.mean)
            Y.append(y)

    return X, Y, labels
