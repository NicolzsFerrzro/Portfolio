import random

paquet_de_carte = ["♣A♣", "♥A♥","♠A♠","♦A♦",
                "♣K♣", "♥K♥","♠K♠","♦K♦", 
                "♣Q♣", "♥Q♥","♠Q♠","♦Q♦",
                "♣J♣", "♥J♥","♠J♠","♦J♦",
                "♣10♣", "♥10♥","♠10♠","♦10♦",
                "♣9♣", "♥9♥","♠9♠","♦9♦",
                "♣8♣", "♥8♥","♠8♠","♦8♦",
                "♣7♣", "♥7♥","♠7♠","♦7♦",
                "♣6♣", "♥6♥","♠6♠","♦6♦", 
                "♣5♣", "♥5♥","♠5♠","♦5♦",
                "♣4♣", "♥4♥","♠4♠","♦4♦",
                "♣3♣", "♥3♥","♠3♠","♦3♦",
                "♣2♣", "♥2♥","♠2♠","♦2♦"]

# Cartes triées par valeur
les_as = ["♣A♣", "♥A♥","♠A♠","♦A♦"]
les_rois = ["♣K♣", "♥K♥","♠K♠","♦K♦"] 
les_dames = ["♣Q♣", "♥Q♥","♠Q♠","♦Q♦"] 
les_valets = ["♣J♣", "♥J♥","♠J♠","♦J♦"] 
les_dix = ["♣10♣", "♥10♥","♠10♠","♦10♦"] 
les_neufs = ["♣9♣", "♥9♥","♠9♠","♦9♦"] 
les_huits = ["♣8♣", "♥8♥","♠8♠","♦8♦"] 
les_septs = ["♣7♣", "♥7♥","♠7♠","♦7♦"] 
les_six = ["♣6♣", "♥6♥","♠6♠","♦6♦"] 
les_cinq = ["♣5♣", "♥5♥","♠5♠","♦5♦"] 
les_quatres = ["♣4♣", "♥4♥","♠4♠","♦4♦"] 
les_trois = ["♣3♣", "♥3♥","♠3♠","♦3♦"] 
les_deux = ["♣2♣", "♥2♥","♠2♠","♦2♦"] 

 # mettre ca dans la fonction 1 et tester en rempacant par valeur_main

# Tirer une nouvelle carte
def nouvelle_carte():
    carte = random.choice(paquet_de_carte)
    paquet_de_carte.remove(carte)
    print(carte)
    return carte

def valeur_des_cartes(carte):
    if carte in les_deux:
        valeur_carte = 2
    if carte in les_trois:
        valeur_carte = 3
    if carte in les_quatres:
        valeur_carte = 4
    if carte in les_cinq:
        valeur_carte = 5
    if carte in les_six:
        valeur_carte = 6
    if carte in les_septs:
        valeur_carte = 7
    if carte in les_huits:
        valeur_carte = 8
    if carte in les_neufs:
        valeur_carte = 9
    if carte in les_dix:
        valeur_carte = 10
    if carte in les_valets:
        valeur_carte = 10
    if carte in les_dames:
        valeur_carte = 10
    if carte in les_rois:
        valeur_carte = 10
    if carte in les_as:
        valeur_carte = 11
    return valeur_carte

def boucle_carte():
    carte1 = nouvelle_carte()
    carte2 = nouvelle_carte()
    valeur_carte1 = valeur_des_cartes(carte1)
    valeur_carte2 = valeur_des_cartes(carte2)
    Valeur_main = valeur_carte1 + valeur_carte2
    if Valeur_main == 21:
        print(f"Vous avez {Valeur_main} Black Jack !")
    else:
        print(f"Vous avez {Valeur_main}")
    while not Valeur_main == 21:
        choix_input = input("Voulez vous une autre carte ? oui / non : ")
        choix_yes = ["oui", "y", "yes"]
        choix_no = ["non", "n", "no"]
        if choix_input in choix_yes:
            carte = nouvelle_carte()
            if carte in les_as and Valeur_main >= 11:
                valeur_carte = 1
            else :
                valeur_carte = valeur_des_cartes(carte)
            Valeur_main += valeur_carte
            print(Valeur_main)
            if Valeur_main > 21:
                print(f"{Valeur_main} ! Vous avez Perdu !")
                quit()
            elif Valeur_main == 21:
                print(f"{Valeur_main} ! Black Jack !")
                quit()
        if choix_input in choix_no:
            break
    return Valeur_main
    
def boucle_carte_bot():
    carte1 = nouvelle_carte()
    carte2 = nouvelle_carte()
    valeur_carte1 = valeur_des_cartes(carte1)
    valeur_carte2 = valeur_des_cartes(carte2)
    Valeur_main = valeur_carte1 + valeur_carte2
    print(Valeur_main)
    while not Valeur_main == 21:
        if Valeur_main < 16 :
            carte = nouvelle_carte()
            if carte in les_as and Valeur_main >= 11:
                valeur_carte = 1
            else :
                valeur_carte = valeur_des_cartes(carte)
            Valeur_main += valeur_carte
            print(Valeur_main)
            
            if Valeur_main > 21:
                print(f"{Valeur_main} ! La banque a Perdu !")
                break
            elif Valeur_main == 21:
                print(f"{Valeur_main} ! Black Jack !")
                break
        else :
            break
    return Valeur_main


valeur_main = boucle_carte()

# programmer un pattern de jeu jouer contre un bot et remplacer 16 par tirage aléatoire

valeur_main_bot = boucle_carte_bot()

# ameliorer si black jack fin du game fonction end of programm ? 

if 21 > valeur_main > valeur_main_bot:
    print(f"{valeur_main} contre {valeur_main_bot} Vous battez la banque !")
elif 21 > valeur_main_bot > valeur_main :
    print(f"{valeur_main_bot} contre {valeur_main}. La banque gagne !")
    


        




       
            


#valeur_main_deux_carte = distribution_deux_cartes(valeur_main)

#if valeur_main_deux_carte > 21:
    #print("La banque gagne")
    
#elif valeur_main_deux_carte == 21:
    #print("Black Jack !")
    
#else : nouvelle_carte(valeur_main_deux_carte)




    
#valeur_main_trois_cartes = nouvelle_carte(valeur_main_deux_carte)
#comparaison_main(valeur_main_trois_cartes)






    















