d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

d.update({'prenom': "Jacques"})

list_of_key = list(d.keys())
print(list_of_key)

list_of_value = list(d.values())
print(list_of_value)

print(d)
print(d["prenom"],d["nom"], " a ", d["age"]," ans")

print(d.keys())