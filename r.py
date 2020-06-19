Read=lambda:map(int,input().split())
n,=Read()
for i in range(1,100000):
 n-=i
 if n<=0:
  print("Bob")
  break
 n-=i*2
 if n<=0:
  print("Nelson")
  break