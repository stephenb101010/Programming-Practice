#What are all of the words that have a B and an X and are less than 5 letters long?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if (line.find("B") != -1) and (line.find("X") != -1) and (len(line) < 5):
            words.append(line)
print(words)