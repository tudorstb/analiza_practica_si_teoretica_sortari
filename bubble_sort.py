import time
import json
def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]		
		if not swapped:
			return





f = open('random_elem.json')
data = json.load(f)
lista_timpuri_ex=[]
start_time_total = time.time()
for elem in data:
	start_time = time.time()
	bubbleSort(elem[1])
	end_time = time.time()
	lista_timpuri_ex.append(end_time-start_time)
stop_time_total = time.time()

print((stop_time_total-start_time_total)*10)
print(stop_time_total-start_time_total)

with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)
