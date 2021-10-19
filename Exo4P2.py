#False car numlist n'est pas alphalist
#False car numplis n'est pas égale à alphalist
#True numlist et alphalist sont devenu la meme variable
#True ils sont donc égaux




numlist = [1,2,3,4,5]
alphalist = ["a","b","c","d","e"]
print(numlist is alphalist)
print(numlist == alphalist)
numlist = alphalist
print(numlist is alphalist)
print(numlist == alphalist)