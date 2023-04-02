import json
import time

# O(n*log(n))

def partition(array, low, high):
	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1
def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)

f = open('random_elem.json')
data = json.load(f)
size = len(data[1])

start_time = time.time()
quickSort(data[1], 0, size - 1)
end_time = time.time()

print((end_time-start_time)*10)
print("\n"+ str(end_time-start_time))
