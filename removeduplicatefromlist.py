n = list(map(int,input().split()))
nn=[]
for i in n:
    if i not in nn:
        nn.append(i)
print(nn)

