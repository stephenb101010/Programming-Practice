#What are all of the words that contain the word CAT and are exactly 5 letters long?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if (line.find("CAT") != -1) and (len(line) == 5):
            words.append(line)
print(words)