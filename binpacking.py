# explanations for member functions are provided in requirements.py

import random as rand
import math 
import time
from collections.abc import Iterable

# Use the provided Merge Sort for sorting

class MergeSort:
	def __init__(self):
		self.time = 0

	def sort(self, data):
		self.sortHelper(data, 0, len(data))

	def sortHelper(self, data, low, high):
		if high - low > 1:
			mid = low + (high-low)//2
		
			self.sortHelper(data, low, mid)	
			self.sortHelper(data, mid, high)
			self.merge(data, low, mid, high)

	def merge(self, data, low, mid, high):
		temp = []
		
		i = low
		j = mid

		while (i < mid and j < high):
			if data[i] < data[j]:
				temp.append(data[i])
				i += 1
			else:
				temp.append(data[j])
				j += 1
		while (i < mid):
			temp.append(data[i])
			i += 1
		while (j < high):
			temp.append(data[j])
			j += 1
		for k in range(len(temp)):
			data[k+low] = temp[k] 

# Implement the Next Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class NextFit:
    def __init__(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.bin_size = 1
        self.num_bins = 0
    
    def reset(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.num_bins = 0

    def measure(self, data):
        optimal = math.ceil(sum(data))
        #self.num_bins = self.pack(data) superf?
        waste = self.num_bins - sum(data)
        self.waste.append(waste)
        return waste

    def pack(self, data):
        working_space = self.bin_size
        working_bin = []
        
        for chunk in data:
            if chunk <= working_space:
                working_bin.append(chunk)
                working_space -= chunk
            else:
                self.bins.append(working_bin)
                working_bin = chunk
                working_space = self.bin_size - chunk

        if working_bin:
            self.bins.append(working_bin)
            
        self.num_bins = len(self.bins)

        return self.num_bins

# Implement the First Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class FirstFit:
    def __init__(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def measure(self, data):
        self.reset()
        start_time = time.perf_counter()
        bin_capacity = 1
        total_sum = sum(data)
        optimal = math.ceil(total_sum / bin_capacity)

        self.num_bins = self.pack(data)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)

        actual_bins = self.num_bins
        waste = (actual_bins * bin_capacity) - total_sum
        self.waste.append(waste)

        return waste

    def pack(self, data):
        bin_capacity = 1
        for item in data:
            placed = False
            for i in range(len(self.bin_sums)):
                if self.bin_sums[i] + item <= bin_capacity:
                    self.bins[i].append(item)
                    self.bin_sums[i] += item
                    placed = True
                    break
            if not placed:
                self.bins.append([item])
                self.bin_sums.append(item)
                self.num_bins += 1

        return self.num_bins

# Implement the Best Fit Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class BestFit:
    def __init__(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def measure(self, data):
        self.reset()
        start_time = time.perf_counter()
        bin_capacity = 1
        total_sum = sum(data)
        optimal = math.ceil(total_sum / bin_capacity)
        self.num_bins = self.pack(data)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)
        actual_bins = self.num_bins
        waste = (actual_bins * bin_capacity) - total_sum
        self.waste.append(waste)

        return waste

    def pack(self, data):
        bin_capacity = 1
        for item in data:
            best_fit_index = -1
            min_space_left = bin_capacity + 1

            for i in range(len(self.bin_sums)):
                space_left = bin_capacity - self.bin_sums[i]
                if space_left >= item and space_left < min_space_left:
                    best_fit_index = i
                    min_space_left = space_left

            if best_fit_index >= 0:
                self.bins[best_fit_index].append(item)
                self.bin_sums[best_fit_index] += item
            else:
                self.bins.append([item])
                self.bin_sums.append(item)
                self.num_bins += 1

        return self.num_bins
	
# Implement the First Fit Decreasing Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class FirstFitDec:
    def __init__(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = FirstFit()

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = FirstFit()

    def measure(self, data):
        self.reset()
        self.sorter.sort(data)
        data.reverse()

        start_time = time.perf_counter()

        waste = self.packer.measure(data)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)

        self.bins = self.packer.bins
        self.bin_sums = self.packer.bin_sums
        self.waste = self.packer.waste
        self.times = self.packer.times
        self.num_bins = self.packer.num_bins

        return waste

# Implement the Best Fit Decreasing Bin Packing Algorithm
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class BestFitDec:
    def __init__(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = BestFit()

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = BestFit()

    def measure(self, data):
        self.reset()

        self.sorter.sort(data)
        data.reverse()

        start_time = time.perf_counter()

        waste = self.packer.measure(data)

        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        self.times.append(elapsed_time)

        self.bins = self.packer.bins
        self.bin_sums = self.packer.bin_sums
        self.waste = self.packer.waste
        self.times = self.packer.times
        self.num_bins = self.packer.num_bins

        return waste

# Implement a Custom Fit Bin Packing Algorithm
# 	The goal is to modify the best performing (fewest bins) algorithm
# 	to try to improve the packing (number of bins) for at least 1 set of the standard input data.
#	HINT: 		try modifying data after sorting 
# 	bins: 		is a list of lists, where each inner list shows the contents of a bin (do not change)
#	bin_sums: 	is a list of sums, one for each bin
# 	waste: 		is the computed waste for the input data (do not change)
#	times:		is a list to hold the run times (do not change)
# 	num_bins: 	stores the number of bins required to pack the data (do not change)
#	sorter:		sorting object
# 	packer:		bin packing object
# 	reset: 		is a method to reset the state of the packing object (do not change)
# 	measure: 	is a method to compute the waste by estimating the optimal and calling pack on the data
#	pack: 		is a method which implements the bin packing algorithm

class CustomFit:
    def __init__(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = NextFit() 

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = NextFit()

    def measure(self, data):
        # TODO: Sort Data
        
        # Implement Optimization
  
        waste = self.packer.measure(data)
        self.bins = self.packer.bins
        self.bin_sums = self.packer.bin_sums
        self.waste = self.packer.waste
        self.times = self.packer.times
        self.num_bins = self.packer.num_bins
        return waste

    def pack(self, data):
        data = self.sorter(data)
        working_space = self.bin_size
        working_bin = []
        bow = 0
        stern = 1
        buffer = data[-stern]

        for chunk in data:
            if chunk <= working_space:
                working_bin.append(chunk)
                working_space -= chunk
                bow += 1
            elif buffer <= working_space:
                working_bin.append(buffer)
                working_space -= buffer
                stern += 1
                buffer = data[-stern]
            else:
                self.bins.append(working_bin)
                working_bin = chunk
                working_space = self.bin_size - chunk
                bow +=1

            if bow + stern == (len(data)-1):
                break
            
        if working_bin:
            self.bins.append(working_bin)
            
        self.num_bins = len(self.bins)

        return self.num_bins

	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
