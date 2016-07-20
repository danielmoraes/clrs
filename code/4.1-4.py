def FindMaximumSubarrayLinear(A):
    low, high, sum = -1, -1, 0
    c_low, c_sum = -1, 0
    for i in range(len(A)):
        c_sum = max(A[i], c_sum + A[i])
        if c_sum == A[i]:
            c_low = i
        if c_sum > sum:
            low, high, sum = c_low, i, c_sum
    return low, high, sum

print FindMaximumSubarrayLinear([-1, 1, 2, 3, -1, -2, -2, 100])
