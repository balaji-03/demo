def fact(n):
    
    if n>1 :
        return n*fact(n-1)
    elif n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return
n=int(input("Enter the number"))
print("Factorial of %d is "%n,fact(n))