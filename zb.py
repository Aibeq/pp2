Read=lambda:map(int,input().split())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (abs(a-b))==(abs(c-d)):
   print("YES")
elif (a+b)==(c+d):
  print("YES")
else :
  print("NO")