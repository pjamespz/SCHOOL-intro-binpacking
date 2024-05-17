import binpacking
import random
import time
import math

'''
The first part of this code will verify functional correctness of all bin packing algorithms.
'''

random.seed(260)

names = ["NexFit", "FirstFit", "BestFit", "FirstFitDec", "BestFitDec", "CustomFit"]

packer = [None]*6
packer[0] = binpacking.NextFit()
packer[1] = binpacking.FirstFit()
packer[2] = binpacking.BestFit()
packer[3] = binpacking.FirstFitDec()
packer[4] = binpacking.BestFitDec()
packer[5] = binpacking.CustomFit()

DATA_SIZE = 50
NUM_EXP = 9
data = []


for j in range(NUM_EXP):
    print()
    DATA_SIZE = DATA_SIZE * 2
    print("DATA_SIZE:", DATA_SIZE)
    data = []
    for i in range(DATA_SIZE):
        data.append(round(random.uniform(0.0,0.8), 8))

    data_save = data.copy()

    # Uniformly distributed data
    
    for i in range(len(packer)):
        packer[i].reset()
        # print(names[i])
        data = data_save.copy()
        start_time = time.perf_counter()
        packer[i].measure(data)
        end_time = time.perf_counter()
        packer[i].times.append(end_time - start_time)
    print()
    print("Uniformly Distributed Random Data Waste: ")
    for i in range(len(packer)):
        print(names[i], packer[i].waste)

    print()

    print("Uniformly Distributed Random Data Time: ")
    for i in range(len(packer)):    
        print(names[i], packer[i].times)

# Please read all of the following before starting your implementation:
#
# Details about Gradescope submission:
#
# - You should not include anything outside of standard Python libraries.
# - Functions should be tested using Python 3.6+ on a Linux environment.
# - You must submit the binpacking.py file and a project report, along with any additional source files that you might create
# - The submission should either be the files themselves, or a zip file not containing any directories.
# - The python file and the project report will be submitted to 2 different assignments. The autograder will be set up to test your code.
#
# A) Finish the implementations of the following bin packing algorithms:
# 
# - Next Fit
# - First Fit
# - Best Fit
# - First Fit Decreasing
# - Best Fit Decreasing
# - Custom Fit
#
# - Each algorithm is implemented as a class. The testing code can be seen above. 
# 
# - Executing project2_tests.py will call the bin packing algorithms on random data uniformly distributed between 0 and 0.8.
#
# B) Report:
# - 1) Plot each algorithm's waste as a function of the data size. 
# - 2) You will test each algorithm on lists of items of length n, as n grows, where the n items in the lists are 
# - floating point numbers between 0.0 and 0.8 generated uniformly at random. The code for running the experiments is provided
# - in this file. Each algorithm is defined to operate with bins of size 1. The goal of these experiments is to determine an 
# - estimate for the waste, W(A), for each of the above bin-packing algorithms, A, as a function of n, as n grows, 
# - where W(A) is defined as follows:
# - The waste, W(A), of a bin-packing algorithm, A, for any given list of items, is the number of bins used by the algorithm A 
# - minus the total size (i.e., the sum) of all the items in the list.
# - You should test multiple random sequences for each length n, and have n grow, and then plot the results on a log-log scale to see 
# - if there is a line that fits the data. If so, you should then determine the slope of that line, so as to provide 
# - experimental evidence for estimating W(A) as a function of n, and you should give that function in your report, 
# - for each algorithm, A.

# - 3) Discuss what you observe for the run times of the algorithms in the report. Use the log-log scale plots to estimate the big-O 
# - run-time of each bin packing algorithm
#

# - 
