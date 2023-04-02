import random
import json
import time

n = int(input("marimea listei="))
start = int(input("cel mai mic elem="))
stop = int(input("cel mai mare="))

nr_de_liste = int(input("numarul de liste dorite="))
lista_numere_aleatorii = []
lista_de_liste = []
while nr_de_liste:
    start_time = time.time()
    while n:
        lista_numere_aleatorii.append(random.randint(start,stop))
        n-=1
    end_time = time.time()

    lista_completa_date = [str(end_time-start_time),lista_numere_aleatorii]
    lista_de_liste.append(lista_completa_date)
    nr_de_liste-=1
with open("random_elem.json", 'w') as json_file:
    json.dump(lista_de_liste, json_file)


print("\n"+ str(end_time-start_time))