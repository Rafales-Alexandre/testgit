# liste = ["orange", "fraise", "pomme", "abricot"]
# print(liste)
# print(type(liste))

# liste.append("kiwi")
# print(liste)

# liste.remove("pomme")
# print(liste)

# nliste = ["choux", "tomates"]

# liste = nliste[:]

# print(liste,nliste)

# liste.append("framboise")

# print(liste,nliste)

# print(liste[0])

# del liste[1]
# print(liste)

# print(len(liste))

#transformer list en string
# string = ";".join(liste)
# print(string)
# print(type(string))

#transformer string en list
# liste2 = string.split(";")

# print(liste2)
# print(type(liste2))

# print(liste2[-1:])


var = (1, 2)
var = list(var)
var.append(3)
var.append(4)
var = tuple(var)

print(var)
print(type(var))