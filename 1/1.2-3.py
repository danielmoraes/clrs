import math

for i in xrange(1, 100):
    print "%d, %10.2f, %10.2f\n" % (i, 100 * math.pow(i, 2), math.pow(2, i),)
