#Définition du signe.

def signe(nmbr):
    if nmbr == 0:
        return "Il est nul"
    elif nmbr > 0:
        return "Il est positif"
    else:
        return "Il es négatif"

#Définition de la parité.

def parité(nmbr):
    if nmbr %2 == 0:
        return "Il est pair"
    else:
        return "Il est impair"

def appel(nmbr):
    print(signe(nmbr),"et",parité(nmbr))