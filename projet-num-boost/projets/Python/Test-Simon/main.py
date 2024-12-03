# 0 - Générer une chaine de caractère qui contient 4 chiffres aléatoires, c'est votre séquence initiale.

# 1 - Ajouter un nouveau nombre aléatoire à la fin de votre séquence

# 2 - Nettoyer l'écran et affichez "Retenez la séquence" pendant 1 seconde

# 3 - Afficher la séquence à mémoriser pendant 3 secondes

# 4 - Nettoyer n'écran et demander la réponse à l'utilisateur

# 5 - Si la réponse est bonne, afficher pendant 1 seconde "Bonne réponse, votre score est : xxx", puis reboucler à l'étape 1

# 5bis - Si la réponse n'est pas bonne, sortir du programme et afficher : "Mauvaise réponse, la séquence était : xxxx, votre score final : xxxx"

import time
import random
import os
 
def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
# gener un nombre au hasard à 5 chiffre

def séquence():
    s=""
    for i in range(0,4):
        n = random.randint(0, 9)
        s += str(n)
    return s

points = 0      
s=séquence()
while True : 
    
    print("Retenez la séquence : ")
    time.sleep(1)
    n = random.randint(0, 9)
    s += str(n)
    print(s)
    time.sleep(3)
    clear_screen()

    reponse_s = input("Quelle était la séquence : ")

    if reponse_s != s: 
        break
             
    if reponse_s == s : 
        points += 1
        for i in range(0,1):
            print(f"\nBonne réponse, votre score est : {points}")
            time.sleep(3)
            clear_screen()
        True

print(f"\nMauvaise réponse, la séquence était : {s}, votre score final : {points}")     


