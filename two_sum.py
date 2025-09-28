# Find ALL pair of numbers that sum up to a number (target). Assume that you have a sorted array (arr)
# Time: O(n), Space: O(1)

def two_sum_all(arr, target):
    left, right = 0, len(arr) - 1 # Using two pointers
    results = []
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            results.append((arr[left], arr[right])) # found a pair
            left += 1
            right -= 1
        elif s < target:
            left += 1   # need bigger sum
        else:
            right -= 1  # need smaller sum
    return results or None
