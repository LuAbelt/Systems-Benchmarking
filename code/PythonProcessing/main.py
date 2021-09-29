from visualization import *
from data_import import *
from data_analysis import *

if __name__ == '__main__':
    # plot_commits_with_cp()

    commit_res_dir = "../../commit_benchmark/lz4hc/results"
    commit_hash_file = "../../benchmark/lz4commits"

    comp_dict, decomp_dict, labels = import_benchmark_data(commit_hash_file, commit_res_dir)

    compression_speed = comp_dict["lz4 1.9.2"]
    decompression_speed = decomp_dict["lz4 1.9.2"]

    compression_speed.reverse()
    decompression_speed.reverse()

    print("Starting Analysis")

    comp_analysis = e_divisive_analysis(compression_speed)
    decomp_analysis = e_divisive_analysis(decompression_speed)

    print("E_Divisive Analysis")
    print(comp_analysis)
    print(decomp_analysis)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
