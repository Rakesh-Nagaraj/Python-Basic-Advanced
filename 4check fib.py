val = int(input())
c = 0
a = 1
b = 1

if val == 1 or val == 0:
    print("True")
else:
    while val > c:
        c = a+b
        b = a
        a = c
    if c == val:
        print("True")
    else:
        print("False")