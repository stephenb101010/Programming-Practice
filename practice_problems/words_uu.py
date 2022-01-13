#What are all of the words containing UU?
words = []
key = "UU"
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        if line.find(key) != -1:
            words.append(line)
print(words)