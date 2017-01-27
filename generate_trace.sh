#!/bin/bash

a=0
while [ "$a" -lt 100 ]    # this is loop1
do
   perf stat -e L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores ./a.out >> out.file 2>&1
   a=`expr $a + 1`
done
