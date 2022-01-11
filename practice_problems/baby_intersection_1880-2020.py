with open("baby_names_1880_short.txt") as names_1880, open("baby_names_2020_short.txt") as names_2020:
    names_80 = set()
    names_20 = set()
    for entry in names_1880:
        entry = entry.strip("\n")
        names_80.add(entry)
    for entry in names_2020:
        entry = entry.strip("\n")
        names_20.add(entry)
names_80.intersection_update(names_20)
print(names_80)