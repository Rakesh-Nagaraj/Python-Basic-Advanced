n = int(input())
val = list(map(int,input().split()))
req = list(map(int,input().split()))
for i in range (n):
    for j in range (int(len(req))):
        if val[i] == req[j] :
            print("Element {} index = {}".format(1, i))
else:
    print("Element {} index = {}".format(2, -1))