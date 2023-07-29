from random import choice
list = ["why are you doing that",
        "why don't you ask anything",
        "Outperform everyone"]

ques = choice(list)
answer = input(ques).strip().lower()
while answer != "just because":
    answer = input("why").strip().lower()
print("ohhh I see!")