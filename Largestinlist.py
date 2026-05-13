n = list(map(int,input().split()))
largest = 0
for i in n:
    if i>largest:
        largest = i
print(largest)