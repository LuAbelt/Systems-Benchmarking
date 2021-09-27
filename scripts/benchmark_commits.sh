#!/bin/bash
#SBATCH --job-name=labelt-lz4-commits-benchmarks
#SBATCH --exclusive
#SBATCH --partition=seminar
#SBATCH --constraint=kine
#SBATCH --array=0-6
#SBATCH --time=1-00:00:00
#SBATCH --output=/scratch/abeltluk/slurm_logs/lz4commits/commit_benchmark_%A_%a.out
#SBATCH --error=/scratch/abeltluk/slurm_logs/lz4commits/commit_benchmark_%A_%a.err

USER=abeltluk
USER_BASE_DIR=/scratch/$USER
RELEASES_FILE=$USER_BASE_DIR/SystemsBenchmarking/benchmark/lz4commits

RELEASES_LIST=($(<$RELEASES_FILE))
BENCH_BASE_DIR=$USER_BASE_DIR/SystemsBenchmarking/commit_benchmark/lz4hc

PER_TASK=50
START_NUM=$(( $SLURM_ARRAY_TASK_ID * $PER_TASK ))
END_NUM=$(( ($SLURM_ARRAY_TASK_ID + 1) * $PER_TASK ))

for (( run=$START_NUM; run<END_NUM; run++ )); do
	RELEASE=${RELEASES_LIST[${run}]}

	srun ./run_benchmark.sh $RELEASE $BENCH_BASE_DIR
done
