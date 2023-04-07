def subset_sum(numbers, target):
    # Create a list to store the sums of all possible subsets
    sums = [0]

    # Loop through each number in the list and add it to each of the
    # sums in the list so far
    for number in numbers:
        new_sums = []
        for _sum in sums:
            new_sum = _sum + number
            if new_sum == target:
                return [number]
            elif new_sum < target:
                new_sums.append(new_sum)
        sums += new_sums

    # Find the sum closest to the target, but not exceeding it
    closest_sum = max([_sum for _sum in sums if _sum <= target])
    # Find the subset that adds up to the closest sum
    subset = []
    for number in reversed(numbers):
        if closest_sum - number in sums:
            subset.append(number)
            closest_sum -= number
    subset.reverse()

    return subset

numbers = [7, 2, 3, 4, 5]
target = 13

subset = subset_sum(numbers, target)
print(f"Subset that adds up to {target}: {subset}")
print("subset=",subset)