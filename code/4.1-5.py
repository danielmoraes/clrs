import time


def FindMaximumSubarrayLinear1(A):
    low, high, sum = -1, -1, 0
    c_low, c_sum = -1, 0
    for i in range(len(A)):
        c_sum = max(A[i], c_sum + A[i])
        if c_sum == A[i]:
            c_low = i
        if c_sum > sum:
            low, high, sum = c_low, i, c_sum
    return low, high, sum


def FindMaximumSubarrayLinear2(A):
    low, high, sum = -1, -1, 0
    c_low, c_sum = -1, 0
    for i in range(len(A)):
        if c_sum + A[i] <= 0:
            c_sum = 0
        else:
            c_sum += A[i]
            if c_sum == A[i]:
                c_low = i
            if c_sum > sum:
                low, high, sum = c_low, i, c_sum
    return low, high, sum

start = time.time()
print FindMaximumSubarrayLinear1([-1, 1, 2, 3, -1, -2, 2, 100, 300, 500])
end = time.time()
t1 = end - start

start = time.time()
print FindMaximumSubarrayLinear2([-1, 1, 2, 3, -1, -2, 2, 100, 300, 500])
end = time.time()
t2 = end - start

print "1: %.5f\n2: %.5f" % (t1, t2,)
