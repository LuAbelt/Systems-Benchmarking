#!/bin/bash

# This bash file builds and benchmarks lz4 against a specific commit

USER=abeltluk
USER_BASE_DIR=/scratch/$USER
LZBENCH_DIR=$USER_BASE_DIR/lzbench
LZ4_DIR=$USER_BASE_DIR/lz4
SILESIA_DIR=$USER_BASE_DIR/silesia

RELEASE=$1

REL_BENCH_BASE_DIR=$USER_BASE_DIR/commit_benchmark
WORKING_DIR=$REL_BENCH_BASE_DIR/build/$RELEASE

RESULT_FILE=$REL_BENCH_BASE_DIR/results/$RELEASE.res
TIMINGS_FILE=$REL_BENCH_BASE_DIR/results/$RELEASE.timings

# Setup environment
mkdir $WORKING_DIR
cd $WORKING_DIR

# Copy LZBench and LZ4 from base
cp -r $LZBENCH_DIR .
cp -r $LZ4_DIR .

# Copy siselia corpus
cp -r $SILESIA_DIR .

# Checkout correct version of lz4:
cd ./lz4
git checkout $RELEASE

# Overwrite lz4 files of lzbench
cd $WORKING_DIR
cp -r ./lz4/lib/* ./lzbench/lz4

# Build lzbench with new version
cd ./lzbench
make

cd $WORKING_DIR
# Run lzbench TODO
./lzbench/lzbench -elz4 -i10,10 -j -r -o4 -v silesia > $RESULT_FILE

# Cleanup
cd $USER_BASE_DIR
rm -rf $WORKING_DIR
