# first_loop = "Hello World !"
# for f in first_loop:
#     second_loop = ["H","E","L","L","O"]
#     for g in second_loop:
#         trirth_loop = {"f1":"h","f2":"E","f3":"L","f4":"L","f5":"O"}
#         for h in trirth_loop:
#             print(h)
#             print(g)
#             print(f)


nmbr = 1000
count = 0
for f in range(nmbr):
    count += 1
    if f == 500:
        print("!!!!!!")
        continue
    else:
        print(count)
        