#What are all of the words containing an X and a Y and a Z?
words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if (line.find("X") != -1) and (line.find("Y") != -1) and (line.find("Z") != -1):
            words.append(line)
print(words)