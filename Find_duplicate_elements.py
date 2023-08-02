n = int (input())
val = list(map(int, input().split()))
for con in range (n):
    for var in range (con+1, n):
        if val[con] == val[var]:
            print(val[con])