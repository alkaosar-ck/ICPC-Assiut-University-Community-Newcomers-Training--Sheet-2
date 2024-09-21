def fac(n):
   r = 1
   for x in range(1,n+1):
      r*=x
   return r
for _ in range(int(input())):
   n = int(input())
   print(fac(n))