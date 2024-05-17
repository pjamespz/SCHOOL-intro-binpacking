# explanations for member functions are provided in requirements.py

import random as rand
import math 
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
		self.num_bins = 0

	def reset(self):
		self.bins = []
		self.waste = []
		self.times = []
		self.num_bins = 0

	def measure(self, data):
		optimal = 0 # TODO - implement estimation of optimal
		self.num_bins = self.pack(data)
		waste = 0 # TODO - calculate the waste
		self.waste.append(waste)
		return waste

	def pack(self, data):
		# Implement the bin packing algorithm
  
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
		optimal = 0 # TODO - implement estimation of optimal
		self.num_bins = self.pack(data)
		waste = 0 # TODO - calculate the waste
		self.waste.append(waste)
		return waste

	def pack(self, data):
		# Implement the bin packing algorithm

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
		optimal = 0 # TODO - implement estimation of optimal
		self.num_bins = self.pack(data)
		waste = 0 # TODO - calculate the waste
		self.waste.append(waste)
		return waste

	def pack(self, data):

		# Implement the bin packing algorithm

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
		# TODO: Sort data
		waste = 0 # TODO: call measure method of bin packing algorithm
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
		# TODO: Sort data
		waste = 0 # TODO: call measure method of bin packing algorithm
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
		self.packer = None # TODO: Use the best bin packing algorithm based on the test data 

	def reset(self):
		self.bins = [[]]
		self.bin_sums = [0]
		self.waste = []
		self.times = []
		self.num_bins = 1
		self.sorter = MergeSort()
		self.packer = None # TODO: Use the best bin packing algorithm based on the test data 

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


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define
