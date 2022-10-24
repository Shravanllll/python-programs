a=eval(input())
d={}
r,ans='',''
for i in a:
    if i in d and i!=' ':
        l=d[i]
        d[i]=l+1
    elif i!=' ':
        d[i]=1
small=999
for i in d:
    if d[i]<=small:
        small=d[i]
        ans=i
print(ans)
