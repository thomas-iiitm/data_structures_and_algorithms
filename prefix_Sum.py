"""
 Computes the sum of elements in array A for each [L, R] range in B using a prefix sum. 
 For each query [L, R] in B, returns the sum of A[L..R] both inclusive
 Time Complexity - O(N) 
 Space Complexity - O(N)
"""
from itertools import accumulate

def rangeSum(self, A, B):

    prefix_sum = [0] + list(accumulate(A))

    res = []
    for L, R in B:
        res.append(prefix_sum[R + 1] - prefix_sum[L])

    return res



"""
 Find the point of equilibrium such that sum of elements on left side equals sum of elements on right side
 Time Complexity - O(N) 
 Space Complexity - O(N)
"""

def point_of_equilibrium(A):
    prefix_sum = list(accumulate(A))
    left_sum, right_sum = 0,0
    res = -1
    for i in range(0,len(A)):
        left_sum = 0 if i==0 else prefix_sum[i-1]
        right_sum = prefix_sum[len(A)-1] - prefix_sum[i]
        if left_sum == right_sum:
            res = i
            break
    return res



"""
    Return the count of indices i such that removing A[i] makes the sum of
    elements at even indices equal to the sum at odd indices in the new array.  
    Also capture the indices that need to remvoed.

    Time Complexity - O(N + M)
    Space Complexity - O(1)
      
"""

def solution(A):
    total_sum_odd, total_sum_even = 0, 0
    for i in range(0, len(A), 2):
        total_sum_even += A[i]
    for i in range(1, len(A), 2):
        total_sum_odd += A[i]

    even_seen, odd_seen = 0, 0

    list_indices = []
    # print(f"Odd Sum -- {total_sum_odd}")
    # print(f"Even Sum --- {total_sum_even}")

    for i, elm in enumerate(A):
        # print(f"\n ******* {i}, {elm} *******")
        if i%2 == 0:
            even_new = even_seen + (total_sum_odd - odd_seen)
            odd_new = odd_seen + (total_sum_even - even_seen - elm)
        else:
            even_new = even_seen + (total_sum_odd - odd_seen - elm)
            odd_new = odd_seen + (total_sum_even - even_seen)

        # print(f" ------- {even_new}, {odd_new} -------")
        if even_new == odd_new:
            list_indices.append(i)

        if i%2 == 0:
            even_seen += elm
        else:
            odd_seen += elm

    return len(list_indices)
