nmbr = 5
if nmbr == 0:
    print("Le nombre est nul!")
elif nmbr < 0:
    print("Il est negatif!")
else:
    print("Il est positif!")

modulonmbr = nmbr % 2
if modulonmbr == 1:
    print("Il est impaire!")
else:
    print("Il est pair")

a = 3
b = 4
if a < b:
    print(a)
else:
    print(b)

c = 8
d = 6
e = 9
if c < d and c < e:
    print("c est le plus petit")
    if d > e:
        print("e est le plus grand")
    else:
        print("d est le plus grand")
elif d < c and d < e:
    print("d est le plus petit")
    if c > e:
        print("c est le plus grand")
    else:
        print("e est le plus grand")
elif e < d and e < c:
    print("e est le plus petit")
    if d > c:
        print("d est le plus grand")
    else:
        print("c est le plus grand")
else:
    print(" ")

jour = "lundi"
if jour == "lundi":
    print("c'est reparti !")
elif jour == "mercredi":
    print("jour des enfants")
elif jour == "vendredi":
    print("bientôt le week-end")
elif jour == "samedi" or jour == "dimanche":
    print("bon week-end")
else:
    print("bonne semaine")


couleur = "rouge magenta"
if couleur == "rouge magenta" or couleur == "bleu cyan" or couleur == "jaune":
    print("couleur primaires")
elif couleur == "orange" or couleur == "violet" or couleur == "vert":
    print("couleurs secondaires")
else:
    print("autes couleurs")