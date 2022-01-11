import re

with open("sowpods.txt") as file:
    words = []
    for line in file:
        line = line.strip("\n")
        if re.search("[^aeiou]*a[^aeiou]*e[^aeiou]*i[^aeiou]*o[^aeiou]*u[^aeiou]*", line) != None:
        #This doesn't work here. In terminal it almost does.
            words.append(line)
    print(words)