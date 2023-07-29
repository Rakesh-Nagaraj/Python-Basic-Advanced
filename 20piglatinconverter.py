orginal_word = input().lower().strip()
words = orginal_word.split()
new_word = []
for word in words:
    if word[0] in "aeiou":
        word = word + "yay"
        new_word.append(word)

    else:
        num = 0
        for letter in word:
            if letter not in "aeiou":
                num = num + 1
            else:
                break
        cons = word [:num]
        revs = word [num:]
        new = revs + cons + "ya"
        new_word.append(new)
output = " ".join(new_word)
print(output)