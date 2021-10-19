#On definit la fonction jour de la semaine

def jours_de_la_semaine(jdls):
    if jdls == "lundi" or jdls == "mardi":
        return "Bon début de semaine!"
    elif jdls == "mercredi":
        return "Plus que la moitié!"
    elif jdls == "jeudi" or jdls == "vendredi":
        return "On en arrive au bout!"
    elif jdls == "samedi" or jdls == "dimanche":
        return "Bon week-end!"
    else:
        return "Ce n'est pas un jour de la semaine!"

# print(jours_de_la_semaine(str(input('jour?'))))
