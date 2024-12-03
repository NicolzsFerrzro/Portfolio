
'''
def nombre_magic(nombre_min, nombre_max, nombre_essai):
    import random
    nombre_x = random.randint(nombre_min, nombre_max)
    for i in range(0, nombre_essai):
        print(f"Vous avez {nombre_essai-i} essais.")
        try:
            input_nb=input(f"Devinez le nombre mystere compris entre {nombre_min} et {nombre_max} : ")
            int_x = int(input_nb)
            if int_x < nombre_x :
                print(f"Le nombre mystere est superieur à {int_x} ")
            elif nombre_max >= int_x > nombre_x :
                print(f"Le nombre mystere est inferieur à {int_x}") 
            elif int_x == nombre_x :
                print(f"BRAVO {int_x} est le nombre mystere !")
                break
            else :  
               print(f"ERREUR vous devez entrez un nombre valide compris entre {nombre_min} et {nombre_max} !")
        except:
            print(f"ERREUR vous devez entrez un nombre valide compris entre {nombre_min} et {nombre_max} !")        
    if int_x != nombre_x :
            print("Vous n'avez pas trouvé le nombre mystere !")
            print(f"La réponse était {nombre_x}.")

        
nombre_magic(0, 50, 5) 

'''
import random

def devinez_un_nombre(nombre_min, nombre_max, nb_essais):
    nombre_mystere = random.randint(nombre_min, nombre_max)
    int_nombre = 1
    while not int_nombre == nombre_mystere and nb_essais != 0:
        try:
            nombre_inp = input(f"Vous avez droit à {nb_essais} essais. Entrez le nombre mystere compris entre {nombre_min} et {nombre_max} : ")
            int_nombre = int(nombre_inp)
            if int_nombre == nombre_mystere :
                print(f"BRAVO {nombre_mystere} est le nombre mystère !")
            elif nombre_max >= int_nombre > nombre_mystere :
                print(f"Le nombre mystère est inferieur à {int_nombre}.")
                nb_essais = (nb_essais-1) 
            elif nombre_min <= int_nombre < nombre_mystere :
                print(f"Le nombre mystère est supérieur à {int_nombre}.") 
                nb_essais = (nb_essais-1)      
        except:
            print(f"ERREUR vous devez entrer un nombre compris entre {nombre_min} et {nombre_max}")
        else: 
            if nombre_min > int_nombre or nombre_max < int_nombre:
                print(f"ERREUR vous devez entrer un nombre compris entre {nombre_min} et {nombre_max}")
                nb_essais = (nb_essais-1)
            if nb_essais == 0:
                print(f"GAME OVER, Vous n'avez pas trouvé le nombre mystère, la réponse est {nombre_mystere} !")



    



devinez_un_nombre(0, 50, 5)