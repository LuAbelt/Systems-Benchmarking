import csv
import os

from data_analysis import jump_detection, trend_detection
from data_import import import_benchmark_data

import matplotlib.pyplot as plt
from signal_processing_algorithms.energy_statistics import energy_statistics
import numpy.random


def plot_release_data():
    release_res_dir = "../../release_benchmark/lz4hc/results"
    release_list_file = "../../benchmark/lz4releases"

    compression_speed, decompression_speed, labels = import_benchmark_data(release_list_file,release_res_dir,)

    plt.xticks(rotation=90)
    sorted_labels = sorted(labels)

    for compressor in compression_speed:
        #Only temporary to only show lz4hc
        #compressor = "lz4hc 1.9.2 -1"

        comp_data_series = compression_speed[compressor]
        comp_data_series.sort(key=dict(zip(comp_data_series, labels)).get)
        plt.plot(sorted_labels, comp_data_series, label=f"Compression speed (lz4hc)")

        decomp_data_series = decompression_speed[compressor]
        decomp_data_series.sort(key=dict(zip(decomp_data_series, labels)).get)
        plt.plot(sorted_labels, decomp_data_series, label=f"Decompression speed (lz4hc)",color="orange")
        #break

    plt.ylabel('MB/s')
    plt.xlabel("Version")
    plt.ylim([0, 4000.0])
    plt.legend()
    plt.tight_layout()
    plt.show()
    #plt.savefig("out/lz4hc_release_decompression.png")


def plot_commit_data():
    commit_res_dir = "../../commit_benchmark/lz4hc/results"
    commit_hash_file = "../../benchmark/lz4commits"

    comp_dict, decomp_dict, labels = import_benchmark_data(commit_hash_file,commit_res_dir)
    print(decomp_dict)
    compression_speed = comp_dict["lz4 1.9.2"]
    decompression_speed = decomp_dict["lz4 1.9.2"]

    decompression_speed.reverse()
    compression_speed.reverse()
    #plt.plot(compression_speed, label="Compression Speed (lz4hc)")
    plt.plot(decompression_speed, label="Decompression Speed", color="orange")
    plt.ylabel('MB/s')
    plt.xlabel("# of commits since v1.8.1")
    plt.ylim([0,4000])
    plt.legend(loc=9)

    # Calculate change points based on created data
    # comp_cp = energy_statistics.e_divisive(compression_speed, pvalue=0.1, permutations=100)
    # decomp_cp = energy_statistics.e_divisive(decompression_speed, pvalue=0.1, permutations=100)

    # print(comp_cp)
    # print(decomp_cp)
    #
    # for cp in comp_cp:
    #     plt.vlines(x=cp,color="r",lw=0.5,ls=":",ymin=250,ymax=750)

    # plt.scatter(comp_cp,[compression_speed[cp] for cp in comp_cp],marker='.',c='r')
    # plt.scatter(decomp_cp,[decompression_speed[cp] for cp in decomp_cp],marker='.',c='r')

    # for cp in decomp_cp:
    #     plt.vlines(x=cp,color="g",lw=0.5, ls=":",ymax=max(decompression_speed),ymin=min(decompression_speed))
    plt.tight_layout()
    labels.reverse()
    # print(labels[decompression_speed.index(max(decompression_speed))])
    # plt.show()

    plt.savefig("out/lz_commits_decompression")


def plot_commits_with_cp():
    plt.figure(dpi=600)
    commit_res_dir = "../../commit_benchmark/lz4hc_180_181/results"
    commit_hash_file = "../../benchmark/lz4hc_commits"

    comp_dict, decomp_dict, labels = import_benchmark_data(commit_hash_file, commit_res_dir)
    print(decomp_dict)
    compression_speed = comp_dict["lz4hc 1.9.2 -1"]
    decompression_speed = decomp_dict["lz4hc 1.9.2 -1"]

    decompression_speed.reverse()
    compression_speed.reverse()
    plt.plot(compression_speed, label="Compression Speed (lz4hc)")
    # plt.plot(decompression_speed, label="Decompression Speed", color="orange")

    plt.ylabel('MB/s')
    plt.xlabel("# of commits since v1.8.0")
    # plt.ylim([0, 4000])
    plt.ylim([0, 150])
    plt.legend(loc=9)

    # Calculate change points based on created data
    comp_cp = energy_statistics.e_divisive(compression_speed, pvalue=0.1, permutations=100)
    decomp_cp = energy_statistics.e_divisive(decompression_speed, pvalue=0.1, permutations=100)

    decompression_jd = jump_detection(decompression_speed)
    decompression_td = trend_detection(decompression_speed,10,0.05)

    compression_jd = jump_detection(compression_speed)
    compression_td = trend_detection(compression_speed,10,0.05)

    # for cp in comp_cp:
    #     plt.vlines(x=cp,color="r",lw=0.5,ls=":",ymin=250,ymax=750)

    # for cp in decomp_cp:
    #     plt.vlines(x=cp,color="g",lw=0.5,ymax=max(decompression_speed),ymin=min(decompression_speed))

    for cp in comp_cp:
        plt.vlines(x=cp,color="g",lw=0.5,ymax=max(compression_speed),ymin=min(compression_speed))

    # for jp in decompression_jd:
    #     plt.vlines(x=jp, color="r", lw=0.5, ymax=max(decompression_speed), ymin=min(decompression_speed))

    # for jp in compression_jd:
    #     plt.vlines(x=jp, color="r", lw=0.5, ymax=max(compression_speed), ymin=min(compression_speed))

    # for tp in decompression_td:
    #     plt.vlines(x=tp, color="b", lw=0.5, ymax=max(decompression_speed), ymin=min(decompression_speed))

    # for tp in compression_td:
    #     plt.vlines(x=tp, color="b", lw=0.5, ymax=max(compression_speed), ymin=min(compression_speed))

    # print(len(decomp_cp))
    # print(len(decompression_jd))
    # print(len(decompression_td))

    print(comp_cp)
    print(len(compression_jd))
    print(len(compression_td))

    plt.tight_layout()
    labels.reverse()
    # plt.show()

    plt.savefig("out/lz4hc_commit_e-divisive.png")


def create_outlier():
    numbers = numpy.random.uniform(0.95,1.05,200)
    numbers = numpy.append(numbers, numpy.random.uniform(1.8,2.1,3))
    numbers = numpy.append(numbers, numpy.random.uniform(0.95,1.05,200))
    numbers += 1
    plt.plot(numbers)
    plt.ylim(0,4)
    plt.savefig("out/outlier.png")


def create_changepoint():
    numbers = numpy.random.uniform(0.95, 1.05, 200)
    numbers = numpy.append(numbers, numpy.random.uniform(1.9,2.1,200))
    numbers += .5
    plt.plot(numbers)
    plt.ylim(0, 4)
    plt.savefig("out/changepoint.png")