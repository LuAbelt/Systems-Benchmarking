#!/bin/bash

# This bash file builds and benchmarks lz4 against a specific commit

USER=abeltluk
USER_BASE_DIR=/scratch/$USER/SystemsBenchmarking
LZBENCH_DIR=$USER_BASE_DIR/lzbench
LZ4_DIR=$USER_BASE_DIR/lz4
SILESIA_DIR=$USER_BASE_DIR/silesia

RELEASE=$1

BENCH_BASE_DIR=$2
WORKING_DIR=$BENCH_BASE_DIR/build/$RELEASE

RESULT_FILE=$BENCH_BASE_DIR/results/$RELEASE.res
TIMINGS_FILE=$BENCH_BASE_DIR/results/$RELEASE.timings

# Time start of benchmark run
date +%s%N >> $TIMINGS_FILE

# Setup environment
mkdir -p $WORKING_DIR
mkdir -p $BENCH_BASE_DIR/results
cd $WORKING_DIR

# Copy LZBench and LZ4 from base
# Timing
date +%s%N >> $TIMINGS_FILE

cp -r $LZBENCH_DIR .

# Timing
date +%s%N >> $TIMINGS_FILE

cp -r $LZ4_DIR .

# Timing
date +%s%N >> $TIMINGS_FILE

# Copy siselia corpus
cp -r $SILESIA_DIR .

# Timing
date +%s%N >> $TIMINGS_FILE

# Checkout correct version of lz4:
cd ./lz4
git checkout $RELEASE

# Timing
date +%s%N >> $TIMINGS_FILE

# Overwrite lz4 files of lzbench
cd $WORKING_DIR
cp -r ./lz4/lib/* ./lzbench/lz4

# Timing
date +%s%N >> $TIMINGS_FILE

# Build lzbench with new version
cd ./lzbench
make

# Timing
date +%s%N >> $TIMINGS_FILE

cd $WORKING_DIR
# Run lzbench 
#./lzbench/lzbench -elz4/lz4hc -t60,60 -p3 -j -r -o4 -v silesia > $RESULT_FILE
./lzbench/lzbench -elz4hc,1 -t60,60 -p3 -j -r -o4 -v silesia > $RESULT_FILE

# Timing
date +%s%N >> $TIMINGS_FILE

# Cleanup
cd $USER_BASE_DIR
rm -rf $WORKING_DIR

# Timing data
date +%s%N >> $TIMINGS_FILE
