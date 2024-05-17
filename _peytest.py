import math

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

class NextFit:
    def __init__(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.bin_size = 1
        self.num_bins = 0
        self.working_bin = []

    def reset(self):
        self.bins = []
        self.waste = []
        self.times = []
        self.num_bins = 0

    def measure(self, data):
        optimal = math.ceil(sum(data))
        self.num_bins = self.pack(data)
        waste = self.num_bins - sum(data)
        self.waste.append(waste)
        return waste

    def pack(self, data):
        working_space = self.bin_size
        for chunk in data:
            if chunk <= working_space:
                self.working_bin.append(chunk)
                working_space -= chunk
            else:
                self.bins.append(self.working_bin)
                self.working_bin = [chunk]
                working_space = self.bin_size - chunk

        if self.working_bin:
            self.bins.append(self.working_bin)
            
        self.num_bins = len(self.bins)

        return self.num_bins

class CustomFit:
    def __init__(self):
        self.bins = []
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 1
        self.bin_size = 1
        self.sorter = MergeSort()
        self.packer = NextFit() 

    def reset(self):
        self.bins = [[]]
        self.bin_sums = [0]
        self.waste = []
        self.times = []
        self.num_bins = 0
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
        data = sorted(data, reverse = True)
        working_space = self.bin_size
        working_bin = []
        bow = 0
        stern = 1
        buffer = data[-stern]

        for chunk in data:
            print(chunk)
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

            if bow + stern == (len(data)+1):
                break
            
        if working_bin:
            self.bins.append(working_bin)
            
        self.num_bins = len(self.bins)

        return self.num_bins
    # feel free to define new methods in addition to the above
    # fill in the definitions of each required member function (above),
    # and for any additional member functions you define

   
data = [.6, .5, .3, .3, .2, .2, .9, .8, .1, .2]

packer = CustomFit()
packer.pack(data)
print(packer.bins)