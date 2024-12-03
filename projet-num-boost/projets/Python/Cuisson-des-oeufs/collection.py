import time
import winsound

CHOIX_CUISSON = (
    ("Oeufs à la coque crues", 1*60), 
    ("Oeufs mollets ratés", 30),
    ("Oeufs très très durs", 14*60),
    ("Steak hachés à chier", 12*60 + 25),
    ("Poivrons pas bons", 50),
)

#affichage_temps
def temps_en_seconde(temps):
    min = temps//60
    seconde = temps-min*60
    if min < 1:
        r = f"{seconde:02d} secondes"
    if min == 1 :
        r = f"{min} minute {seconde:02d} secondes"
    if min > 1 :
        r = f"{min} minutes {seconde:02d} secondes"
    return r

# Choix Utilisateur   
def temps_de_cuisson(min, max):
    choice = input(" \n Faites un choix : ")
    try :
        choix_utilisateur = int(choice)
        choice_int = int(choice)
        choix_utilisateur = CHOIX_CUISSON[choice_int-1]
        temps = choix_utilisateur[1]
        print(f"{choix_utilisateur[0]} : {temps_en_seconde(temps)}")

        if min >= choice_int > max :
            print(f"Entrez un choix entre {min} et {max} !")
            return temps_de_cuisson(min, max)
        return temps   
    except :
        print(f"Entrez un choix numérique entre {min} et {max} !")
        return temps_de_cuisson(min, max)

# Cuisson
def cuisson_plat(temps):
    d = temps
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

# index et menu 
index_cuisson = 1
for choix_cuisson in CHOIX_CUISSON:
    print(f"{index_cuisson} - {choix_cuisson[0]} : {temps_en_seconde(choix_cuisson[1])}")
    index_cuisson += 1

# choix et temps associé
t = temps_de_cuisson(index_cuisson-len(CHOIX_CUISSON), len(CHOIX_CUISSON))

# animation et compte à rebours
cuisson_plat(t)





# Cuisson en Fonction du choix
# def temps_choix(choice):
# if choix_int in (1, len(CHOIX_CUISSON)) 
# faire une fonction ou le max serait min = 1 et max = len(CHOIX_CUISSON)



    
        
  
        
        


            # d = int(temps)
            # while not d == 0 :
            #     d -= 10
            #     for i in range (0,10):
            #         time.sleep(1)
            #         print(".", end="", flush=True)
                
            #     min = d//60
            #     seconde = d-min*60
            #     print(f"\nTemps restant : {min}:{seconde:02d}")
            # if d == 0:
            #     winsound.Beep(500, 100)
            #     winsound.Beep(300, 100)
            #     winsound.Beep(700, 100)

    

    

# r = temps_en_seconde
# user_choice(r)


    # int(choice)
    # if choice in CHOIX_CUISSON(1, len(CHOIX_CUISSON)):
    #     print(f"{choix_cuisson[0]}")
    #     cooking_time = choix_cuisson[1]
    # return cooking_time

    # # except : 
    # #         print(" \n Vous devez choisir parmis les choix proposés \n ")
    # #         return user_choice(r)



        # if choice in choix_de_cuisson(1, len(choix_de_cuisson)):

        #     print(f"{choix_de_cuisson[0]}")
        #     cooking_time = 3
           
        #     False
        #     return cooking_time
        # if not choice in choix_de_cuisson :
        #     print(" \n Unknown command try again \n ")
        #     True






