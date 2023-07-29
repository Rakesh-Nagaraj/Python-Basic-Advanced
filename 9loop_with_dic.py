dic = {
    "Male" : ["Hunt", "Rakesh", "John" , "Rohith" , "Visvak" ],
    "Female" : ["Mathu", "Jeniliya", "godot"]
}

for val in dic.keys():
    for names in dic[val]:
        if "a" in names :
            print(names)