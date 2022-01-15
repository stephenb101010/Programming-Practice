#What are all of the words containing UU?
words = []
key = "UU"
with open("sowpods.txt") as file:
    #words = [line.strip("\n") for line in file if key in line]
    for line in file:
        line = line.strip("\n")
        #line = line.replace("\n", "")
        #if line.find(key) != -1:
        if key in line:
            words.append(line)
print(words)