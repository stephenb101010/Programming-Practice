with open("sowpods.txt") as file:
    words = []
    final_list = []
    for line in file:
        line = line.replace("\n", "")
        if (line.find("A") != -1) and (line.find("E") != -1) and (line.find("I") != -1) and (line.find("O") != -1) and (line.find("U") != -1):
            words.append(line)
    for word in words:
        if word.index("A") < word.index("E"):
            if word.index("E") < word.index("I"):
                if word.index("I") < word.index("O"):
                    if word.index("O") < word.index("U"):
                        final_list.append(word)
    print(final_list)