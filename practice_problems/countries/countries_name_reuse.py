with open("countries.txt") as file:
    names = []
    final = []
    for line in file:
        line = line.strip("\n")
        line = line.upper()
        names.append(line) 
    length = len(names)
    for name in names: