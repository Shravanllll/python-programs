a=eval(input())
def fun():
    ans=[]
    for i in a.values():
        if len(a)%2!=0:
            ans+=[i]
    print(ans)
fun()
