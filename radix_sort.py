import time
import json
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):

    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10



f = open('random_elem.json')
data = json.load(f)
lista_timpuri_ex=[]
start_time_total = time.time()
for elem in data:
	start_time = time.time()
	radixSort(elem[1])
	end_time = time.time()
	lista_timpuri_ex.append(end_time-start_time)
stop_time_total = time.time()

print((stop_time_total-start_time_total)*10)
print(stop_time_total-start_time_total)

with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)