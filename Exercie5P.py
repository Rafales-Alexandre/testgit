stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Camera",310.28,"Haut-parleurs", 27.00, "Television", 1000, "Cartes meres", "souris", "clavier", 500, "barrettes de memoire"] 

stock_str= [x for x in stock if not isinstance(x,(int,float))]
print(stock_str)

stock_int_float= [x for x in stock if not isinstance(x,str)]
print(stock_int_float)

#peut etre fait en utilisant le systeme de class
# stock_number = set(stock) - set(stock_str)
# print(stock_number)


