

def fonction(unit1, unit2, coef, reverse : bool = False):
    valeur_input = input("\nValeur à convertir\n(q to return) : ")
    if valeur_input == "q" : 
         return True
    if reverse == True:
        unit1, unit2 = unit2, unit1
        coef = 1/coef
    try:
        valeur = float(valeur_input)
        print(f"{valeur*coef} {unit2}")
        return False
    except ValueError : 
        print("Numeric only")
    

choice = "1"
while not choice == "":
    print()
    choice = input(f"pouce --> cm (1)\ncm --> pouce (2)\nto quit (q): ")
    if choice == "q":
            quit()
    if choice in ["1", "2"]:
        while True :
            if fonction("pouce", "cm", 2.54, reverse = False if choice == "1" else True) :
                break
    else : print("Idk this command")
        
        
    # if choice =="2":
    #     fonction("pouce", "cm", 2.54, reverse = True)
        
        
    
        
        
       
        


# unit1 = "cm"
# unit2 = "pouce"
# coef1 = 1/2.54
# coef2 = 2.54



# choix1 = str(f"{unit1} -> {unit2}")
# choix2 = str(f"{unit2} -> {unit1}")
# choice = ""
# while not choice == "q":
#     choice = input(f"{choix1} (1)\n{choix2} (2)\nto quit (q): ")
#     if choice in ["1", "2", "q"] :
#         if choice == "q" : quit()   
#         while choice == "1" or "2":
#             valeur_input = input("\nValeur à convertir\n(q to return) : ")
#             if valeur_input == "q" : break
#             else :
#                 try:
#                     valeur = float(valeur_input)
#                     if choice == "1" :
#                         print(f"{valeur*coef1} {unit2}")
                
#                     elif choice == "2" :
#                         print(f"{valeur*coef2} {unit1}")

#                 except ValueError : 
#                     print("Numeric only")
#     else : 
#         print()
#         print("nop idk this command")
#         print()



# def choix_conversion(sens1, sens2) :
#     type_convert = input(f"Souhaitez vous convertir de {sens1} ou {sens2} (press enter to quit) : ")
#     if type_convert == sens1:
#         unite = "cm"
#     elif type_convert == sens2:
#         unite = "pouce"
#     return unite

# def conversion_pouce_cm(unite):
#     if unite == "cm":
#         x = 2.54
#         unite0 = "pouce"
#     elif unite == "pouce":
#         x = 0.394
#         unite0 = "cm"
#     nb_a_convert = input(f"Entrez la valeur à convertir en {unite} (press enter to go back): ")
#     resultat = float(nb_a_convert)*x
#     print(f"{nb_a_convert} {unite0} égale {resultat} {unite}")


# sens1 = "pouce vers cm"
# sens2 = "cm vers pouce"
# type_convert = "1"
# while type_convert == sens1 or sens2:
#     try:
#         unité = choix_conversion(sens1, sens2)
#         nb_a_convert = 1
#         while not nb_a_convert == 0:
#             try:
#                 conversion_pouce_cm(unité)
#             except: break
#     except: quit()
#     if type_convert == "" :
#         quit()







    
# def conversion_pouce_cm():
#     nb_a_convert = input("Entrez la valeur à convertir en cm (press enter to go back): ")  
#     pouces_vers_cm = int(nb_a_convert)*2.54
#     resultat_pouces_cm = float(pouces_vers_cm)
#     print(f"{nb_a_convert} pouces égale {resultat_pouces_cm} cm")

# def conversion_cm_pouce():
#     nb_a_convert = input("Entrez la valeur à convertir en pouces (press enter to go back): ") 
#     cm_vers_pouces = int(nb_a_convert)*0.394
#     resultat_cm_pouces = float(cm_vers_pouces)
#     print(f"{nb_a_convert} cm égale {resultat_cm_pouces} pouces")

# choix1 = "pouce vers cm"
# choix2 = "cm vers pouce"
# type_convert = ""
# while type_convert == choix1 or choix2:
#     try:
#         type_convert = input(f"Souhaitez vous convertir de {choix1} ou {choix2} (press enter to quit) : ")
#         if type_convert == choix1 :
#             nb_a_convert = 1
#             while not nb_a_convert == 0:
#                 try : conversion_pouce_cm()
#                 except : break
                
#         elif type_convert == choix2:
#             nb_a_convert = 1
#             while not nb_a_convert == 0:
#                 try : conversion_cm_pouce()
#                 except : break
#     except:
#         quit()
#     if type_convert == "":
#         quit()




# choix1 = "pouce vers cm"
# choix2 = "cm vers pouce"
# type_convert = ""
# while type_convert == choix1 or choix2 :
#     try:
#         type_convert = input(f"Souhaitez vous convertir de {choix1} ou {choix2} (press enter to quit) : ")
#         if type_convert == choix1 :
#             nb_a_convert = 1
#             while not nb_a_convert == 0 :
#                 try:
#                     nb_a_convert = input("Entrez la valeur à convertir en cm (press enter to go back): ")  
#                     pouces_vers_cm = int(nb_a_convert)*2.54
#                     resultat_pouces_cm = float(pouces_vers_cm)
#                     print(f"{nb_a_convert} pouces égale {resultat_pouces_cm} cm")
#                 except:
#                     break
        
#         elif type_convert == choix2 :
#             nb_a_convert = 1
#             while not nb_a_convert == 0 :
#                 try :
#                     nb_a_convert = input("Entrez la valeur à convertir en pouces (press enter to go back): ") 
#                     cm_vers_pouces = int(nb_a_convert)*0.394
#                     resultat_cm_pouces = float(cm_vers_pouces)
#                     print(f"{nb_a_convert} cm égale {resultat_cm_pouces} pouces")
#                 except : 
#                     break
#     except:
#         quit()
#     if type_convert == "" : 
#         quit()
