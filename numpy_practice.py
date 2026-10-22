
import numpy as np

# 1. Create a 1D array
numbers = np.array([10, 20, 30, 40, 50])
print("1D Array:", numbers)

# 2. Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print("\n2D Array:\n", matrix)

# 3. Indexing
print("\nFirst element:", numbers[0])
print("Third element:", numbers[2])

# 4. Slicing
print("First three elements:", numbers[:3])
print("Elements from index 2:", numbers[2:])

# 5. Mathematical operations
print("\nSum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# 6. Array arithmetic
print("\nAdd 5:", numbers + 5)
print("Multiply by 2:", numbers * 2)

# 7. Python list vs NumPy array
python_list = [1, 2, 3]
numpy_array = np.array([1, 2, 3])

print("\nPython list * 2:", python_list * 2)
print("NumPy array * 2:", numpy_array * 2)
