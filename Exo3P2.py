stock = ["Ordinateur de bureau", "Ordinateur portable", 100, "Camera",310.28,"Haut-parleurs", 27.00, "Television", 1000, "Cartes meres", "souris", "clavier", 500, "barrettes de memoire"] 
# stock_str = ["Ordinateur de bureau", "Ordinateur portable", "Caméra", "Haut-parleurs", "Télévision", "Cartes mères", "souris", "clavier", "barrettes de mémoire"] 
# stock_int = [100, 310.28, 27.00, 1000, 500] 
# print(len(stock_str))
# print(len(stock_int))
# sorted(stock)
# print(stock)
stock_sans_int = [x for x in stock if not isinstance(x,int)]
print(stock_sans_int)
# nombres = []
# first_number = stock[2]
# del stock[2]
# nombres.append(first_number)
# print(stock)
# print(nombres)

# first_number = stock[3]
# del stock[3]
# nombres.append(first_number)
# print(stock)

# first_number = stock[4]
# del stock[4]
# nombres.append(first_number)
# print(stock)

# first_number = stock[5]
# del stock[5]
# nombres.append(first_number)
# print(stock)

# first_number = stock[8]
# del stock[8]
# nombres.append(first_number)
# print(stock)
# print(nombres)

# stock.sort(key=str.lower)
# print(stock)
# stock_str = stock_str.title
# sorted(stock_str)
# print(stock_str)

# stock_str.sort()
# print(stock_str)
