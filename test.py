#!/usr/bin/env python

import random
import time
import getopt
import importlib


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
	begin=time.time()
	test_sort(insert_sort, size=50)
	print "this sorting takes totally: ", time.time() - begin
	
