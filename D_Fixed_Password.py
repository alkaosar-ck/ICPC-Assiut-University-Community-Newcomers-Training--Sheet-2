import sys
n = []
for line in sys.stdin:
   n.append(int(line.strip()))
for x in n:
   if x == 1999:
      print('Correct')
      break
   else:
      print('Wrong')