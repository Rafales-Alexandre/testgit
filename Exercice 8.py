reponse = input ("repondre oui ou non")
if reponse == "oui" or reponse == "non":
    print(reponse)
else:
    print("the else is a lie")


#3
if len(reponse) == 3:
    print("Il y a 3 caractères")
elif len(reponse) >= 3:
    print("Il y a plus de 3 caractères")
else:
    print("Il y a moins de 3 caractères")