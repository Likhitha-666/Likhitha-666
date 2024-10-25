n=input()
ans=0
for i in range(len(n)-1):
    temp=abs(ord(n[i]+n[i+1]))
    ans+=i
print(ans)    
    
