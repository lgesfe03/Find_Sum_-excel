def find_closest_sum(arr, target_sum):
    n = len(arr)
    dp = [[False for j in range(target_sum + 1)] for i in range(n + 1)]
    dp[0][0] = True
    closest_sum = None

    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            if arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][int(j - arr[i - 1])]
            if dp[i][j] and (closest_sum is None or abs(target_sum - j) < abs(target_sum - closest_sum)):
                closest_sum = j

    if closest_sum == target_sum:
        print("The target sum can be obtained exactly.")
    else:
        print(f"The closest sum to the target is {closest_sum}.")

    print("The components of the closest sum are:")

    i = n
    j = closest_sum
    while i > 0 and j > 0:
        if dp[i - 1][j]:
            i -= 1
        else:
            print(arr[i - 1])
            j -= int(arr[i - 1])
            i -= 1

# example usage
arr = [4.0, 6.0, 9, 13, 16, 19]
target_sum = 3045
find_closest_sum(arr, target_sum)
