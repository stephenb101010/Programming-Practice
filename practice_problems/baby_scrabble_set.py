with open("sowpods.txt") as words, open("baby_names_2020_short.txt") as names:
    reversed_words = set()
    names_set = set()
    for word in words:
        word = word.strip("\n")
        rev_word = word[::-1]
        reversed_words.add(rev_word)    
    for name in names:
        name = name.strip("\n") #This works
        upper_name = name.upper() #This works
        names_set.add(upper_name) #This works
matches = reversed_words.intersection_update(names_set)
print(matches)