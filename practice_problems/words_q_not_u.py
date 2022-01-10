words = []
key_words = []
with open("sowpods.txt") as file:
    for line in file:
        words.append(line)
for word in words:
    if (word.find("Q") != -1) and (word.find("U") == -1):
        key_words.append(word)
print(key_words)