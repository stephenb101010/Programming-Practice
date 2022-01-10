words = []
key_words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        words.append(line)
for word in words:
    if (word.find("X") != -1) and (word.find("Y") != -1) and (word.find("Z") != -1):
        key_words.append(word)
print(key_words)