vow = 0
cons = 0
val = input().lower()
n = int(len(val))
for i in val:
    if i.lower() in "aeiou" :
        vow = vow + 1
    elif val ==  " ":
        pass
    else:
        cons = cons + 1
print("the value of vowel is: {}".format(vow))
print("the value of cons is: {}".format(cons))
