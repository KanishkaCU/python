n = int(input())
original = n
sum = 0
power = len(str(n))
while n>0:
    digit = n%10
    sum = sum + digit**power
    n=n//10
if original == sum :
    print("yes")
else:
    print("no")