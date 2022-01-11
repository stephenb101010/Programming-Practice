with open("sowpods.txt") as words:
    reversed_words = []
    for word in words:
        word = word.strip("\n")
        rev_word = word[::-1]
        reversed_words.append(rev_word)
with open("baby_names_2020_short.txt") as names:
    matches = []
    for name in names:
        name = name.strip("\n").upper()
        for word in reversed_words:
            if name == word:
                matches.append(name)
print(matches)