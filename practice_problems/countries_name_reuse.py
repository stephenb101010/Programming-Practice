with open("countries.txt") as file:
    names = []
    final = []
    for line in file:
        line = line.strip("\n")
        line = line.upper()
        names.append(line) 
    length = len(names)
    for name in names:
        i = 1
        while i < length:
            test = names[i]
            if test.find(name) != -1:
                final.append(name)
                final.append(test)
            i += 1
print(final)