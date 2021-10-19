a = bool(print(input("a est-il True ou False?")))
if a != True or a != False:
    a = bool(print(input("écrivez True ou False!")))
b = bool(print(input("b est-il True ou False?")))
if b != True or a != False:
    b = bool(print(input("écrivez True ou False!")))

if a == True and b != True:
    print("a est égal à True et b égal à False")
elif a != True or b == True:
    print("a est différent de True ou b est égal à True")

