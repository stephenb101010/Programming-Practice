with open("sowpods.txt") as file:
    words = []
    vowels = "AEIOU"
    for line in file:
        line.strip("\n")
        for letter in vowels:
            if line.count(letter) != 1:
                words.append(line)
    #Check to make sure each vowel only appears once
    for word in words:
        if (word.index("A") < word.index("E")) and (word.count("A") == 1) and (word.count("E") == 1):
#            if word.index("E") < word.index("I"):
#                if word.index("I") < word.index("O"):
#                    if word.index("O") < word.index("U"):
                        final_list.append(word)
    print(final_list)