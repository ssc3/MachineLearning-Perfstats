# MachineLearning-Perfstats

MIT License

Copyright (c) [2017] [Shubhojit Chattopadhyay]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

GOAL OF THE PROJECT
To predict d1 cache behavior based on a set of trace files used for the set

HOW TO USE?
- Clone this repository
- python perfstatspred.py
- Inputs are: # l1-dcache-loads, l1-dcache-load-misses, l1-dcache-stores
- Output is: d1 misses as a percentage of d1 accesses
- To change the input under test, go to end of perfstatspred.py and modify the list with 3 numbers 
  new_input = array([0, 22729, 23345])
  


HOW DOES THIS WORK?
This is a single neuron simple neural network. D1 cache training data was collected on a simple C program, 
doing the same operation on a sorted vs unsorted array. The neural network first trains the neuron and
then, for a new input makes a prediction of what its d1 miss percentage would be.


IS THIS PERFECT?
Not at all. No extensive testing has been done. No research on why adjustments are calculated the way they are
The trace data was collected using linux perf tools FOR A SINGLE WORKLOAD on a BUSY machine. So no reason why these traces represent anything other than my own laptop behavior.
Further, the training set is not representative of anything. If anything, I believe it is heavily skewed towards showing less d1 cache miss percentage.

EXAMPLE:
RESULT WITH REAL PERF STAT:
ssc3@ssc3:~/neuron-predictor$ perf stat -e L1-dcache-loads,L1-dcache-load-misses,L1-dcache-stores ./a.out
Count = 99999

 Performance counter stats for './a.out':

         1,280,947 L1-dcache-loads                                             
            23,775 L1-dcache-load-misses     #    1.86% of all L1-dcache hits  
           546,344 L1-dcache-stores                                            

       0.001776835 seconds time elapsed
       
       
RESULT WITH PREDICTION:
---> Testing with new input (same as what perf stats had)
Considering new input = [1280947   23775  546344]

**** RESULT *****
Normalized = [ 0.]
Denormalized = [ 1.88]  <------ RESULT


WHOA! IS IT ALWAYS THIS ACCURATE?
No. Multiple reasons for it. The training set is woefully inadequate and skews towards smaller value for cache misses.



