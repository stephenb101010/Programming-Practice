with open("sowpods.txt") as file:
    words = []
    for line in file:
        line = line.strip("\n")
        if (line.count("a") == 1): 
            words.append(line)
    print(words)