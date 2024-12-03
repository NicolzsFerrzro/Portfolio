resultats_tables = []

def demander_nombre_multiplication():
    nombre_a_multiplier = input(f"Entrez un nombre pour lequel vous voulez les tables de multiplications : ")
    try : n=int(nombre_a_multiplier)
    except ValueError:
        print(f"Erreur entrez un nombre ou un chiffre")
        return demander_nombre_multiplication()
    return n

def multiplication_n(n,min, max):
    for i in range(min, max+1):
        r = n * i
        print(f"{n} * {i} = {r}")
        # resultats_tables.append(f"{n} * {i} = {r}")
    

def demander_tables_a_afficher(n):
    min_str = input(f"Affichez les tables de multiplications pour {n} de : ")
    max_str = input(f"à : ")
    try:
        min = int(min_str) 
        max = int(max_str)
        if min > max :
            min, max = max, min   
            # print(f"Erreur impossible d'effectuer les opérations de {min} à {max} pour {n}")
            # return demander_tables_a_afficher(n)
            print(f"Vous voulez dire de {min} à {max} ?")
            return min,max
    except ValueError:
        print(f"Erreur vous devez entrer un nombre ou un chiffre pour la valeur de départ et d'arriver de la table de multiplication de {n}")
        return demander_tables_a_afficher(n)
    return min,max
    
    
def afficher_tables_de_multiplication():
    n=demander_nombre_multiplication()
    min,max=demander_tables_a_afficher(n)
    print(f"Voici les tables de multiplication pour {n} de {min} à {max}")
    multiplication_n(n, min, max)

afficher_tables_de_multiplication()
    
# multiplication_n(4, 1, 19)
# print(resultats_tables)


