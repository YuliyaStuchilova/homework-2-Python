# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input())

for i in range(1, n+1):
    if n % i == 0 and i != 1:
        print(i)
        break
