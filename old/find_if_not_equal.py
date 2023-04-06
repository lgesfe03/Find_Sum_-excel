import numpy as np

def find_closest_sum(arr, target_sum):
    # Sort the array in ascending order
    arr = np.sort(arr)

    # Initialize the closest_sum to a large positive number
    closest_sum = float('inf')

    # Iterate through all possible subsets of the array
    for i in range(2**len(arr)):
        subset = [arr[j] for j in range(len(arr)) if (i & (1 << j))]

        # Compute the sum of the current subset
        subset_sum = sum(subset)

        # If the subset sum is closer to the target sum than the current closest sum, update the closest sum
        if abs(subset_sum - target_sum) < abs(closest_sum - target_sum):
            closest_sum = subset_sum

        # If we find a subset that sums up to the target sum, we can stop searching and return that subset
        if closest_sum == target_sum:
            return subset

    # If no subset sums up to the target sum, return the closest sum
    return closest_sum

arr = [3, 2, 5, 1, 8, 4]
target_sum = 10

subset = find_closest_sum(arr, target_sum)
print(subset)