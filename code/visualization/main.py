import csv
import os

import matplotlib.pyplot as plt


def plot_release_data():
    release_res_dir = "../../results/releases_benchmark/"
    labels = []
    compression_speed = []
    decompression_speed = []

    for filename in os.listdir(release_res_dir):
        with open(os.path.join(release_res_dir, filename)) as res_file:
            labels.append(filename.strip(".res"))
            reader = csv.reader(res_file)
            next(reader)
            next(reader)
            line = next(reader)
            compression_speed.append(float(line[1]))
            decompression_speed.append(float(line[2]))

    plt.plot(labels, compression_speed)
    plt.ylabel('MB/s')
    plt.xlabel("Version")
    plt.ylim([0, 600.0])
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("compression_plot.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plot_release_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
