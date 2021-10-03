# About this directory

This directory contains various subdirectories where the benchmark results of different runs on individual commits have been collected.

Generally the exact results are always again contained in a separate `results` directory. For each commit the results will be contained in a file which base name is the (short) commit hash. There are generally two types of files in these directories:
* `.res` files - This contains the output as it was created by `lzbench` in a CSV format
* `.timings` files - These files contain additional timing information about the benchmark run itself. These could e.g. be used to further evaluate the required time of such a benchmark. This data was not used in this paper.

This directory contains the following directories:
* `lz4hc` - Contains results for all commits between releases *v1.8.1* and *v1.8.2*. Each benchmark run measured the performance of `lz4` and `lz4hc` (including all different compression levels)
* `lz4hc_180_181` - Contains results for all commits between releases *v1.8.1* and *v1.8.2*. Each benchmark run contains the performance of `lz4hc` with compression level 1.
* `results` - Results from a very early stage of the seminar. These were preliminary results that were used in the seminar presentation. Unlike all other results, for these `lzbench` was run with the `-i100,100` argument instead of `-t60,60`