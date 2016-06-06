import math

for i in xrange(1, 100):
    print "%d, %10.2f, %10.2f\n" % (i, 8 * math.pow(i, 2),
                                    64 * i * math.log(i, 2),)
