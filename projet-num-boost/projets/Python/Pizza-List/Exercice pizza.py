import time
import random

livreur_list = ["bob", "charl", "jam", "pil"] 
pizza_disponible = ["margharita", "calzone", "tri fromaggi", "vegetarienne"]
livreur_dist = ["15","10", "2", "9"]

strdistance_min = livreur_dist[0]
distance_min = int(strdistance_min)
index = 0
for i in livreur_dist:
    distance = int(i)
    if distance < distance_min:
        distance_min=distance
        index +=1
livreur_proche = livreur_list[index]


def temps_livraison(distance, vitesse):
    t_brut = (distance*60)/vitesse
    min = round(t_brut)
    sec = round((t_brut - min)*60)
    
    return min, sec 
   

min, sec = temps_livraison(distance_min,55)
t_sec = ((min*60)+sec)





def list_pizza():
    index=0
    for pizza in pizza_disponible:
        index+=1
        pizza = pizza[0].upper() + pizza[1:len(pizza)].lower()
        print(f"{index} - {pizza}")  

#afficher une liste de 5 pizza 
list_pizza()

#demander choix pizza
choice = input("Enter your choice : ")
client_input = choice.lower()

#si nouvelle pizza non existante dans la liste, l'ajouter à la liste
if client_input in pizza_disponible:
    client_choice = client_input[0].upper() + client_input[1:len(client_input)].lower()
    print(f"Alright your {client_choice} is on is way, {livreur_proche} is {distance_min}km away he will be there in {min} minutes and {sec} secondes ;)")
    # import time reproduire l'exercice des oeufs
   
    while  t_sec != 0 :
        if t_sec >= 10 :
            t_sec -= 10  
            for i in range(0,10):
                time.sleep(1)
                print(".", end="", flush=True)
            print("")
            print(f"{t_sec} secondes restantes avant la livraison")
        elif t_sec < 10 :
             t_sec -= 1
             for i in range(0,t_sec):
                time.sleep(1)
                print(".", end="", flush=True)  
        if t_sec <= 0 :  
                print("") 
                print("You've been delivered, enjoy !")
                break
    
            

if not client_input in pizza_disponible:
    pizza_disponible.append(client_input)
    #afficher la nouvelle liste de pizza
    list_pizza()
    print("Unfortunatly we don't make it but we regist your demand, if lot of people ask same as you the new list could be :")