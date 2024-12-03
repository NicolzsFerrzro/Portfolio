conversion_unit_coef=(
     ("pouces", "cm", 2.54),
        ("cm", "pouces", 0.39)
                    

)

def fonction_choix():
    print("Faites votre choix : ")
    index = 1
    for unit in conversion_unit_coef:
         print(f"{index} - convertir de {unit[0]} à {unit[1]}")
         index += 1
    



def fonction_coef():
    choix_input = input("Entrez votre choix : ")
    try :
        user_choice = int(choix_input)
        user_choice -= 1
        if 0 <= user_choice <= len(conversion_unit_coef)-1:
            choice = conversion_unit_coef[user_choice]
            coef = choice[2]
            return coef, choice
        if not 0 > user_choice > len(conversion_unit_coef):
            print(f"Le choix doit être compris entre 1 et {len(conversion_unit_coef)}")
            return fonction_coef()
    except : 
        print(f"Le choix doit être compris entre 1 et {len(conversion_unit_coef)}")
        return fonction_coef()

        

def fonction_result(coef, choice):
    valeur_input = input(f"Entrez la valeur à convertir de {choice[0]} à {choice[1]} [(q) pour quitter] : ") 
    try:
        if valeur_input == "q":
            return True
        valeur = float(valeur_input)
        round(valeur, 2)
        result = valeur*coef
        print(f"{valeur}{choice[0]} est égale à {round(result, 2)}{choice[1]}")
        return False
    except ValueError : 
        print("Attention ce n'est pas une valeur numérique")
        return fonction_result(coef, choice)


fonction_choix()
coef, choice = fonction_coef()

while True:
    if fonction_result(coef, choice):
        break


# if valeur_input == "q" : 
#         return True


    

# choice = "1"
# while not choice == "":
#     print()
#     choice = input(f"pouce --> cm (1)\ncm --> pouce (2)\nto quit (q): ")
#     if choice == "q":
#             quit()
#     if choice in ["1", "2"]:
#         while True :
#             if fonction("pouce", "cm", 2.54, reverse = False if choice == "1" else True) :
#                 break
#     else : print("Idk this command")