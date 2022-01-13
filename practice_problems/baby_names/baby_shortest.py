with open("baby_names_2020_short.txt") as file:
    shortest = "aaaaaaaaaa"
    for name in file:
        name = name.strip("\n")
        if len(name) < len(shortest):
            shortest = name
print(shortest)