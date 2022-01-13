#Create and print an array containing all of the words that end in "GHTLY"
with open("sowpods.txt") as file:
    words = []
    for line in file:
        line = line.replace("\n", "")
        if (line.endswith("GHTLY") == True):
            words.append(line)
print(words)