Read=lambda:map(int,input().split())
l,r=Read()
for i in range(l,r):
    if i%7==1 or i%7==2 or i%7==5:
     print(i,end=" ")