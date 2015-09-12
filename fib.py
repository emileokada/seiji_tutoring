fib_array = [0,1]

def fib(n):
    if len(fib_array)<n+1:
        while len(fib_array)<n+1:
            fib_array.append(fib_array[-1]+fib_array[-2])
    return fib_array[n]
    
n=1
fib_sum = 0
while fib(n) <= 4000000:
    if (fib(n)%2==0):
        fib_sum += fib(n)
    n+=1

print fib_sum
