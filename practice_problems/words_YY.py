#What are all of the words that start and end with a Y?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        end = len(line) - 1
        if (line[0] == "Y") and (line[-1] == "Y"):
            #Could also use startswith and endswith
            words.append(line)
print(words)