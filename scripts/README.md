# About this directory

This directory contains all scripts that were used on the Slurm infrastructure to perform the benchmarking experiment.

The following scripts are contained in this directory:
* `benchmark_commits.sh` - Script used to benchmark all commits for `lz4` (Between version *v1.8.1* and *v1.8.2*)
* `benchmark_commits_lz4hc.sh` - Script used to benchmark all commits for `lz4hc` (Between version *v1.8.0* and *v1.8.1*)
* `benchmark_releases.sh` - Script used to benchmark releases
* `example.sh` - Toy script for simple testing purposes
* `run_benchmark.sh` - Main driver script that was called by all other script during execution. Benchmarks a specific commit passed as an argument. Takes two positional arguments:
    1. The hash to be benchmarked as the first argument
    2. The working directory to clone, build and run the benchmark in