with open("sowpods.txt") as file:
    total = 0
    for line in file:
        line = line.replace("\n", "")
        if (line.find("TYPE") != -1):
            total +=1
    print(total)