def fibonacci(n):
    if n==0:
        return (0)
    elif n==1:
        return(1)
    else:
        f=fibonacci(n-1) + fibonacci(n-2)
        return(f)
a= fibonacci(34)    
print(a)
password=46
