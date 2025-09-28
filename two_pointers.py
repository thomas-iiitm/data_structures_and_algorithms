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




# You’re given an array height[] where each element represents the height of a vertical line drawn on the x-axis. Each line is drawn 
# at position i with height height[i]. What is the maximum area that can be filled with water
# Time: O(n), Space: O(1)

def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate current container area
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        
        # Move the smaller line inwards
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
