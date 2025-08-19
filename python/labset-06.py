import numpy

arr1 = numpy.array([1, 2, 3, 4, 5])
arr2 = numpy.array([10, 20, 30, 40, 50])



print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise addition
add_result = arr1 + arr2
print("\n Addition:", add_result)

# Element-wise multiplication
mul_result = arr1 * arr2
print("Multiplication:", mul_result)

# Compute statistics
mean_val = numpy.mean(arr1)
var_val = numpy.var(arr1)
std_val = numpy.std(arr1)

print("\nMean of arr1:", mean_val)
print("Variance of arr1:", var_val)
print("Standard Deviation of arr1:", std_val)
