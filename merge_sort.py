import json
import time

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]
 
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        i = j = k = 0
 
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1
 
        
        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1
 
        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1
 
f = open('random_elem.json')
data = json.load(f)

start_time = time.time()
mergeSort(data[1])
end_time = time.time()

print((end_time-start_time)*10)
print("\n"+ str(end_time-start_time))