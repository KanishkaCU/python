n = list(map(int,input().split()))
freq = {}
for i in n:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)