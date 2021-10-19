#1
def supprimeDoublon(liste):
    liste = liste
    newliste = []
    for i in liste:
        if i not in newliste:
            newliste.append(i)
    
    print(newliste)



#2
listetest = [3,4,5,3,4,5,1]

supprimeDoublon(listetest)