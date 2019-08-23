n=int(input("Enter a given number: "))
m=n
d=0
s=0
while (n>0):
    d=n%10
    s=s*10+d
    n=n/10
print('The Reverse of the Number {0} is : {1} '.format(m,s))

