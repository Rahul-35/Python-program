l=[]
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
f=1
g=1
for i in range(1,a+1):
    f=f*i
l.append(str(f))
for j in range(1,b+1):
    g=g*i
l.append(str(g))
print','.join(l)
