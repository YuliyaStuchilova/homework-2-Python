#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input())
sum=0

for i in range(n+1):
    sum=sum+i

print(sum)