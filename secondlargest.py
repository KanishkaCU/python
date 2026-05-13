n = list(map(int,input().split()))
largest = 0
for i in n:
    if i > largest :
        largest = i
n.remove(largest)
s_largest=0
for i in n:
    if i >s_largest:
        s_largest = i
print(s_largest)
