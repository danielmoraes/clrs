import sys
import time
import random


def FindMaximumSubarrayBruteForce(A):
    max_sum = MIN_INT
    l, h = -1, -1
    for i in range(0, len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
                l, h = i, j
    return l, h, max_sum


def FindMaximumCrossingSubarray(A, low, mid, high):
    max_left = -1
    left_sum = MIN_INT
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    max_right = -1
    right_sum = MIN_INT
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def FindMaximumSubarrayRecursive(A, low, high):
    if high == low:
        return (low, high, A[low])
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum =\
            FindMaximumSubarrayRecursive(A, low, mid)
        right_low, right_high, right_sum =\
            FindMaximumSubarrayRecursive(A, mid + 1, high)
        cross_low, cross_high, cross_sum =\
            FindMaximumCrossingSubarray(A, low, mid, high)

        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def FindMaximumSubarrayMixed(A, low, high):
    if high - low < CROSSOVER:
        return FindMaximumSubarrayBruteForce(A)
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum =\
            FindMaximumSubarrayRecursive(A, low, mid)
        right_low, right_high, right_sum =\
            FindMaximumSubarrayRecursive(A, mid + 1, high)
        cross_low, cross_high, cross_sum =\
            FindMaximumCrossingSubarray(A, low, mid, high)

        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

MIN_INT = -sys.maxint - 1
CROSSOVER = 52

print "   #  BruteForce  Recursive  Winner"
print "-----------------------------------"

for i in range(2, 101):
    a = [int(100 * random.uniform(-1, 1)) for j in xrange(i)]

    start = time.clock()
    FindMaximumSubarrayBruteForce(a)
    end = time.clock()
    t1 = end - start

    start = time.time()
    FindMaximumSubarrayRecursive(a, 0, len(a) - 1)
    end = time.time()
    t2 = end - start

    if t1 < t2:
        w = "B"
    elif t2 < t1:
        w = "R"
    else:
        w = "D"

    print "%4d  %.6f    %.6f   %s" % (i, t1, t2, w,)
