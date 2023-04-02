import time
import json
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        swapped = False
        for i in range (start, end):
            if (a[i] > a[i+1]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True
 
        if (swapped==False):
            break

        swapped = False
 
        end = end-1

        for i in range(end-1, start-1,-1):
            if (a[i] > a[i+1]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        start = start+1
 





f = open('random_elem.json')
data = json.load(f)
lista_timpuri_ex=[]
start_time_total = time.time()
for elem in data:
	start_time = time.time()
	cocktailSort(elem[1])
	end_time = time.time()
	lista_timpuri_ex.append(end_time-start_time)
stop_time_total = time.time()

print((stop_time_total-start_time_total)*10)
print(stop_time_total-start_time_total)

with open("lista_timpuri_ex.json", 'w') as json_file:
    json.dump(lista_timpuri_ex, json_file)