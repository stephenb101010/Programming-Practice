with open("countries") as file:
    names = []
    for line in file:
        line = line.strip("\n")