import numpy as np

# Create an array
data = np.array([10, 20, 30, 40, 50])

print("Original Array:", data)

# Array indexing
print("First Element:", data[0])

# Array slicing
print("First Three Elements:", data[:3])

# Mathematical operations
print("Addition:", data + 5)
print("Multiplication:", data * 2)

# Statistical operations
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

print("Day 26 Completed!")