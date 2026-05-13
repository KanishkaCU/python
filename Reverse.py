n = int(input())
sum=0
while(n>0):
    digit=n%10
    sum = sum*10 + digit
    n = n//10
print(sum)