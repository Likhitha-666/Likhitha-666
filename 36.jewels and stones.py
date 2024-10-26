jewels="aabbcd"
stones="abba"
count=0
for i in jewels:
    for j in stones:
        if i==j:
            count+=1
            break
print(count)
