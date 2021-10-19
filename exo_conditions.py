temp = input("Fait-il froid? (y/n)")
pluie = " "
if temp == "y":
    pluie = input("Pleut-il? (y/n)")
    
    if pluie == "y":
        print("Prenez un parapluie et un manteau.")
    else:
        print("Prenez une casquette et un manteau.")    
    
else:
    print("Je prend une veste légère.")