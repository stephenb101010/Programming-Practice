#What are all of the words containing a Q but not a U?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if (line.find("Q") != -1) and (line.find("U") == -1):
            words.append(line)
print(words)