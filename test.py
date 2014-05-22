def test_sort(fn, size, debug = True):
	import random
	vals = [10+i for i in range(size)]
	random.shuffle(vals)
	if debug:
		print 'before sort', vals
	vals = fn(vals)
	if debug:
		print 'after sort' , vals
	
	
if __name__ == '__main__':
	import time
	begin=time.time()
	test_sort(insert_sort, size=50)
	print time.time() - begin
	
