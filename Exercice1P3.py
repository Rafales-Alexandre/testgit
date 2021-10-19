#1
liste_nombres = [10,500,60.56,80,78.90,500]

def somme_éléments_list_nombrs(liste):
    somme = 0
    for i in range(0, len(liste)):
            somme = somme + liste[i]
    return somme

somme_éléments_list_nombrs(liste_nombres)

#2
# def moyenne_somme_éléments_list_nombrs(liste):
#     somme = 0
#     moyenne = 0
#     for i in range(0, len(liste)):
#             somme = somme + liste[i]
#             moyenne = somme / len(liste) 
#     print(moyenne)

# moyenne_somme_éléments_list_nombrs(liste_nombres)

# #3#4 il renvoie l'indice le plus petit
# def maximum_élément_list_nombrs(liste):
#     max = 0
#     for num in liste:
#         if  num > max:
#             max = num
#     print(max)
#     print(liste.index(max))

# maximum_élément_list_nombrs(liste_nombres)

# #5
# def nmbr_caractere(phrase):
#     count=0
#     phrase = ""
#     somme = 0
#     for i  in phrase:
#         if i == "a":
#             count +=1
#             somme = somme + count
#             print(count)

# ph = "concatenation"
# nmbr_caractere(ph)

# #6
# def élément_positif_ou_nul(liste):
#     for i in liste:
#         if i ==0 or i>=0:
#             print("we good")
#         else:
#             print('ERREUR')

# élément_positif_ou_nul(liste_nombres)

# #7      
# def test_croissant(liste):
#     for i in range(0,len(liste)-1):
#         if not liste[i] <= liste[i+1]:
#             return False 
#     return True
    
# print(test_croissant(liste_nombres))
    