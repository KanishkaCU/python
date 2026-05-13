n = int(input("Enter a number: "))
if n<=1:
    print(n,"Not a prime number")
else:
    is_prime = True 
    i=2
    while n > i:
        if n%i==0:
            is_prime=False
        i=i+1
if is_prime:
    print("yes")
else:
    print("no")
        