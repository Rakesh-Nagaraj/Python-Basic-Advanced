def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
    return (n)


def armstrong(x):
    n = order(x)
    temp = x
    sum = 0

    while temp !=0:
        r = temp % 10
        sum = sum + pow(r,n)
        temp = temp // 10

    return (sum == x)

x = int(input())
print(armstrong(x))
