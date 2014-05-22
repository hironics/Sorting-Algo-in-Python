def quick_sort(datalist):
	if not datalist:
		return []
	
	pivot = datalist[0]
	left = []
	right = []
	for i in range(1, len(datalist)):
		if datalist[i] > pivot:
			right.append(datalist[i])
		elif datalist[i] < pivot:
			left.append(datalist[i])
	return quick_sort(left) + [pivot] + quick_sort(right)		
			

