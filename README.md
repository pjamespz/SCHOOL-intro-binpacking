# **Bin Packing Algorithms**
- Peyton Politewicz, Drake Watson

*View the project [here](https://github.com/pjamespz/SCHOOL-intro-binpacking/blob/main/295P-Project-2-PeytonPolitewicz-DrakeWatson.pdf).*

### Custom Packing Algorithm Choice: NextFit, Decreasing, With Two Pointers
- Our custom packing algorithm takes advantage of the fact that our data is uniformly distributed.
- We use NextFit, but we reverse-sort the data as in the BestFit and FirstFit Decreasing algorithms.
- Then, we align a buffer pointer with the last index in the data - the smallest value.
- We use a two-pointer approach to ‘zipper’ pack the data, first checking the largest value, then checking the lowest value, and bringing the two pointers together toward the center of the dataset.
- This was initially tested with randomly generated values from 0 to 1 - the maximum size of the bin - and it performed just as well as BFD and FFD.
- However, the transition to max data sizes below the capacity of the bin proved a massive performance impact because this would wind up taking the first value, then many of the small values, and so on...
- To fix this, we instead split the data into two envelopes.
- The first envelope is found by bringing the low-value pointer up the dataset until it finds a value that would overflow a bin when added to the largest value.
- It then takes one step back - this demarcates the first envelope and the algorithm packs the first set.
- Then, the remaining values are folded into bins the same way.
- This two-envelope approach claws back the majorty of the performance gain over normal NextFit, and results in the CustomFit performing better than anything other than BFD and FFD in terms of waste.
- When it comes to runtime, however, our CustomFit ran dramatically faster than every algorithm other than NextFit.
- In the end, using NextFit as a baseline for performance, and considering BFD/FFD as an optimal case, **our CustomFit performs 98.7% as well as BFD/FFD in terms of waste, but operates 127,441.01% faster.**
