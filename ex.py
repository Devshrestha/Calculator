a=[1,5,3,6,8,5,4]
y=0
for x in range(len(a)):
    y+=a[x]*(10**x)


print(y)