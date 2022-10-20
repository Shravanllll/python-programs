n = int(input())
sum = 0
i=n
while i>0:
   a=i%10
   sum += a** 3
   i//= 10
if n == sum:
   print("  Armstrong number")
else:
   print(" not Armstrong number")
