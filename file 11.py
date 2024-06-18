def fibonacci(n):
    if(n==1 or n==2):
        return 1
    else:
        fibo=fibonacci(n-1)+fibonacci(n-2)
        return fibo
    
count = 1
while count <= number:
 print(fibonacci(count), end=" ")
 count+=1