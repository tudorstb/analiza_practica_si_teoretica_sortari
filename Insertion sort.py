import time
import json
def insertionSort(arr):
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key

f = open('random_elem.json')
data = json.load(f)
lista_timpuri_ex=[]

# start_time_total = time.time()

# for elem in data:
# 	start_time = time.time()
# 	insertionSort(elem[1])
# 	end_time = time.time()
	
# 	lista_timpuri_ex.append(end_time-start_time)

# stop_time_total = time.time()

# print(stop_time_total-start_time_total)
print(222.5555636882782*10)
with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)

