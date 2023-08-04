n = int(input())
val = list(map(int, input().split()))
val2 = []

for i in range(len(val)):
    if val[i] == 0:
        val2.append(val[i])

for i in range(len(val)):
    if val[i] != 0:
        val2.append(val[i])

print(*val2, end=" ")