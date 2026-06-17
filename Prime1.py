# prime count
""" num = int(input())

count = 0

for n in range(2,num+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        count=count+1
    
print(count) """

# sum of digits

""" num =input()
count = 0
for digit in num:
    count = count+int(digit)
print(count) """

#largest of 3 number

#odd/even
n = int(input())
ecount=0
ocount=0
for num in range(1,n+1):
   
    if num%2==0:
        ecount=ecount+1          
    else:
        ocount=ocount+1
print(ecount,ocount)

