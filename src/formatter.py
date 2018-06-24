
# adjust/distance/duplication
def dict_to_adjust_plot_data(data_dict):
    X = []
    Y = [[] for i in range(len(data_dict.keys()))]
    labels = []

    for adjust, datas in data_dict.items():
        print("adjust {}".format(adjust))
        if adjust == 0:
            for data in datas:
                print(data.dat_data.distance)

        elif adjust == 1:
            for data in datas:
                print(data.dat_data.distance)

    return X, Y, labels
