#What is the shortest word that contains all 5 vowels?
with open("sowpods.txt") as file:
    shortest = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    for line in file:
        line = line.replace("\n", "")
        if (line.find("A") != -1) and (line.find("E") != -1) and (line.find("I") != -1) and (line.find("O") != -1) and (line.find("U") != -1):
            if len(line) < len(shortest):
                shortest = line
print(shortest)