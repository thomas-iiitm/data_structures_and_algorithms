# Find pair of numbers that sum up to a number (target). Assume that you have a sorted array (arr)
# Time: O(n), Space: O(1)

def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])  # found the pair
        elif current_sum < target:
            left += 1  # need bigger sum
        else:
            right -= 1 # need smaller sum
    
    return None
