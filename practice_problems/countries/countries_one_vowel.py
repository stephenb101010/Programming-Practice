with open("countries.txt") as file:
    names = []
    for line in file:
        line = line.strip("\n")
        