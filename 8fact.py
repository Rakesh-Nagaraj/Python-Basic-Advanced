def fact(n):
    if n < 0:
        return ("give the postive value")
    elif n == 0 or n == 1:
        return (1)
    else:
        fact = 1
        while n != 0:
            fact = fact * n
            n = n - 1
        return (fact)



n = int(input())
print(fact(n))
