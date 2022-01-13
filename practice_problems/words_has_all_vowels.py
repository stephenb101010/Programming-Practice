#What are all of the words that have all 5 vowels, in any order?
with open("sowpods.txt") as file:
    words = []
    for line in file:
        line = line.replace("\n", "")
        if (line.find("A") != -1) and (line.find("E") != -1) and (line.find("I") != -1) and (line.find("O") != -1) and (line.find("U") != -1):
            words.append(line)
print(words)