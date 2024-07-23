def Fibounacci(n):
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibounacci(n-1)+Fibounacci(n-2)
    

print(Fibounacci(10))
