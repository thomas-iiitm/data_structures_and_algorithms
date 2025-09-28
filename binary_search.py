# Typical Binary Search -- assumes a sorted list is provided
# Time: O(log n), Space: O(1)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid   # found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # not found



# Find square root of a number using Binary Search - Finds floor(√n)  

def sqrt(n):
    if n < 2:
        return n
    left, right = 1, n // 2 # square root will be always be less than N/2
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
