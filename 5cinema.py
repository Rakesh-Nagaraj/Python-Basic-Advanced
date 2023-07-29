movies = {
    "Master": [3,10],
    "Vikram": [18,14],
    "Leo":[18,20]
}

while True:
    name=input("please enter the movie name").strip().title()
    if name in movies:
        age = int(input("please enter your age"))
        if age > movies[name][0]:
            if movies[name][1]>0:
                print("Here is your ticket, please enjoy your movie")
                movies[name][1] = movies[name][1]-1
                print(movies[name])
            else:
                print("sorry tickets sold out")
        else:
            print("sorry you are not allowed for this movie")
    else:
        print("this movie is not available now")
