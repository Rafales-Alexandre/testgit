var = "programmation"

lvar = var[:5]
print(lvar)
dvar = var [-2:]
print(dvar)
cvar = var [3:8]
print(cvar)

count = 0
for i in var :
    if i == "a":
        count += 1
        print(count)

countz = 0
countt = 0
for i in var:
    if i == "z":
        countz += 1
        print(f"il y a {countz} z")
    elif i == "t":
        countt += 1
        print(f"il y a {countt} t")