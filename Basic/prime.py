n=int(input("Enter a number:"))
c=0
for i in range(1,n+1):
    if(n%i)==0:
        c=c+1
if(c==2):
    print('{0} is prime'.format(n))
else:
    print('{0} is not prime'.format(n))
