vol = 0
cons = 0
for i in input().lower():
    if i in "aeiou":
        vol = vol + 1
    elif i == " ":
        pass
    else:
        cons = cons + 1
print ("the no.of vowles in given word is {}".format(vol))
print ("the no.of const in give word is {}".format(cons))