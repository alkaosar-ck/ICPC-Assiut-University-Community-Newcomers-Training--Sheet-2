i = int(input())
count = 0
for x in range(1,i+1):
   if x % 2== 0:
      print(x)
      count+=1
if count == 0:
   print(-1)