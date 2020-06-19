Read=lambda:map(int,input().split())
n,=Read()
last=n%10
sum=0
while n>0:
  sum+=n%10
  n=n//10
if sum%last>0:
 print("No")
else:
 print("Yes")