from visualization import *
from data_import import *
from data_analysis import *

if __name__ == '__main__':
    commit_res_dir = "../../commit_benchmark/lz4hc_180_181/results"
    commit_hash_file = "../../benchmark/lz4hc_commits"

    comp_dict, decomp_dict, labels = import_benchmark_data(commit_hash_file, commit_res_dir)

    compression_speed = comp_dict["lz4hc 1.9.2 -1"]
    decompression_speed = decomp_dict["lz4hc 1.9.2 -1"]

    comp_jd = jump_detection(compression_speed)
    decomp_jd = jump_detection(decompression_speed)

    print("Jump detection points")
    print(comp_jd)
    print(decomp_jd)

    comp_trend = trend_detection(compression_speed,10,0.05)
    decomp_trend = trend_detection(decompression_speed,10,0.05)

    print("Trend detection points")
    print(comp_trend)
    print(decomp_trend)

    comp_analysis = e_divisive_analysis(compression_speed)
    decomp_analysis = e_divisive_analysis(decompression_speed)

    print("E_Divisive Analysis")
    print(comp_analysis)
    print(decomp_analysis)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
