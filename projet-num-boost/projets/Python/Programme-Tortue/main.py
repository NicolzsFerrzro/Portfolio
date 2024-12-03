import turtle

turtle.setup(1000, 800, 170, 0)

t = turtle.Turtle()

def escalier():
    nombre_de_marche = 0
    while nombre_de_marche == 0 :
        nombre_de_marche_input = (input("Entrez le nombre de marche : ")) 
        try :
            nombre_de_marche = int(nombre_de_marche_input)
            if nombre_de_marche > 0: 
                try :
                    for i in range(nombre_de_marche):
                        t.forward(10)
                        t.left(90)
                        t.forward(10)
                        t.right(90)
                except: 
                    print("ERREUR entrez une valeur !")
            else:
                print("ERREUR entrez une valeur superieur à 0 !")
        except :
            print("ERREUR entrez une valeur numérique !")
         
def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)

def carre_au_carre(taille, nb):
        for i in range(1, nb):
            carre(i*1*taille)


def carre_de_carre(taille, nb):
        carre_au_carre(taille, nb)
        t.left(90)
        carre_au_carre(taille, nb)
        t.left(90)
        carre_au_carre(taille, nb)
        t.left(90)
        carre_au_carre(taille, nb)
        

'''def carres(taille_carre, nb):
        for i in range(0, nb):
            taille = (i+1)*taille_carre
            carre(taille)'''





#escalier()
#carre(10)
carre_de_carre(5, 10)
#t.right(90)
#t.circle(20, 180)



turtle.done()


