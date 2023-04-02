import json
import time
def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


f = open('random_elem.json')
data = json.load(f)

lista_timpuri_ex=[]

start_time_total = time.time()

for elem in data:
	start_time = time.time()
	size = len(elem[1])
	shellSort(elem[1], size)
	end_time = time.time()
	
	lista_timpuri_ex.append(end_time-start_time)

stop_time_total = time.time()

print((stop_time_total-start_time_total)*10)
print(stop_time_total-start_time_total)

with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)

