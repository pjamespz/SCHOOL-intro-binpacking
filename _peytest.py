import math
import random


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
        print(stern)
        print(firstEnv)

        while i < firstEnv:
            print(f"run {i+1}")
            print(working_space)
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
            print(f"run {i+1}")

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
        print(self.bins)

        self.num_bins = len(self.bins)

        return self.num_bins

random.seed(260)
data = []
DATA_SIZE = 50
#for i in range(DATA_SIZE):
#    data.append(round(random.uniform(0.0, 0.8), 8))
#data = sorted(data, reverse=True)
bow = 0
stern = 1
#buffer = data[-stern]
data = [0.8, 0.8, 0.8, 0.8, 0.6, 0.5, 0.4, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1]
#first run setup - set zipper band
while True:
    if data[bow] + data[-stern] >= 1 or stern == len(data):
        break
    else:
        stern += 1

packer = twoPointerFit()
packer.pack(data)