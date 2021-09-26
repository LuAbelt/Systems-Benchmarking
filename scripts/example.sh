#!/bin/bash
#SBATCH --job-name=testjob-luabelt
#SBATCH --output=/scratch/abeltluk/slurm_logs/slurm_log_%j.out
#SBATCH --time=10:00
#SBATCH --constraint=kine
#SBATCH --partition=seminar

srun sleep 10
srun lscpu > /scratch/abeltluk/lscpu
