n, m = int(input()), int(input())
res = []
for i in range(n, m + 1):
   for j in range(2, i):
       if not i % j:
           break
   else:
       res.append(i)
print(*res)

for i in range(1, 11):
   for j in range(1, 11):
       print(f'{i} * {j} = {i * j}')
   print()

   n, m = int(input()), int(input())
   for i in range(n, m + 1):
       for j in range(1, 11):
           print(f'{i} * {j} = {i * j}')
       print()