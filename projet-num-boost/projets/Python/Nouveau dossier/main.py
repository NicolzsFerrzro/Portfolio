italie_city ="Rome","Naples","Turin","Bologne"
france_city = "Paris","Marseille","Lyon","Bordeaux"
espagne_city = "Madrid","Valence","Barcelone","Séville"
allemagne_city = "Berlin","Stuttgarth","Francfort","Munich"


import random

def random_list(villes):
    random_list = random.sample(villes, len(villes))
    return random_list
    

def question(pays, villes, numero_question):
    
    
    if pays[0] in ["i","I","e","E","a","A","o", "O", "u", "U"] :
        pronom = "l'" 
    if pays in ["France", "france"]:
        pronom = "la "
    print(f"Question {numero_question} - Quelle est la capitale de {pronom}{pays} ?")
    random_list_city = random_list(villes)
    for i in range(0,4):
        print(random_list_city[i])
    return villes
    
def reponse(villes, points):
    capitale = villes[0]
    answer_str = input("Votre réponse : ")
    if answer_str == "":
        print("Il semblerait que vous ayez fait une mauvaise manipulation")
        return reponse(villes, points)# ne renvoit aucune valeur

    if answer_str.lower() == capitale.lower() :
        print("Bonne réponse")
        points += 1
        
    else:
        print("Mauvaise réponse")
    return points


# points=0

# # Question 1 : Espagne
# question("Espagne",espagne_city, 1)
# points = reponse(espagne_city,points)

# # Question 2 : Italie
# question("Italie",italie_city, 2)
# points = reponse(italie_city,points)

# # Qestion 3 : France
# question("France",france_city, 3)
# points = reponse(france_city,points)

# # Question 4 : Allemagne
# question("Allemagne",allemagne_city, 4)
# points = reponse(allemagne_city,points)

# print(f"Vous avez {points} points sur 4")


list_pays = (
("Espagne", espagne_city),
("Italie", italie_city),
("France", france_city),
("Allemagne", allemagne_city)
)

def create_random_qcm(nombre_de_question):
    points = 0
    new_list_pays = random_list(list_pays)
    for i in range(0, nombre_de_question):
        pays = new_list_pays[i][0]
        villes = new_list_pays[i][1]
        question(pays,villes, i+1)
        points = reponse(villes,points)
    if interpretation_result(nombre_de_question,points):
        return create_random_qcm(nombre_de_question)

def interpretation_result(nombre_de_question,points):
    score_pc = round(points/nombre_de_question*100)
    print(f"Vous avez {points} réponses correctes sur un total de {nombre_de_question} questions") 
    print(f"soit {score_pc}% de réussite")
    if score_pc >= 70 :
        print("Bravo, les connaissances sont acquises")
        return False
    else:
        print("Malheureusement, les connaissances ne sont pas acquises")
        relunch = input("Voulez vous relancer le QCM ? [y/n] : ")
        if relunch == "y":
            return True
        


create_random_qcm(4)




       
        
        

 