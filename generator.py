import random
import json
import time

n = int(input("marimea listei="))
start = int(input("cel mai mic elem="))
stop = int(input("cel mai mare="))
lista_numere_aleatorii = []

start_time = time.time()
while n:
    lista_numere_aleatorii.append(random.randint(start,stop))
    n-=1

end_time = time.time()

lista_completa_date = [str(end_time-start_time),lista_numere_aleatorii]

with open("random_elem.json", 'w') as json_file:
    json.dump(lista_completa_date, json_file)


print("\n"+ str(end_time-start_time))