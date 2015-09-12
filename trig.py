def t(n):
    return n*(n+1)/2

def divisors(n):
    counter = 0
    for i in range(n):
        if(n%(i+1)==0):
            counter += 1
    return counter

n=1
while(divisors(t(n))<=500):
    n+=1
print t(n)
