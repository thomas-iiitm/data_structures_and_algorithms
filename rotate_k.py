"""
Rotate an array (shown as A) B number of times. 
Time Complexity: O(K*N)
Space Complexity: O(1)
"""

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_k(A, B):
    B = B % len(A)
    reverse(A, 0, len(A)-1)
    reverse(A, 0, B-1)
    reverse(A, B, len(A)-1)
    return A
