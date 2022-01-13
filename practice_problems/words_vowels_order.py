#What are all of the words that have all 5 vowels, in alphabetical order?
with open("sowpods.txt") as file:
    words = []
    for line in file:
        line = line.strip("\n")
        if (line.count("A") == 1): #and (line.index("a") < line.index("e"))
            if (line.count("E") == 1):
                if (line.count("I") == 1):
                    if (line.count("O") == 1):
                        if (line.count("U") == 1):
                            words.append(line)
    filtered = []
    for entry in words:
        if entry.index("A") < entry.index("E"):
            if entry.index("E") < entry.index("I"):
                if entry.index("I") < entry.index("O"):
                    if entry.index("O") < entry.index("U"):
                        filtered.append(entry)
    print(filtered)