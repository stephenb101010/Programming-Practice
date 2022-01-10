words = []
key = "UU"
key_words = []
with open("sowpods.txt") as file:
    for line in file:
        words.append(line)
for word in words:
    if word.find(key) != -1:
        key_words.append(word)
print(key_words)