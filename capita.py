a=eval(input())
H=''
for i in a:
    if 'A'<=i<='Z':
        H+=chr(ord(i)+32)

    elif 'a'<=i<='z':
        H+=chr(ord(i)-32)
    else:
        H+=i
print(H)
