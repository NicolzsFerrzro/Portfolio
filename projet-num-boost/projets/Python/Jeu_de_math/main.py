import random


def jeu_de_math(nombre_min, nombre_max):
    a = random.randint(nombre_min, nombre_max)
    b = random.randint(nombre_min, nombre_max)
   
    o = random.randint(0, 3)
    # 0 -> +
    # 1 -> *
    # 2 -> -
    # 3 -> /

    str_operateur = "+"

    if o == 1:
        str_operateur = "*"
    elif o == 2:
        str_operateur = "-"
    
    try: 
        reponse_input = input(f"Calculez : {a} {str_operateur} {b} = ")
        reponse_int = int(reponse_input)
        
        resultat = a + b

        if o == 1:
            resultat = a*b
        elif o == 2:
            resultat = a-b
            
        if reponse_int == resultat :
            return True

        else :
            return False
    except:
        print(f"ERREUR Entrez une valeur numerique")
    return False
    
    
        
def exos_de_math(nb_calculs):
    nb_points = 0
    for i in range(0, nb_calculs):
        num_calcul = i+1
        print(f"Calcul {num_calcul} sur {nb_calculs}")
        if jeu_de_math(1, 10):
            print("Bonne réponse")
            nb_points += 1 
            
        else:
            print("Mauvaise reponse")

    print(f"Votre score est {nb_points}/{nb_calculs}") 
        
    moyenne = int(nb_calculs/2)
    if nb_points == nb_calculs :
        print("Excellent")
    elif nb_points > moyenne : 
        print("Pas mal")
    elif 0 < nb_points < moyenne :
        print("Peut mieux faire")
    else: 
        print("Revisez")




exos_de_math(5)