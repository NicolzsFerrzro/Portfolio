nom_chauffeur = ["Jim", "Jean", "Bo", "Blu", "Pi", "Lu"]
distances_chauffeur = [1.4, 2.5, 0.4, 1.1, 0.8, 1.9]


index_list = []
chauffeur_le_plus_proche = []

def closest_driver():
    index = -1
    distance_min = distances_chauffeur[0]
    for i in distances_chauffeur:
        index += 1
        if i < distance_min :
            distance_min = i
            index_list.append(index)
    linked_name = index_list[0]
    linked_name = nom_chauffeur[linked_name]
    chauffeur_le_plus_proche.append(linked_name)
    chauffeur_le_plus_proche.append(distance_min)
    return chauffeur_le_plus_proche

def afficher_closest_driver():
    driver = chauffeur_le_plus_proche[0]
    distance = chauffeur_le_plus_proche[1]
    print(f"{driver} est le plus proche il est seulement à {distance} km")

closest_driver()
afficher_closest_driver()