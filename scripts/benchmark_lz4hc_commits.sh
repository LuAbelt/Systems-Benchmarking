#!/bin/bash
#SBATCH --job-name=labelt-lz4hc-commits-benchmarks
#SBATCH --exclusive
#SBATCH --partition=seminar
#SBATCH --constraint=kine
#SBATCH --time=1-00:00:00
#SBATCH --output=/scratch/abeltluk/slurm_logs/lz4commits/commit_benchmark_%A_%a.out
#SBATCH --error=/scratch/abeltluk/slurm_logs/lz4commits/commit_benchmark_%A_%a.err

USER=abeltluk
USER_BASE_DIR=/scratch/$USER
COMMIT_FILE=$USER_BASE_DIR/SystemsBenchmarking/benchmark/lz4hc_commits

COMMITS_LIST=($(<$COMMIT_FILE))

BENCH_BASE_DIR=$USER_BASE_DIR/SystemsBenchmarking/commit_benchmark/lz4hc_180_181

for (( run=0; run<${#COMMITS_LIST[@]}; run++ )); do
	COMMIT=${COMMITS_LIST[${run}]}

	srun ./run_benchmark.sh $COMMIT $BENCH_BASE_DIR
done
