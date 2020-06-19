Read=lambda:map(int,input().split())
a,b,c,d=Read()
if a*b>c*d:
  print("Impossible")
  exit()
if b>a:
  c=a
  a=b
  b=c
if d>c:
  c=a
  a=b
  b=c
if c>=a and d>=b:
  print("Thanks, Nurbek")
  exit()
  print("Impossible")