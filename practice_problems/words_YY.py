words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        end = len(line) - 1
        if (line[0] == "Y") and (line[end] == "Y"):
            words.append(line)
print(words)