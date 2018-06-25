from src.draw_graph import Target

def dict_to_plot_data(data_dict, x_param, target_type, label_params):
    X = []
    Y = []
    labels = []

    for key, datas in data_dict.items():
        label = "{} {}".format(label_params[0].name, key)
        if isinstance(datas, dict):
            for k, vs in datas.items():
                tmp_label = label
                tmp_label += " - {} {}".format(label_params[1].name, k)
                y = []
                for v in vs:
                    x = v.get_value(x_param)
                    if not x in X:
                        X.append(x)
                    y.append(v.get_value(target_type))
                Y.append(y)
                labels.append(tmp_label)
        else:
            y = []
            for data in datas:
                x = data.get_value(x_param)
                if not x in X:
                    X.append(x)
                y.append(v.get_value(target_type))
            Y.append(y)
            labels.append(label)

    return X, Y, labels
