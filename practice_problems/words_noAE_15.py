#What are all of the words that have no E or A and are at least 15 letters long?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if (line.find("A") == -1) and (line.find("E") == -1) and (len(line) >= 15):
            words.append(line)
print(words)