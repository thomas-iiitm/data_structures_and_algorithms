"""
    Return the count of indices i such that removing A[i] makes the sum of
    elements at even indices equal to the sum at odd indices in the new array.  

    Also capture the indices that need to remvoed.
      
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
