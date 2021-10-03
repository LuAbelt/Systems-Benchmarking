# Systems Benchmarking Seminar 2021 - Paper and Experiment implementation
#### By Lukas Abelt
___

## About this Repository
This repository is the result of the "Systems Benchmarking" seminar in summer semester 2021 at Saarland University (https://cms.sic.saarland/se_seminar_ss21/). It contains all relevant information and implementation artifacts that were used to write the seminar paper about "Benchmarking Before Releases vs. Before Each Commit" by Lukas Abelt. It's main motivation was to ensure the reproducibility of the experiment that was performed as part of this seminar paper.

___
## Repository Structure

This repository consists of the following sub-directories:
* `benchmark` - Contains files that list relevant commits used in the experiment
* `code` - Contains code artifacts that were used to evaluate the experiment results
* `commit_benchmark` - Contains raw results of the benchmarks performed on individual commits
* `lz4` - Git submodule to the original lz4 Git repository (https://github.com/lz4/lz4)
* `lzbench` - Git submodule to a slightly adapted version of lzbench (https://github.com/inikep/lzbench)
* `release_benchmark` - Contains raw results of the benchmarks performed on releases on lz4
* `scripts` - Contains the slurm scripts used to perform the benchmarking experiment
* `silesia` - Contains the silesia compression corpus that was used in this experiment (http://sun.aei.polsl.pl/~sdeor/index.php?page=silesia)
* `tex` - Contains the tex files that were used to create the seminar paper

More detailed information can be found in the respective README files of the directories 