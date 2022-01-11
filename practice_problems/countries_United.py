with open("countries.txt") as file:
    united_countries = []
    for line in file:
        line = line.strip("\n")
        if line.find("United") != -1:
            united_countries.append(line)
print(united_countries)