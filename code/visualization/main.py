import csv
import os

import matplotlib.pyplot as plt
from signal_processing_algorithms.energy_statistics import energy_statistics
import numpy.random


def plot_release_data():
    release_res_dir = "../../release_benchmark/lz4hc/results"
    labels = []
    compression_speed = dict()
    decompression_speed = dict()

    for filename in os.listdir(release_res_dir):
        if filename.endswith(".timings"):
            continue
        with open(os.path.join(release_res_dir, filename)) as res_file:
            labels.append(filename.strip(".res"))
            reader = csv.reader(res_file)
            # Skip headers and memcpy line
            next(reader)
            next(reader)
            for line in reader:
                try:
                    compression_speed[line[0]].append(float(line[1]))
                    decompression_speed[line[0]].append(float(line[2]))
                except KeyError:
                    compression_speed[line[0]] = [float(line[1])]
                    decompression_speed[line[0]] = [float(line[2])]

    plt.xticks(rotation=90)
    sorted_labels = sorted(labels)

    for compressor in compression_speed:
        comp_data_series = compression_speed[compressor]
        comp_data_series.sort(key=dict(zip(comp_data_series, labels)).get)
        plt.plot(sorted_labels, comp_data_series, label=f"Compression speed {compressor}")

        # decomp_data_series = decompression_speed[compressor]
        # decomp_data_series.sort(key=dict(zip(decomp_data_series, labels)).get)
        # plt.plot(labels, decomp_data_series, label=f"Decompression speed {compressor}")

    plt.ylabel('MB/s')
    plt.xlabel("Version")
    plt.ylim([0, 150.0])
    plt.legend()
    plt.tight_layout()
    #plt.show()
    plt.savefig("test.png")


def plot_commit_data():
    commit_res_dir = "../../commit_benchmark/mintime/results/"
    commit_hash_file = "../../benchmark/merge_commits"
    compression_speed = []
    decompression_speed = []
    labels = []

    with open(commit_hash_file) as hash_file:
        for commit_hash in hash_file:
            if not os.path.isfile(os.path.join(commit_res_dir,commit_hash.strip()+".res")):
                continue
            with open(os.path.join(commit_res_dir,commit_hash.strip()+".res")) as commit_file:
                reader = csv.reader(commit_file)
                labels.append(commit_hash)
                next(reader)
                next(reader)
                line = next(reader)
                compression_speed.append(float(line[1]))
                decompression_speed.append(float(line[2]))
            #print(commit_hash.strip()+".res")

        decompression_speed.reverse()
        compression_speed.reverse()
        plt.plot(compression_speed, label="Compression Speed")
        plt.plot(decompression_speed, label="Decompression Speed")
        plt.ylabel('MB/s')
        plt.xlabel("# of commits since v1.8.1")
        plt.ylim([0,4000])
        plt.legend(loc=9)

        # Calculate change points based on created data
        comp_cp = energy_statistics.e_divisive(compression_speed, pvalue=0.1, permutations=100)
        decomp_cp = energy_statistics.e_divisive(decompression_speed, pvalue=0.1, permutations=100)

        print(comp_cp)
        print(decomp_cp)

        for cp in comp_cp:
            plt.vlines(x=cp,color="r",lw=0.5,ls=":",ymin=250,ymax=750)

        # plt.scatter(comp_cp,[compression_speed[cp] for cp in comp_cp],marker='.',c='r')
        # plt.scatter(decomp_cp,[decompression_speed[cp] for cp in decomp_cp],marker='.',c='r')

        for cp in decomp_cp:
            plt.vlines(x=cp,color="g",lw=0.5, ls=":",ymax=max(decompression_speed),ymin=min(decompression_speed))
        plt.tight_layout()
        labels.reverse()
        print(labels[decompression_speed.index(max(decompression_speed))])
        plt.show()


def create_outlier():
    numbers = numpy.random.uniform(0.95,1.05,200)
    numbers = numpy.append(numbers, numpy.random.uniform(1.8,2.1,3))
    numbers = numpy.append(numbers, numpy.random.uniform(0.95,1.05,200))
    numbers += 1
    plt.plot(numbers)
    plt.ylim(0,4)
    plt.savefig("outlier.png")


def create_changepoint():
    numbers = numpy.random.uniform(0.95, 1.05, 200)
    numbers = numpy.append(numbers, numpy.random.uniform(1.9,2.1,200))
    numbers += .5
    plt.plot(numbers)
    plt.ylim(0, 4)
    plt.savefig("changepoint.png")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plot_release_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
