import time
import json
# O(n*n)

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])



f = open('random_elem.json')
data = json.load(f)

lista_timpuri_ex=[]

start_time_total = time.time()

for elem in data:
	start_time = time.time()
	size = len(elem[1])
	selectionSort(elem[1], size)
	end_time = time.time()
	
	lista_timpuri_ex.append(end_time-start_time)

stop_time_total = time.time()

print(235.62679266929626*10)
print(stop_time_total-start_time_total)

with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)
