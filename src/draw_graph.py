from src.parser import parse_rtt
import matplotlib.pyplot as plt
from matplotlib import ticker
import os
from enum import Enum

# グラフを描く関数

COLOR_LIST = ['r', 'g', 'b', 'm', 'c', 'y', 'k', 'r', 'g', 'b', 'm', 'c', 'y', 'k']
STYLE_LIST = ['-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--', '-.', ':', '-', '--', '-.', ':']

def Target(Enum):
    Mean = 1
    Median = 2
    Std = 3

def draw_rtt(data):
    # RTT fileを読み込んでなかったら
    if not data.is_rtt():
        fname = "./result/batch_" + data.dat_data.output_file_name
        data.rtt_data = parse_rtt(fname)

    dir_path = "./rtt_fig/"
    if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
    fig_name = dir_path + data.dat_data.output_file_name + ".png"
    print("Draw {} in {}".format(fig_name.split('/')[2], dir_path.split('/')[1]))

    X, Y1, Y2 = data.rtt_data.create_plot_data()

    fig, ax1 = plt.subplots()
    ln1 = ax1.plot(X, Y1, color=COLOR_LIST[0], label="Probability", linestyle=STYLE_LIST[0])
    ax2 = ax1.twinx()
    ln2 = ax2.plot(X, Y2, color=COLOR_LIST[1], label="Cumulative Probability", linestyle=STYLE_LIST[1])

    ax1.set_xlabel("RTT (s)")
    ax1.set_ylabel("Probability of RTT")
    ax2.set_ylabel("Cumulative Probability of RTT")

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc="right")

    plt.grid(True)

    plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
    plt.gca().ticklabel_format(style="sci",  axis="x",scilimits=(0,0))

    plt.savefig(fig_name, dpi=90, bbox_inches="tight", pad_inches=0.0)
    plt.close('all')

def draw_two_line_graph(X, Y1, Y2, labels, location, fig_name):
    fig, ax1 = plt.subplots()
    ln1 = ax1.plot(X, Y1, color=COLOR_LIST[0], label=ax1_label)
    ax2 = ax1.twinx()
    ln2 = ax2.plot(X, Y2, color=COLOR_LIST[1], label=ax2_label, linestyle=STYLE_LIST[0])

    ax1.set_xlabel(X_label)
    ax1.set_ylabel(Y1_label)
    ax2.set_ylabel(Y2_label)

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc=location)

    plt.grid(True)

    if max(X) > 10 ** 6:
        plt.gca().xaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        plt.gca().ticklabel_format(style="sci",  axis="x",scilimits=(0,0))
    if max(Y1) > 10 ** 6:
        ax1.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        ax1.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))
    if max(Y2) > 10 ** 6:
        ax2.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
        ax2.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))

    plt.savefig(fig_name, dpi=90, bbox_inches="tight", pad_inches=0.0)
    plt.close('all')
