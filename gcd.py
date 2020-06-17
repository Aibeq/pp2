def gcd(a,b):
 if b==0:
  return a
 else:
  return gcd(b,a%b)
Read=lambda:map(int,input().split())
a,b=Read();
print(gcd(a,b)+a*b//gcd(a,b))