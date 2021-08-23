#!/bin/bash
#SBATCH --job-name=labelt-lz4-release-benchmarks
#SBATCH --exclusive
#SBATCH --partition=seminar
#SBATCH --constraint=kine
#SBATCH --array=0-12
#SBATCH --output=/scratch/abeltluk/slurm_logs/lz4releases/release_benchmark_%A_%a.out
#SBATCH --error=/scratch/abeltluk/slurm_logs/lz4releases/release_benchmark_%A_%a.err

USER=abeltluk
USER_BASE_DIR=/scratch/$USER
RELEASES_FILE=$USER_BASE_DIR/lz4releases

RELEASES_LIST=($(<$RELEASES_FILE))
RELEASE=${RELEASES_LIST[${SLURM_ARRAY_TASK_ID}]}

srun ./run_benchmark.sh $RELEASE
