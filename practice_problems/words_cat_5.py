words = []
key_words = []
with open("sowpods.txt") as file:
    for line in file:
        line = line.replace("\n", "")
        words.append(line)
for word in words:
    if (word.find("CAT") != -1) and (len(word) == 5):
        key_words.append(word)
print(key_words)