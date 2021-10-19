#1
s = 0
n = 15
for i in range(0, n+1):
    s = s + i
    print(s)


#2
s = 0
n = 16
for i in range(0, n):
    if i%2 == 0:
        s = s + i
    else:
        s = s
    print(s)


# #3
s = 0
n = 16
for i in range(0, n+1):
    if i%2 == 0:
        s = s + i
    else:
        s = s
    print(s)

#4


s=0
n=0
while s<= 1500:
    n+=1
    s = s + n
print(n)

#5
n=5
if n==0:
    print(1)
else:
    f=1
    for k in range(2,n+1):
        f=f*k
        print(f) 