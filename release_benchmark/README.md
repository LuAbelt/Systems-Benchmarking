# About this directory

This directory contains various subdirectories where the benchmark results of different runs on releases have been collected.

Generally the exact results are always again contained in a separate `results` directory. For each commit the results will be contained in a file which base name is the (short) commit hash. There are generally two types of files in these directories:
* `.res` files - This contains the output as it was created by `lzbench` in a CSV format
* `.timings` files - These files contain additional timing information about the benchmark run itself. These could e.g. be used to further evaluate the required time of such a benchmark. This data was not used in this paper.

This directory contains the following directories:
* `lz4hc` - Contains results for the performance benchmark on `lz4hc`
* `mintime` - Contains results for the benchmark on the releases of `lz4` with the `-t60,60` argument passed to `lzbench`
* `results` - Contains results for the benchmark on the releases of `lz4` with the `-i100,100` argument passed to `lzbench`