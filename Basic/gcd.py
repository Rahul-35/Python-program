def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n==0:
        return(n)
    else:
        return(gcd(n,m%n))
print('The gcd of two numbers {0} and {1} is : {2} '.format(8,12,gcd(8,12)))
