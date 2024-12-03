import time
import winsound

def cooking_choice():
    while True : 
        choice=input('''
How your eggs ?

1) Oeufs à la coque : 3 minutes
2) Oeufs mollets : 6 minutes
3) Oeufs durs : 9 minutes
        
Make a choice : ''')
        if choice in ["1", "2", "3"]:
            if choice == "1" :
                print("""
                Oeufs à la coque : 3 minutes""")
                cooking_time = 3
            if choice == "2" :
                print("""
                Oeufs à la coque : 6 minutes""")
                cooking_time = 6
            if choice == "3" :
                print("""
                Oeufs à la coque : 9 minutes""")
                cooking_time = 9
            False
            return cooking_time
        else : 
            print(""" 
            
            /!\ Unknown command try again /!\ """)
            True


def cuisson_oeuf(cooking_time):
    d = cooking_time*60
    while not d == 0 :
        d -= 10
        for i in range (0,10):
            time.sleep(1)
            print(".", end="", flush=True)
        
        min = d//60
        seconde = d-min*60
        print(f"\nTemps restant : {min}:{seconde:02d}")
    if d == 0:
        winsound.Beep(500, 100)
        winsound.Beep(300, 100)
        winsound.Beep(700, 100)
        
        print("""
        
        Cuisson terminée """) 

cooking_time=cooking_choice()
cuisson_oeuf(cooking_time)

      

    

    
    




# -> Votre programme proposera 3 options :
# - Oeufs à la coque : 3 minutes
# - Oeufs mollets : 6 minutes
# - Oeufs durs : 9 minutes



# Une fois l'option choisie, votre programme commencera à attendre la durée concernée.
# A chaque seconde, vous afficherez un "." sur une même ligne (afin que l'on voit un effet de progression).
# Et toutes les 10 secondes vous irez à la ligne suivante en affichant le temps restant.






# Exemple:

# ..........

# Temps restant : 2:50..........

# Temps restant : 2:40.....

# (voir la vidéo ci-dessus pour avoir une illustration)



# Quand le temps est écoulé, vous afficherez "Cuisson terminée", et votre programme se terminera.

# BONUS : Vous pourrez aussi jouer un son une fois la cuisson terminée



# NOTION SUPPLÉMENTAIRES

# Pour réaliser ce programme vous aurez besoin des notion supplémentaires suivantes :



# -> Bloquer le programme pendant 1 seconde :

# import time
# time.sleep(1)


# -> Afficher un point sans aller à la ligne :

# print(".", end="", flush=True)


# -> Boucler 5 secondes et afficher un "." à chaque seconde :

# for i in range(5):
#     time.sleep(1)
#     print(".", end="", flush=True)


# -> Convertir la durée "d" en secondes, en minutes/secondes :

# d = 100
# min = d//60 # division entière (pas de virgules)
# sec = d-min*60


# -> Afficher un nombre avec 2 chiffres complétés par un "0" (si nécessaire) :

# print(f"{min:02d}")






