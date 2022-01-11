with open("baby_names_2020_short.txt") as file:
    names = []
    longest_names = []
    for name in file:
        name = name.strip("\n")
        names.append(name)
    names.sort(key= len, reverse= True)
    longest = names[0]
    for name in names:
        if len(name) >= len(longest):
            longest_names.append(name)
print(longest_names)