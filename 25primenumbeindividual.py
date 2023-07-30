val = int(input())

for i in range(2,val):
        if (val % i == 0):
            print("the given number is not a prime number")
            print(i)
            print(val)
            break
else:
    print("the given number {} is a prime number".format(val))