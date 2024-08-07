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
        self.bins = [[]]
        self.waste = []
        self.times = []
        self.bin_size = 1
        self.num_bins = 1
    
    def reset(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.num_bins = 1

    def measure(self, data):
        self.reset()
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time

    def pack(self, data):
        working_space = self.bin_size
        working_bin = []
        
        for chunk in data:
            if chunk <= working_space:
                working_bin.append(chunk)
                working_space -= chunk
            else:
                self.bins.append(working_bin)
                working_bin = [chunk]
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
        self.bin_size = 1
        self.num_bins = 1

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def measure(self, data):
        self.reset()
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time

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
        self.bin_size = 1

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1

    def measure(self, data):
        self.reset()
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time


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
        self.bin_size = 1
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
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.packer.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time


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
        self.bin_size = 1
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
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.packer.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time


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
        self.bin_size = 1
        self.sorter = MergeSort()
        self.packer = twoPointerFit() 

    def reset(self):
        self.bins = []
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.sorter = MergeSort()
        self.packer = twoPointerFit()

    def measure(self, data):
        self.reset()
        self.sorter.sort(data)
        data.reverse()
        start_time = time.perf_counter()  # Start timing
        
        self.num_bins = self.packer.pack(data)
        
        end_time = time.perf_counter()  # End timing
        elapsed_time = end_time - start_time
        
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        
        return waste, elapsed_time

    def pack(self, data):
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
                working_bin = [chunk]
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

class twoPointerFit:
    def __init__(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.bin_size = 1
        self.num_bins = 0
        self.sorter = MergeSort()  # Assuming MergeSort is defined elsewhere
    
    def reset(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.num_bins = 0

    def measure(self, data):
        self.reset()
        self.num_bins = self.pack(data)
        total_space_used = self.num_bins * self.bin_size
        total_data_size = sum(data)
        waste = total_space_used - total_data_size
        self.waste.append(waste)
        return waste

    def pack(self, data):
        data = sorted(data, reverse=True)
        working_space = self.bin_size
        working_bin = []
        bow = 0
        stern = 1
        firstEnv = len(data)
        i = 0
        #first run setup - set zipper band
        while True:
            if data[bow] + data[-stern] >= 1 or stern == len(data):
                break
            else:
                stern += 1
                firstEnv -= 1
        
        offset = len(data) - stern + 1
        buffer = data[-stern]

        while i < firstEnv:
            if data[bow] <= working_space:
                working_bin.append(data[bow])
                working_space -= data[bow]
                bow += 1
            elif bow + stern - 1 < len(data) and buffer <= working_space:
                working_bin.append(buffer)
                working_space -= buffer
                stern += 1
                if bow + stern - 1 < len(data):
                    buffer = data[-stern]
            else:
                self.bins.append(working_bin)
                working_bin = []
                if bow < len(data):
                    working_bin.append(data[bow])
                    working_space = self.bin_size - data[bow]
                    bow += 1
            i += 1
        #setup second pass of remaining values
        bow = offset
        stern = 1
        buffer = data[-stern]
        i = 0

        while i < len(data) - offset:

            if bow < len(data) and data[bow] <= working_space:
                working_bin.append(data[bow])
                working_space -= data[bow]
                bow += 1

            elif bow + stern - 1 < len(data) and buffer <= working_space:
                working_bin.append(buffer)
                working_space -= buffer
                stern += 1
                if bow + stern - 1 < len(data):
                    buffer = data[-stern]

            else:
                self.bins.append(working_bin)
                working_bin = []
                if bow < len(data):
                    working_bin.append(data[bow])
                    working_space = self.bin_size - data[bow]
                    bow += 1
                else:
                    break
            i += 1

        if working_bin:
            self.bins.append(working_bin)

        self.num_bins = len(self.bins)

        return self.num_bins