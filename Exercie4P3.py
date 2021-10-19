x = [27,3339,2345,666]

for i in x :
    if i %9 == 0:
        y = i/9
    else:
        y = i-9

    print(int(y))