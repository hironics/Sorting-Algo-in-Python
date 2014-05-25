#!/usr/bin/env python
import sys
import random
import time
import getopt


DEFAULT_SIZE = 100

def test_sort(fn, size = DEFAULT_SIZE, debug = True):
    if size<10:
        size = DEFAULT_SIZE;

    vals = [10+i for i in range(size)]
    random.shuffle(vals)
    if debug:
        print 'Before sort', vals[:5], '...', vals[-5:]
    vals = fn(vals)
    if debug:
        print 'After sort' , vals[:5], '...', vals[-5:]

if __name__ == '__main__':
    sys.path.append('.')
    if len(sys.argv) == 1:
        print """%s sorting_method
        insert_sort
        """% sys.argv[0]
    else:
        pass
    m = __import__(sys.argv[1])
    begin=time.time()
    test_sort(getattr(m, sys.argv[1]), size=20000)
    print "this sorting takes totally: ", time.time() - begin

